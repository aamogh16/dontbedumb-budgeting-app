from flask import Blueprint, request, jsonify
from backend.db_connection import db

users = Blueprint('users', __name__)

# Get all users
@users.route('/', methods=['GET'])
def get_all_users():
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT userID, name, email, userType, supervisorUserID 
        FROM User
    ''')
    users_list = cursor.fetchall()
    cursor.close()
    return jsonify(users_list), 200

# Get single user by ID
@users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT userID, name, email, userType, supervisorUserID 
        FROM User WHERE userID = %s
    ''', (user_id,))
    user = cursor.fetchone()
    cursor.close()
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

# Get dependents (users supervised by this user)
@users.route('/<int:user_id>/dependents', methods=['GET'])
def get_dependents(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT userID, name, email, userType 
        FROM User WHERE supervisorUserID = %s
    ''', (user_id,))
    dependents = cursor.fetchall()
    cursor.close()
    return jsonify(dependents), 200

# Get user's accounts
@users.route('/<int:user_id>/accounts', methods=['GET'])
def get_user_accounts(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT acctID, accType, balance, institution 
        FROM Account WHERE userID = %s
    ''', (user_id,))
    accounts = cursor.fetchall()
    cursor.close()
    return jsonify(accounts), 200

# Create new user
@users.route('/', methods=['POST'])
def create_user():
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        INSERT INTO User (name, email, userType, supervisorUserID)
        VALUES (%s, %s, %s, %s)
    ''', (data['name'], data['email'], data.get('userType'), data.get('supervisorUserID')))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'message': 'User created', 'userID': new_id}), 201

# Update user
@users.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    cursor = db.get_db().cursor()
    
    cursor.execute('''
        UPDATE User SET name = %s, email = %s, userType = %s
        WHERE userID = %s
    ''', (data['name'], data['email'], data.get('userType'), user_id))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'User updated'}), 200

# Delete user
@users.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM User WHERE userID = %s', (user_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({'message': 'User deleted'}), 200