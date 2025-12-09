from flask import Blueprint, request, jsonify
from backend.db_connection import db

subscriptions = Blueprint('subscriptions', __name__)

# Get all subscriptions for a user
@subscriptions.route('/user/<int:user_id>', methods=['GET'])
def get_user_subscriptions(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT s.subID, s.name, s.amount, s.frequency, s.startDate, s.nextBilling, s.accountID
        FROM Subscription s
        JOIN Account a ON s.accountID = a.acctID
        WHERE a.userID = %s
        ORDER BY s.nextBilling ASC
    ''', (user_id,))
    
    subs = cursor.fetchall()
    cursor.close()
    
    return jsonify(subs), 200

# Get a specific subscription
@subscriptions.route('/<int:sub_id>', methods=['GET'])
def get_subscription(sub_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT subID, name, amount, frequency, startDate, nextBilling, accountID
        FROM Subscription
        WHERE subID = %s
    ''', (sub_id,))
    
    sub = cursor.fetchone()
    cursor.close()
    
    if sub:
        return jsonify(sub), 200
    return jsonify({"error": "Subscription not found"}), 404

# Create a new subscription
@subscriptions.route('/', methods=['POST'])
def create_subscription():
    data = request.json
    
    name = data.get('name')
    amount = data.get('amount')
    frequency = data.get('frequency')
    start_date = data.get('startDate')
    next_billing = data.get('nextBilling')
    account_id = data.get('accountID')
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        INSERT INTO Subscription (name, amount, frequency, startDate, nextBilling, accountID)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (name, amount, frequency, start_date, next_billing, account_id))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({"subID": new_id, "message": "Subscription created"}), 201

# Update a subscription
@subscriptions.route('/<int:sub_id>', methods=['PUT'])
def update_subscription(sub_id):
    data = request.json
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        UPDATE Subscription
        SET name = %s, amount = %s, frequency = %s, startDate = %s, nextBilling = %s
        WHERE subID = %s
    ''', (data.get('name'), data.get('amount'), data.get('frequency'), 
          data.get('startDate'), data.get('nextBilling'), sub_id))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Subscription updated"}), 200

# Delete a subscription
@subscriptions.route('/<int:sub_id>', methods=['DELETE'])
def delete_subscription(sub_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Subscription WHERE subID = %s', (sub_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Subscription deleted"}), 200