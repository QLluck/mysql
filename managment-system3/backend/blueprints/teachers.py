from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from backend.extensions import db
from backend.models import Teacher, User, ResearchOffice
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.utils.pagination import paginate_query
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("teachers", __name__, url_prefix="/api/teachers")


@bp.get("")
@jwt_required()
@require_roles("系统管理员")
def list_teachers():
    query = Teacher.query
    office_id = request.args.get("office_id")
    if office_id:
        query = query.filter(Teacher.office_id == office_id)
    teachers, meta = paginate_query(query)
    data = [
        {
            "id": t.id,
            "name": t.name,
            "user_id": t.user_id,
            "office_id": t.office_id,
        }
        for t in teachers
    ]
    return success({"items": data, "meta": meta})


@bp.post("")
@jwt_required()
@require_roles("系统管理员")
def create_teacher():
    data = request.get_json() or {}
    name = data.get("name")
    user_id = data.get("user_id")
    office_id = data.get("office_id")
    if not name:
        return error("教师姓名必填", 400)
    if user_id and not User.query.get(user_id):
        return error("用户不存在", 404)
    if office_id and not ResearchOffice.query.get(office_id):
        return error("教研室不存在", 404)
    teacher = Teacher(name=name, user_id=user_id, office_id=office_id)
    db.session.add(teacher)
    write_log(get_jwt_identity(), "create_teacher", "teacher", None, f"name={name}")
    db.session.commit()
    return success({"id": teacher.id}, "created", 201)


@bp.post("/batch-bind")
@jwt_required()
@require_roles("系统管理员")
def batch_bind():
    """
    批量绑定教师的 user_id 与 office_id
    body: { items: [{teacher_id, user_id, office_id}] }
    """
    data = request.get_json() or {}
    items = data.get("items", [])
    if not items:
        return error("缺少绑定数据", 400)
    for item in items:
        teacher = Teacher.query.get(item.get("teacher_id"))
        if not teacher:
            continue
        if item.get("user_id") and not User.query.get(item["user_id"]):
            continue
        if item.get("office_id") and not ResearchOffice.query.get(item["office_id"]):
            continue
        teacher.user_id = item.get("user_id")
        teacher.office_id = item.get("office_id")
    write_log(get_jwt_identity(), "batch_bind_teachers", "teacher", None, f"count={len(items)}")
    db.session.commit()
    return success({"updated": len(items)})

