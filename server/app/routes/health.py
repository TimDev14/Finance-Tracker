from flask import Blueprint

health_bp = Blueprint('health', __name__, url_prefix='/api/health')

@health_bp.get("")
def health_check():
    return {
         "status": "ok",
        "message": "Finance Tracker API is running"
    }