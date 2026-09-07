from ..extensions import db
from marshmallow import EXCLUDE

class Transactions(db.Model):
    __tablename__ = "transactions"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    linked_account_id = db.Column(db.Integer, db.ForeignKey("linked_accounts.id"), nullable=False) # e.g., Mpesa, Gmail, Paypal
    external_transaction_id = db.Column(db.String(255), nullable=False, unique=True) # e.g., "TXN1234567890"
    amount = db.Column(db.Float, nullable=False) # 2000
    currency = db.Column(db.String(3), nullable=False) # e.g., USD, EUR, KES
    description = db.Column(db.String(255), nullable=False) # e.g., "Payment for groceries", "Salary for June"
    type = db.Column(db.String(50), nullable=False)  # e.g., "income", "expense", "transfer"
    transaction_date = db.Column(db.DateTime, nullable=False) # e.g., "2023-06-15 14:30:00"
    merchant_name = db.Column(db.String(255), nullable=True) # e.g., "Walmart", "Amazon"

    linked_account = db.relationship("LinkedAccounts", back_populates="transactions", lazy=True)