from flask import Blueprint, request, jsonify
from backend.db_connection import db

transactions = Blueprint('transactions', __name__)

# Get all transactions for a user
@transactions.route('/user/<int:user_id>', methods=['GET'])
def get_user_transactions(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT t.transactionID, t.amount, t.date, t.description, t.method, t.source,
               c.name as categoryName, b.name as budgetName
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        LEFT JOIN Budget b ON t.budgetID = b.budgetID
        WHERE a.userID = %s
        ORDER BY t.date DESC
    ''', (user_id,))
    txns = cursor.fetchall()
    cursor.close()
    return jsonify(txns), 200

# Get income transactions
@transactions.route('/user/<int:user_id>/income', methods=['GET'])
def get_user_income(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT t.transactionID, t.amount, t.date, t.description, t.source,
               c.name as categoryName, b.name as budgetName
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        LEFT JOIN Budget b ON t.budgetID = b.budgetID
        WHERE a.userID = %s AND t.amount > 0
        ORDER BY t.date DESC
    ''', (user_id,))
    txns = cursor.fetchall()
    cursor.close()
    return jsonify(txns), 200

# Get expense transactions
@transactions.route('/user/<int:user_id>/expenses', methods=['GET'])
def get_user_expenses(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT t.transactionID, t.amount, t.date, t.description, t.method,
               c.name as categoryName, b.name as budgetName
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        LEFT JOIN Budget b ON t.budgetID = b.budgetID
        WHERE a.userID = %s AND t.amount < 0
        ORDER BY t.date DESC
    ''', (user_id,))
    txns = cursor.fetchall()
    cursor.close()
    return jsonify(txns), 200

# Get income by source
@transactions.route('/user/<int:user_id>/income/by-source', methods=['GET'])
def get_income_by_source(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT COALESCE(t.source, 'Other') as source, SUM(t.amount) as total
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s AND t.amount > 0
        GROUP BY t.source
        ORDER BY total DESC
    ''', (user_id,))
    sources = cursor.fetchall()
    cursor.close()
    return jsonify(sources), 200

# Get expenses by category
@transactions.route('/user/<int:user_id>/expenses/by-category', methods=['GET'])
def get_expenses_by_category(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT COALESCE(c.name, 'Uncategorized') as category, ABS(SUM(t.amount)) as total
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Category c ON t.categoryID = c.categoryID
        WHERE a.userID = %s AND t.amount < 0
        GROUP BY c.name
        ORDER BY total DESC
    ''', (user_id,))
    categories = cursor.fetchall()
    cursor.close()
    return jsonify(categories), 200

# Get expenses by budget
@transactions.route('/user/<int:user_id>/expenses/by-budget', methods=['GET'])
def get_expenses_by_budget(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT COALESCE(b.name, 'Unbudgeted') as budget, ABS(SUM(t.amount)) as total
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        LEFT JOIN Budget b ON t.budgetID = b.budgetID
        WHERE a.userID = %s AND t.amount < 0
        GROUP BY b.name
        ORDER BY total DESC
    ''', (user_id,))
    budgets = cursor.fetchall()
    cursor.close()
    return jsonify(budgets), 200

# Get monthly trends
@transactions.route('/user/<int:user_id>/monthly', methods=['GET'])
def get_monthly_trends(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT DATE_FORMAT(t.date, '%%Y-%%m') as month,
               SUM(CASE WHEN t.amount > 0 THEN t.amount ELSE 0 END) as income,
               ABS(SUM(CASE WHEN t.amount < 0 THEN t.amount ELSE 0 END)) as expenses
        FROM Transaction t
        JOIN Account a ON t.accountID = a.acctID
        WHERE a.userID = %s
        GROUP BY DATE_FORMAT(t.date, '%%Y-%%m')
        ORDER BY month DESC
        LIMIT 6
    ''', (user_id,))
    trends = cursor.fetchall()
    cursor.close()
    return jsonify(trends), 200

# Create transaction
@transactions.route('/', methods=['POST'])
def create_transaction():
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        INSERT INTO Transaction (amount, date, description, method, source, accountID, categoryID, budgetID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        data['amount'],
        data['date'],
        data['description'],
        data.get('method'),
        data.get('source'),
        data['accountID'],
        data.get('categoryID'),
        data.get('budgetID')
    ))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'message': 'Transaction created', 'transactionID': new_id}), 201

# Update transaction
@transactions.route('/<int:txn_id>', methods=['PUT'])
def update_transaction(txn_id):
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        UPDATE Transaction
        SET amount = %s, date = %s, description = %s, method = %s, source = %s, categoryID = %s, budgetID = %s
        WHERE transactionID = %s
    ''', (
        data['amount'],
        data['date'],
        data['description'],
        data.get('method'),
        data.get('source'),
        data.get('categoryID'),
        data.get('budgetID'),
        txn_id
    ))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Transaction updated'}), 200

# Delete transaction
@transactions.route('/<int:txn_id>', methods=['DELETE'])
def delete_transaction(txn_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Transaction WHERE transactionID = %s', (txn_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'Transaction deleted'}), 200