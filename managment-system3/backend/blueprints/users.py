from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from backend.extensions import db
from backend.models import User, Role, UserRole
from backend.services.auth import hash_password
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("users", __name__, url_prefix="/api/users")


@bp.post("")
@jwt_required()
@require_roles("系统管理员")
def create_user():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password") or "123456"
    if not username:
        return error("用户名必填", 400)
    if User.query.filter_by(username=username).first():
        return error("用户名已存在", 400)
    user = User(username=username, password=hash_password(password))
    db.session.add(user)
    write_log(get_jwt_identity(), "create_user", "user", None, f"username={username}")
    db.session.commit()
    return success({"id": user.id}, "created", 201)


@bp.post("/<int:user_id>/roles")
@jwt_required()
@require_roles("系统管理员")
def bind_roles(user_id: int):
    user = User.query.get(user_id)
    if not user:
        return error("用户不存在", 404)
    data = request.get_json() or {}
    role_ids = data.get("role_ids", [])
    roles = Role.query.filter(Role.id.in_(role_ids)).all()
    user.roles = roles
    write_log(get_jwt_identity(), "bind_roles", "user", user_id, f"roles={role_ids}")
    db.session.commit()
    return success({"id": user.id})

