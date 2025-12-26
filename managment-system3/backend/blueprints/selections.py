from datetime import datetime
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt

from backend.extensions import db
from backend.models import Selection, Topic, Teacher
from backend.utils.responses import success, error
from backend.services.logging import write_log
from flask_jwt_extended import get_jwt_identity

bp = Blueprint("selections", __name__, url_prefix="/api/selections")


@bp.get("")
@jwt_required()
def list_selections():
    claims = get_jwt()
    roles = claims.get("roles", [])
    student_id = claims.get("student_id")
    teacher_id = claims.get("teacher_id")
    office_id = claims.get("office_id")

    query = Selection.query

    if "系统管理员" not in roles:
        if "学生" in roles and student_id:
            query = query.filter(Selection.student_id == student_id)
        elif "普通教师" in roles and teacher_id:
            query = query.join(Selection.topic).join(Teacher).filter(Teacher.id == teacher_id)
        elif "教研室主任" in roles and office_id:
            query = query.join(Selection.topic).join(Teacher).filter(Teacher.office_id == office_id)
        else:
            return error("无权限", 403)

    selections = query.all()
    data = [
        {
            "id": s.id,
            "student_id": s.student_id,
            "topic_id": s.topic_id,
            "status": s.status,
            "score": float(s.score) if s.score is not None else None,
        }
        for s in selections
    ]
    return success(data)


@bp.post("")
@jwt_required()
def create_selection():
    claims = get_jwt()
    roles = claims.get("roles", [])
    student_id = claims.get("student_id")
    if "学生" not in roles or not student_id:
        return error("仅学生可预选", 403)

    data = request.get_json() or {}
    topic_id = data.get("topic_id")
    if not topic_id:
        return error("缺少课题ID", 400)

    # 检查已确认唯一
    confirmed = Selection.query.filter_by(student_id=student_id, status=1).first()
    if confirmed:
        return error("已有已确认选题，需先取消", 400)

    selection = Selection(
        student_id=student_id,
        topic_id=topic_id,
        status=0,
        selected_at=datetime.utcnow(),
    )
    db.session.add(selection)
    write_log(get_jwt_identity(), "create_selection", "selection", None, f"topic_id={topic_id}")
    db.session.commit()
    return success({"id": selection.id}, "created", 201)


@bp.put("/<int:selection_id>")
@jwt_required()
def update_selection(selection_id: int):
    claims = get_jwt()
    roles = claims.get("roles", [])
    student_id = claims.get("student_id")
    teacher_id = claims.get("teacher_id")
    selection = Selection.query.get(selection_id)
    if not selection:
        return error("记录不存在", 404)

    data = request.get_json() or {}

    is_admin = "系统管理员" in roles
    is_teacher = "普通教师" in roles and teacher_id
    is_student = "学生" in roles and student_id

    if is_admin:
        pass
    elif is_teacher:
        if not selection.topic or selection.topic.teacher_id != teacher_id:
            return error("无权限", 403)
    elif is_student:
        if selection.student_id != student_id:
            return error("无权限", 403)
        if selection.status != 0:
            return error("仅可修改/取消待确认记录", 400)
    else:
        return error("无权限", 403)

    # 学生可更新提交记录/时间或取消
    if is_student:
        if "latest_submit_record" in data:
            selection.latest_submit_record = data.get("latest_submit_record")
            selection.latest_submit_at = datetime.utcnow()
        if data.get("cancel"):
            selection.status = 2
        db.session.commit()
        return success({"id": selection.id})

    # 教师/管理员更新状态、成绩
    if "status" in data:
        selection.status = int(data["status"])
    if "score" in data:
        selection.score = data["score"]
    write_log(get_jwt_identity(), "update_selection", "selection", selection.id, f"payload_keys={list(data.keys())}")
    db.session.commit()
    return success({"id": selection.id})

