from flask import Blueprint, request, jsonify
from backend.db_connection import db

loans = Blueprint('loans', __name__)

# Get all loans for a user
@loans.route('/user/<int:user_id>', methods=['GET'])
def get_user_loans(user_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT l.loanID, l.name, l.purpose, l.amount, l.amountPaid, 
               l.interestRate, l.minPayment, l.accountID
        FROM Loan l
        JOIN Account a ON l.accountID = a.acctID
        WHERE a.userID = %s
        ORDER BY l.amount DESC
    ''', (user_id,))
    
    loans_list = cursor.fetchall()
    cursor.close()
    
    return jsonify(loans_list), 200

# Get a specific loan
@loans.route('/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    cursor = db.get_db().cursor()
    cursor.execute('''
        SELECT loanID, name, purpose, amount, amountPaid, interestRate, minPayment, accountID
        FROM Loan
        WHERE loanID = %s
    ''', (loan_id,))
    
    loan = cursor.fetchone()
    cursor.close()
    
    if loan:
        return jsonify(loan), 200
    return jsonify({"error": "Loan not found"}), 404

# Create a new loan
@loans.route('/', methods=['POST'])
def create_loan():
    data = request.json
    
    name = data.get('name')
    purpose = data.get('purpose')
    amount = data.get('amount')
    amount_paid = data.get('amountPaid', 0)
    interest_rate = data.get('interestRate')
    min_payment = data.get('minPayment')
    account_id = data.get('accountID')
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        INSERT INTO Loan (name, purpose, amount, amountPaid, interestRate, minPayment, accountID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (name, purpose, amount, amount_paid, interest_rate, min_payment, account_id))
    
    db.get_db().commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({"loanID": new_id, "message": "Loan created"}), 201

# Update a loan
@loans.route('/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    data = request.json
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        UPDATE Loan
        SET name = %s, purpose = %s, amount = %s, amountPaid = %s, 
            interestRate = %s, minPayment = %s
        WHERE loanID = %s
    ''', (data.get('name'), data.get('purpose'), data.get('amount'), 
          data.get('amountPaid'), data.get('interestRate'), data.get('minPayment'), loan_id))
    
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Loan updated"}), 200

# Make a payment on a loan
@loans.route('/<int:loan_id>/pay', methods=['PUT'])
def pay_loan(loan_id):
    data = request.json
    amount = data.get('amount', 0)
    
    cursor = db.get_db().cursor()
    cursor.execute('''
        UPDATE Loan 
        SET amountPaid = amountPaid + %s 
        WHERE loanID = %s
    ''', (amount, loan_id))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Payment applied successfully"}), 200

# Delete a loan
@loans.route('/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Loan WHERE loanID = %s', (loan_id,))
    db.get_db().commit()
    cursor.close()
    
    return jsonify({"message": "Loan deleted"}), 200