from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from backend.extensions import db
from backend.models import Role, Permission
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("roles", __name__, url_prefix="/api/roles")


@bp.get("")
@jwt_required()
@require_roles("系统管理员")
def list_roles():
    roles = Role.query.all()
    data = [{"id": r.id, "name": r.name, "permissions": [p.name for p in r.permissions]} for r in roles]
    return success(data)


@bp.post("")
@jwt_required()
@require_roles("系统管理员")
def create_role():
    data = request.get_json() or {}
    name = data.get("name")
    if not name:
        return error("角色名称必填", 400)
    if Role.query.filter_by(name=name).first():
        return error("角色名称已存在", 400)
    role = Role(name=name)
    db.session.add(role)
    write_log(get_jwt_identity(), "create_role", "role", None, f"name={name}")
    db.session.commit()
    return success({"id": role.id}, "created", 201)


@bp.post("/<int:role_id>/perms")
@jwt_required()
@require_roles("系统管理员")
def bind_perms(role_id: int):
    role = Role.query.get(role_id)
    if not role:
        return error("角色不存在", 404)
    data = request.get_json() or {}
    perm_names = data.get("permissions", [])
    perms = Permission.query.filter(Permission.name.in_(perm_names)).all()
    role.permissions = perms
    write_log(get_jwt_identity(), "bind_perms", "role", role_id, f"perms={perm_names}")
    db.session.commit()
    return success({"id": role.id})

