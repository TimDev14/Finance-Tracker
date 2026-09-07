from extensions import db

class LinkedAccounts(db.Model):
    __tablename__ = "linked_accounts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    provider_account_id = db.Column(db.String(255), nullable=False) # e.g., "mpesa_1234567890"
    provider = db.Column(db.String(255), nullable=False) # e.g., "Mpesa", "Gmail", "Paypal" 
    account_identifier = db.Column(db.String(255), nullable=False) # e.g., "example@gmail.com", "0712345678", "paypal@example.com"
    access_token = db.Column(db.String(255), nullable=False) # e.g., "ya29.a0AfH6SMB..."
    refresh_token = db.Column(db.String(255), nullable=True) # e.g., "1//0g..."
    token_expiry = db.Column(db.DateTime, nullable=True) # e.g., "2023-06-15 14:30:00"
    last_synced = db.Column(db.DateTime, nullable=True) # e.g., "2023-06-15 14:30:00"

    transactions = db.relationship("Transactions", back_populates="linked_account", lazy=True)
    user = db.relationship("Users", back_populates="linked_accounts", lazy=True)