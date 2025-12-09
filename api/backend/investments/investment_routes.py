from flask import Blueprint, request, jsonify
from backend.db_connection import db

investments = Blueprint('investments', __name__)

# Get all investments for a user
@investments.route('/user/<int:user_id>', methods=['GET'])
def get_user_investments(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT investmentID, name, accountType, balance, returnRate, userID
        FROM Investment
        WHERE userID = %s
        ORDER BY balance DESC
    ''', (user_id,))
    
    investments_list = cursor.fetchall()
    cursor.close()
    
    return jsonify(investments_list), 200

# Get a specific investment
@investments.route('/<int:investment_id>', methods=['GET'])
def get_investment(investment_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT investmentID, name, accountType, balance, returnRate, userID
        FROM Investment
        WHERE investmentID = %s
    ''', (investment_id,))
    
    investment = cursor.fetchone()
    cursor.close()
    
    if investment:
        return jsonify(investment), 200
    return jsonify({"error": "Investment not found"}), 404

# Create a new investment
@investments.route('/', methods=['POST'])
def create_investment():
    data = request.json
    
    name = data.get('name')
    account_type = data.get('accountType')
    balance = data.get('balance', 0)
    return_rate = data.get('returnRate')
    user_id = data.get('userID')
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        INSERT INTO Investment (name, accountType, balance, returnRate, userID)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, account_type, balance, return_rate, user_id))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({"investmentID": new_id, "message": "Investment created"}), 201

# Update an investment
@investments.route('/<int:investment_id>', methods=['PUT'])
def update_investment(investment_id):
    data = request.json
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        UPDATE Investment
        SET name = %s, accountType = %s, balance = %s, returnRate = %s
        WHERE investmentID = %s
    ''', (data.get('name'), data.get('accountType'), data.get('balance'), 
          data.get('returnRate'), investment_id))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Investment updated"}), 200

# Delete an investment
@investments.route('/<int:investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Investment WHERE investmentID = %s', (investment_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Investment deleted"}), 200