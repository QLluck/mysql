from flask import Blueprint
from flask_jwt_extended import jwt_required

from backend.models import Topic, Selection, Teacher, Student
from backend.utils.decorators import require_roles
from backend.utils.responses import success

bp = Blueprint("stats", __name__, url_prefix="/api/stats")


@bp.get("/summary")
@jwt_required()
@require_roles("系统管理员", "教研室主任")
def summary():
    total_topics = Topic.query.count()
    audited_topics = Topic.query.filter(Topic.audit_status == 1).count()
    total_students = Student.query.count()
    total_teachers = Teacher.query.count()
    confirmed = Selection.query.filter(Selection.status == 1).count()
    return success(
        {
            "topics_total": total_topics,
            "topics_audited": audited_topics,
            "teachers": total_teachers,
            "students": total_students,
            "confirmed_selections": confirmed,
        }
    )

