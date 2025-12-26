from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, get_jwt, jwt_required

from backend.extensions import db
from backend.models import Topic, Teacher, User
from backend.utils.decorators import require_perms
from backend.utils.responses import success, error
from backend.services.logging import write_log

bp = Blueprint("topics", __name__, url_prefix="/api/topics")


@bp.get("")
@jwt_required()
def list_topics():
    claims = get_jwt()
    query = Topic.query
    audit_status = request.args.get("audit_status")
    if audit_status is not None:
        query = query.filter(Topic.audit_status == int(audit_status))

    roles = claims.get("roles", [])
    office_id = claims.get("office_id")
    teacher_id = claims.get("teacher_id")

    # 数据范围过滤
    if "系统管理员" not in roles:
        if "教研室主任" in roles and office_id:
            query = query.join(Teacher).filter(Teacher.office_id == office_id)
        elif "普通教师" in roles and teacher_id:
            query = query.filter(Topic.teacher_id == teacher_id)

    topics = query.all()
    data = [
        {
            "id": t.id,
            "name": t.name,
            "audit_status": t.audit_status,
            "teacher_id": t.teacher_id,
        }
        for t in topics
    ]
    return success(data)


@bp.post("")
@require_perms("提交课题")
def create_topic():
    claims = get_jwt()
    teacher_id = claims.get("teacher_id")
    if not teacher_id:
        return error("当前用户未绑定教师信息", 400)

    data = request.get_json() or {}
    name = data.get("name")
    description = data.get("description")
    if not name:
        return error("课题名称必填", 400)

    if Topic.query.filter_by(name=name).first():
        return error("课题名称已存在", 400)

    topic = Topic(name=name, description=description, teacher_id=teacher_id, audit_status=0)
    db.session.add(topic)
    write_log(get_jwt_identity(), "create_topic", "topic", None, f"name={name}")
    db.session.commit()
    return success({"id": topic.id}, "created", 201)


@bp.put("/<int:topic_id>")
@jwt_required()
def update_topic(topic_id: int):
    claims = get_jwt()
    roles = claims.get("roles", [])
    teacher_id = claims.get("teacher_id")
    office_id = claims.get("office_id")

    topic = Topic.query.get(topic_id)
    if not topic:
        return error("课题不存在", 404)

    data = request.get_json() or {}

    is_admin = "系统管理员" in roles
    is_director = "教研室主任" in roles
    is_teacher = "普通教师" in roles

    # 权限校验与范围校验
    if is_admin:
        pass
    elif is_director:
        if not office_id or not topic.teacher or topic.teacher.office_id != office_id:
            return error("无权限", 403)
        # 主任仅允许改审核状态
        new_status = data.get("audit_status")
        if new_status is None:
            return error("主任只能修改审核状态", 400)
        topic.audit_status = int(new_status)
        db.session.commit()
        return success({"id": topic.id})
    elif is_teacher:
        if topic.teacher_id != teacher_id:
            return error("无权限", 403)
        if topic.audit_status != 0:
            return error("仅可修改待审核课题", 400)
    else:
        return error("无权限", 403)

    # 管理员/教师更新基础字段
    if "name" in data:
        name = data["name"]
        if Topic.query.filter(Topic.id != topic.id, Topic.name == name).first():
            return error("课题名称已存在", 400)
        topic.name = name
    if "description" in data:
        topic.description = data["description"]
    if is_admin and "teacher_id" in data:
        topic.teacher_id = data["teacher_id"]
    if "audit_status" in data:
        topic.audit_status = int(data["audit_status"])

    write_log(get_jwt_identity(), "update_topic", "topic", topic.id, f"payload_keys={list(data.keys())}")
    db.session.commit()
    return success({"id": topic.id})


@bp.delete("/<int:topic_id>")
@jwt_required()
def delete_topic(topic_id: int):
    claims = get_jwt()
    roles = claims.get("roles", [])
    teacher_id = claims.get("teacher_id")

    topic = Topic.query.get(topic_id)
    if not topic:
        return error("课题不存在", 404)

    is_admin = "系统管理员" in roles
    is_teacher = "普通教师" in roles

    if is_admin:
        pass
    elif is_teacher:
        if topic.teacher_id != teacher_id:
            return error("无权限", 403)
        if topic.audit_status != 0:
            return error("仅可删除待审核课题", 400)
    else:
        return error("无权限", 403)

    db.session.delete(topic)
    write_log(get_jwt_identity(), "delete_topic", "topic", topic_id, None)
    db.session.commit()
    return success({"id": topic_id}, "deleted")

