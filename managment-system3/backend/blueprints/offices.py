from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from backend.extensions import db
from backend.models import ResearchOffice, User
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.utils.pagination import paginate_query
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("offices", __name__, url_prefix="/api/offices")


@bp.get("")
@jwt_required()
@require_roles("系统管理员")
def list_offices():
    query = ResearchOffice.query
    offices, meta = paginate_query(query)
    data = [
        {
            "id": o.id,
            "name": o.name,
            "user_id": o.user_id,
        }
        for o in offices
    ]
    return success({"items": data, "meta": meta})


@bp.post("")
@jwt_required()
@require_roles("系统管理员")
def create_office():
    data = request.get_json() or {}
    name = data.get("name")
    user_id = data.get("user_id")
    if not name:
        return error("教研室名称必填", 400)
    if ResearchOffice.query.filter_by(name=name).first():
        return error("教研室名称已存在", 400)
    office = ResearchOffice(name=name, user_id=user_id)
    db.session.add(office)
    write_log(get_jwt_identity(), "create_office", "office", None, f"name={name}")
    db.session.commit()
    return success({"id": office.id}, "created", 201)


@bp.post("/bind-director")
@jwt_required()
@require_roles("系统管理员")
def bind_director():
    data = request.get_json() or {}
    office_id = data.get("office_id")
    user_id = data.get("user_id")
    office = ResearchOffice.query.get(office_id)
    if not office:
        return error("教研室不存在", 404)
    if user_id and not User.query.get(user_id):
        return error("用户不存在", 404)
    office.user_id = user_id
    write_log(get_jwt_identity(), "bind_director", "office", office_id, f"user_id={user_id}")
    db.session.commit()
    return success({"id": office.id})

