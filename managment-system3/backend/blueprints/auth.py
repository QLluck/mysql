from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from backend.extensions import db
from backend.models import User
from backend.services.auth import authenticate
from backend.utils.responses import success, error
from backend.services.logging import write_log

bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@bp.post("/login")
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return error("用户名或密码为空", 400)

    token = authenticate(db.session, username, password)
    if not token:
        return error("用户名或密码错误", 401)
    user = User.query.filter_by(username=username).first()
    if user:
        write_log(user.id, "login", "user", user.id, None)
    return success({"token": token})


@bp.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    claims = get_jwt()
    user = User.query.get(user_id)
    if not user:
        return error("用户不存在", 404)
    return success(
        {
            "user_id": user.id,
            "username": user.username,
            "roles": claims.get("roles", []),
            "perms": claims.get("perms", []),
        }
    )

