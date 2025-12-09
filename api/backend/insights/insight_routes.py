from flask import Blueprint, jsonify
from backend.db_connection import db

insights = Blueprint('insights', __name__)

# Get AI-powered insights for a user
@insights.route('/user/<int:user_id>', methods=['GET'])
def get_user_insights(user_id):
    cursor = db.get_db().cursor()
    
    # Get income
    cursor.execute('''
        SELECT COALESCE(SUM(t.amount), 0) as income
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount > 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    income = float(cursor.fetchone()['income'])
    
    # Get expenditures
    cursor.execute('''
        SELECT COALESCE(SUM(ABS(t.amount)), 0) as expenses
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    expenses = float(cursor.fetchone()['expenses'])
    
    # Get top spending categories
    cursor.execute('''
        SELECT c.name, SUM(ABS(t.amount)) as total
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
        GROUP BY c.name
        ORDER BY total DESC
        LIMIT 3
    ''', (user_id,))
    top_categories = cursor.fetchall()
    
    # Get categories over budget
    cursor.execute('''
        SELECT c.name, SUM(ABS(t.amount)) as spent, b.limitAmount
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        LEFT JOIN Budget b ON c.categoryID = b.categoryID AND b.userID = %s
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
        GROUP BY c.categoryID, c.name, b.limitAmount
        HAVING spent > limitAmount AND limitAmount > 0
    ''', (user_id, user_id))
    over_budget = cursor.fetchall()
    
    # Get savings goals progress
    cursor.execute('''
        SELECT goalName, currAmt, targAmt
        FROM Saving
        WHERE userID = %s AND currAmt < targAmt
    ''', (user_id,))
    incomplete_goals = cursor.fetchall()
    
    # Calculate metrics
    net_position = income - expenses
    savings_rate = (net_position / income * 100) if income > 0 else 0
    
    # Generate insights
    insights_list = []
    
    # Spending vs income insight
    if net_position < 0:
        insights_list.append(f"You overspent by ${abs(net_position):.0f} this month. Review your spending to get back on track.")
    elif savings_rate < 10:
        insights_list.append(f"Your savings rate is only {savings_rate:.1f}%. Try to save at least 20% of your income.")
    elif savings_rate >= 25:
        insights_list.append(f"Great job! You're saving {savings_rate:.1f}% of your income this month.")
    
    # Top spending category insight
    if top_categories:
        top = top_categories[0]
        pct = (float(top['total']) / expenses * 100) if expenses > 0 else 0
        insights_list.append(f"{top['name']} is your highest expense at ${float(top['total']):.0f} ({pct:.0f}% of spending).")
    
    # Over budget insight
    if over_budget:
        names = [item['name'] for item in over_budget[:2]]
        insights_list.append(f"You're over budget in: {', '.join(names)}. Consider cutting back.")
    
    # Savings goals insight
    if incomplete_goals:
        goal = incomplete_goals[0]
        progress = (float(goal['currAmt']) / float(goal['targAmt']) * 100)
        insights_list.append(f"Your '{goal['goalName']}' goal is {progress:.0f}% complete. Keep going!")
    
    cursor.close()
    return jsonify(insights_list), 200

# Get financial health score
@insights.route('/user/<int:user_id>/health-score', methods=['GET'])
def get_health_score(user_id):
    cursor = db.get_db().cursor()
    
    # Get income
    cursor.execute('''
        SELECT COALESCE(SUM(t.amount), 0) as income
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount > 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    income = float(cursor.fetchone()['income'])
    
    # Get expenditures
    cursor.execute('''
        SELECT COALESCE(SUM(ABS(t.amount)), 0) as expenses
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    expenses = float(cursor.fetchone()['expenses'])
    
    # Get savings total
    cursor.execute('''
        SELECT COALESCE(SUM(currAmt), 0) as saved
        FROM Saving WHERE userID = %s
    ''', (user_id,))
    saved = float(cursor.fetchone()['saved'])
    
    # Calculate score (0-100)
    score = 50  # Base score
    
    net = income - expenses
    savings_rate = (net / income * 100) if income > 0 else 0
    
    # Positive factors
    if net > 0:
        score += 20
    if savings_rate > 15:
        score += 15
    if savings_rate > 25:
        score += 10
    if saved > 0:
        score += 5
    
    # Negative factors
    if net < 0:
        score -= 30
    if savings_rate < 0:
        score -= 20
    
    # Clamp score
    score = max(0, min(100, score))
    
    # Determine label
    if score >= 80:
        label = 'Excellent'
    elif score >= 60:
        label = 'Good'
    elif score >= 40:
        label = 'Fair'
    else:
        label = 'Needs Attention'
    
    result = {
        'score': score,
        'label': label,
        'savingsRate': round(savings_rate, 1),
        'netPosition': net
    }
    
    cursor.close()
    return jsonify(result), 200

# Get spending recommendations
@insights.route('/user/<int:user_id>/recommendations', methods=['GET'])
def get_recommendations(user_id):
    cursor = db.get_db().cursor()
    
    # Get income and expenses
    cursor.execute('''
        SELECT COALESCE(SUM(t.amount), 0) as income
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount > 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    income = float(cursor.fetchone()['income'])
    
    cursor.execute('''
        SELECT COALESCE(SUM(ABS(t.amount)), 0) as expenses
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    expenses = float(cursor.fetchone()['expenses'])
    
    # Get top categories for potential savings
    cursor.execute('''
        SELECT c.name, SUM(ABS(t.amount)) as total
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        WHERE a.userID = %s AND t.amount < 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
        GROUP BY c.name
        ORDER BY total DESC
        LIMIT 3
    ''', (user_id,))
    top_categories = cursor.fetchall()
    
    recommendations = []
    
    net = income - expenses
    savings_rate = (net / income * 100) if income > 0 else 0
    
    # Savings rate recommendation
    if savings_rate < 20:
        recommendations.append({
            'title': 'Increase Your Savings Rate',
            'description': f'Your current savings rate is {savings_rate:.1f}%. Aim for at least 20%.',
            'impact': 'High',
            'action': 'Try reducing discretionary spending by 10%'
        })
    
    # Negative cash flow
    if net < 0:
        recommendations.append({
            'title': 'Negative Cash Flow Alert',
            'description': f'You are spending ${abs(net):.0f} more than you earn.',
            'impact': 'Critical',
            'action': 'Identify and cut non-essential expenses immediately'
        })
    
    # Top spending category
    if top_categories:
        top = top_categories[0]
        potential = float(top['total']) * 0.15
        recommendations.append({
            'title': f'Optimize {top["name"]} Spending',
            'description': f'You spent ${float(top["total"]):.0f} on {top["name"]} this month.',
            'impact': 'Medium',
            'action': f'A 15% reduction could save you ${potential:.0f}/month'
        })
    
    # Positive reinforcement
    if savings_rate >= 25:
        recommendations.append({
            'title': 'Excellent Savings Habit',
            'description': f'You are saving {savings_rate:.1f}% of your income - well above average!',
            'impact': 'Positive',
            'action': 'Consider investing surplus in tax-advantaged accounts'
        })
    
    cursor.close()
    return jsonify(recommendations), 200