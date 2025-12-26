from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.extensions import db
from backend.models import OperationLog
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.utils.pagination import paginate_query

bp = Blueprint("logs", __name__, url_prefix="/api/logs")


@bp.get("")
@jwt_required()
@require_roles("系统管理员")
def list_logs():
    query = OperationLog.query.order_by(OperationLog.created_at.desc())
    user_id = request.args.get("user_id")
    if user_id:
        query = query.filter(OperationLog.user_id == user_id)
    logs, meta = paginate_query(query)
    data = [log.to_dict() for log in logs]
    return success({"items": data, "meta": meta})

