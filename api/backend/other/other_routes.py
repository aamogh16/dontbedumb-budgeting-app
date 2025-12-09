from flask import Blueprint, request, jsonify
from backend.db_connection import db

other = Blueprint('other', __name__)

# Get debt summary for a user
@other.route('/user/<int:user_id>/debt', methods=['GET'])
def get_user_debt(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT l.loanID, l.name, l.purpose, l.amount, l.amountPaid, 
               l.interestRate, l.minPayment,
               (l.amount - l.amountPaid) as balance
        FROM Loan l
        JOIN Account a ON l.accountID = a.acctID
        WHERE a.userID = %s
    ''', (user_id,))
    loans = cursor.fetchall()
    
    # Calculate totals
    total_debt = sum(float(loan['amount']) - float(loan['amountPaid']) for loan in loans)
    monthly_payment = sum(float(loan['minPayment'] or 0) for loan in loans)
    
    # Get income for debt ratio
    cursor.execute('''
        SELECT COALESCE(SUM(t.amount), 0) as income
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount > 0
        AND MONTH(t.date) = MONTH(CURRENT_DATE())
        AND YEAR(t.date) = YEAR(CURRENT_DATE())
    ''', (user_id,))
    income = float(cursor.fetchone()['income'])
    debt_ratio = (monthly_payment / income * 100) if income > 0 else 0
    
    result = {
        'total': total_debt,
        'monthlyPayment': monthly_payment,
        'ratio': round(debt_ratio, 1),
        'accounts': loans
    }
    
    cursor.close()
    return jsonify(result), 200

# Get investments for a user
@other.route('/user/<int:user_id>/investments', methods=['GET'])
def get_user_investments(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT investmentID, name, accountType, balance, returnRate
        FROM Investment
        WHERE userID = %s
    ''', (user_id,))
    investments = cursor.fetchall()
    
    # Calculate totals
    total = sum(float(inv['balance']) for inv in investments)
    weighted_return = 0
    if total > 0:
        for inv in investments:
            weight = float(inv['balance']) / total
            weighted_return += weight * float(inv['returnRate'] or 0)
    
    returns = total * (weighted_return / 100)
    
    result = {
        'total': total,
        'returns': round(returns, 2),
        'returnRate': round(weighted_return, 1),
        'accounts': investments
    }
    
    cursor.close()
    return jsonify(result), 200

# Get subscriptions for a user
@other.route('/user/<int:user_id>/subscriptions', methods=['GET'])
def get_user_subscriptions(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT s.subID, s.name, s.amount, s.frequency, s.startDate, s.nextBilling
        FROM Subscription s
        JOIN Account a ON s.accountID = a.acctID
        WHERE a.userID = %s
        ORDER BY s.nextBilling ASC
    ''', (user_id,))
    subs = cursor.fetchall()
    
    # Calculate monthly total
    total = sum(float(sub['amount']) for sub in subs)
    
    result = {
        'total': total,
        'items': subs
    }
    
    cursor.close()
    return jsonify(result), 200

# Create new loan/debt
@other.route('/debt', methods=['POST'])
def create_debt():
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        INSERT INTO Loan (name, purpose, amount, amountPaid, interestRate, minPayment, accountID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (
        data['name'],
        data.get('purpose'),
        data['amount'],
        data.get('amountPaid', 0),
        data.get('interestRate'),
        data.get('minPayment'),
        data['accountID']
    ))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'message': 'Debt account created', 'loanID': new_id}), 201

# Update loan payment
@other.route('/debt/<int:loan_id>', methods=['PUT'])
def update_debt(loan_id):
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        UPDATE Loan 
        SET name = %s, amountPaid = %s, interestRate = %s, minPayment = %s
        WHERE loanID = %s
    ''', (
        data['name'],
        data.get('amountPaid', 0),
        data.get('interestRate'),
        data.get('minPayment'),
        loan_id
    ))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Debt updated'}), 200

# Delete loan
@other.route('/debt/<int:loan_id>', methods=['DELETE'])
def delete_debt(loan_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Loan WHERE loanID = %s', (loan_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Debt deleted'}), 200

# Create new investment
@other.route('/investments', methods=['POST'])
def create_investment():
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        INSERT INTO Investment (name, accountType, balance, returnRate, userID)
        VALUES (%s, %s, %s, %s, %s)
    ''', (
        data['name'],
        data.get('accountType'),
        data.get('balance', 0),
        data.get('returnRate'),
        data['userID']
    ))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'message': 'Investment created', 'investmentID': new_id}), 201

# Update investment
@other.route('/investments/<int:inv_id>', methods=['PUT'])
def update_investment(inv_id):
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        UPDATE Investment 
        SET name = %s, accountType = %s, balance = %s, returnRate = %s
        WHERE investmentID = %s
    ''', (
        data['name'],
        data.get('accountType'),
        data.get('balance', 0),
        data.get('returnRate'),
        inv_id
    ))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Investment updated'}), 200

# Delete investment
@other.route('/investments/<int:inv_id>', methods=['DELETE'])
def delete_investment(inv_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Investment WHERE investmentID = %s', (inv_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Investment deleted'}), 200

# Create new subscription
@other.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        INSERT INTO Subscription (name, amount, frequency, startDate, nextBilling, accountID)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        data['name'],
        data['amount'],
        data.get('frequency', 'monthly'),
        data['startDate'],
        data.get('nextBilling'),
        data['accountID']
    ))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'message': 'Subscription created', 'subID': new_id}), 201

# Update subscription
@other.route('/subscriptions/<int:sub_id>', methods=['PUT'])
def update_subscription(sub_id):
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        UPDATE Subscription 
        SET name = %s, amount = %s, frequency = %s, nextBilling = %s
        WHERE subID = %s
    ''', (
        data['name'],
        data['amount'],
        data.get('frequency', 'monthly'),
        data.get('nextBilling'),
        sub_id
    ))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Subscription updated'}), 200

# Delete subscription
@other.route('/subscriptions/<int:sub_id>', methods=['DELETE'])
def delete_subscription(sub_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Subscription WHERE subID = %s', (sub_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Subscription deleted'}), 200