from extensions import db
from utils import get_current_user_id
from models.transactions import Transactions

from flask import request, jsonify

class TransactionsController:
    user = get_current_user_id()
    # Create a new transaction
    @classmethod
    def create_transaction(self, data):
        payload = dict(data)
        new_transaction = Transactions(**data)
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify({"message": "Transaction created successfully", "transaction": new_transaction.to_dict()}), 201
    # Get all transactions for a user
    @classmethod
    def get_user_transactions(cls):
        transactions = Transactions.query.filter_by(user_id=cls.user).all()
        if not transactions:
            return jsonify({"message": "No transactions found for user"}), 404
        return jsonify({"transactions": [transaction.to_dict() for transaction in transactions]}), 200

    # Get one transaction by ID
    @classmethod
    def get_transaction(cls, transaction_id):
        if not transaction_id:
            return jsonify({"message": "Transaction not found"}), 400
        transaction = Transactions.query.filter_by(id=transaction_id).first()
        if not transaction:
            return jsonify({"message": "Transaction not found"}), 404
        return jsonify({"transaction": transaction.to_dict()}), 200
    # Get all transactions
    # update transaction
    # delete transaction

    pass