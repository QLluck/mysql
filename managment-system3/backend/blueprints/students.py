from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from backend.extensions import db
from backend.models import Student, User
from backend.utils.decorators import require_roles
from backend.utils.responses import success, error
from backend.utils.pagination import paginate_query
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("students", __name__, url_prefix="/api/students")


@bp.get("")
@jwt_required()
@require_roles("系统管理员")
def list_students():
    query = Student.query
    students, meta = paginate_query(query)
    data = [
        {
            "id": s.id,
            "name": s.name,
            "user_id": s.user_id,
        }
        for s in students
    ]
    return success({"items": data, "meta": meta})


@bp.post("")
@jwt_required()
@require_roles("系统管理员")
def create_student():
    data = request.get_json() or {}
    name = data.get("name")
    user_id = data.get("user_id")
    if not name:
        return error("学生姓名必填", 400)
    if user_id and not User.query.get(user_id):
        return error("用户不存在", 404)
    student = Student(name=name, user_id=user_id)
    db.session.add(student)
    write_log(get_jwt_identity(), "create_student", "student", None, f"name={name}")
    db.session.commit()
    return success({"id": student.id}, "created", 201)


@bp.post("/batch-bind")
@jwt_required()
@require_roles("系统管理员")
def batch_bind():
    """
    批量绑定学生的 user_id
    body: { items: [{student_id, user_id}] }
    """
    data = request.get_json() or {}
    items = data.get("items", [])
    if not items:
        return error("缺少绑定数据", 400)
    for item in items:
        student = Student.query.get(item.get("student_id"))
        if not student:
            continue
        if item.get("user_id") and not User.query.get(item["user_id"]):
            continue
        student.user_id = item.get("user_id")
    write_log(get_jwt_identity(), "batch_bind_students", "student", None, f"count={len(items)}")
    db.session.commit()
    return success({"updated": len(items)})

