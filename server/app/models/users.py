from ..extensions import db
from marshmallow import EXCLUDE

class Users(db.Model):
    __tablename__ = "users"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    linked_accounts = db.relationship("LinkedAccounts", back_populates="user", lazy=True)