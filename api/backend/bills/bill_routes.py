from flask import Blueprint, request, jsonify
from backend.db_connection import db

bills = Blueprint('bills', __name__)

# Get all bills for a user
@bills.route('/user/<int:user_id>', methods=['GET'])
def get_user_bills(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT b.billID, b.name, b.amount, b.dueDate, b.isPaid, 
               b.isRecurring, b.frequency, b.accountID
        FROM Bill b
        JOIN Account a ON b.accountID = a.acctID
        WHERE a.userID = %s
        ORDER BY b.dueDate ASC
    ''', (user_id,))
    
    bills_list = cursor.fetchall()
    cursor.close()
    
    return jsonify(bills_list), 200

# Get a specific bill
@bills.route('/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT billID, name, amount, dueDate, isPaid, isRecurring, frequency, accountID
        FROM Bill
        WHERE billID = %s
    ''', (bill_id,))
    
    bill = cursor.fetchone()
    cursor.close()
    
    if bill:
        return jsonify(bill), 200
    return jsonify({"error": "Bill not found"}), 404

# Create a new bill
@bills.route('/', methods=['POST'])
def create_bill():
    data = request.json
    
    name = data.get('name')
    amount = data.get('amount')
    due_date = data.get('dueDate')
    is_paid = data.get('isPaid', False)
    is_recurring = data.get('isRecurring', False)
    frequency = data.get('frequency')
    account_id = data.get('accountID')
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        INSERT INTO Bill (name, amount, dueDate, isPaid, isRecurring, frequency, accountID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (name, amount, due_date, is_paid, is_recurring, frequency, account_id))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({"billID": new_id, "message": "Bill created"}), 201

# Update a bill
@bills.route('/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    data = request.json
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        UPDATE Bill
        SET name = %s, amount = %s, dueDate = %s, isPaid = %s, 
            isRecurring = %s, frequency = %s
        WHERE billID = %s
    ''', (data.get('name'), data.get('amount'), data.get('dueDate'), 
          data.get('isPaid'), data.get('isRecurring'), data.get('frequency'), bill_id))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Bill updated"}), 200

# Pay a bill
@bills.route('/<int:bill_id>/pay', methods=['PUT'])
def pay_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Bill SET isPaid = TRUE WHERE billID = %s', (bill_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Bill marked as paid"}), 200

# Unpay a bill
@bills.route('/<int:bill_id>/unpay', methods=['PUT'])
def unpay_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Bill SET isPaid = FALSE WHERE billID = %s', (bill_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Bill marked as unpaid"}), 200

# Delete a bill
@bills.route('/<int:bill_id>', methods=['DELETE'])
def delete_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Bill WHERE billID = %s', (bill_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Bill deleted"}), 200