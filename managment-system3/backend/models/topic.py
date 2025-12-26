from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend.extensions import db


class Topic(db.Model):
    __tablename__ = "课题"

    id = db.Column("课题ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("课题名称", db.String(100), nullable=False, unique=True)
    description = db.Column("课题描述", db.Text, nullable=True)
    audit_status = db.Column("审核状态", db.SmallInteger, nullable=False, default=0)  # 0待审核 1通过 2驳回
    teacher_id = db.Column("教师ID", db.Integer, ForeignKey("教师.教师ID", ondelete="SET NULL"), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    teacher = relationship("Teacher", foreign_keys=[teacher_id], lazy="joined")

