from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend.extensions import db


class Selection(db.Model):
    __tablename__ = "选题记录"

    id = db.Column("选题ID", db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column("学生ID", db.Integer, ForeignKey("学生.学生ID", ondelete="CASCADE"), nullable=False)
    topic_id = db.Column("课题ID", db.Integer, ForeignKey("课题.课题ID", ondelete="CASCADE"), nullable=False)
    status = db.Column("选题状态", db.SmallInteger, nullable=False, default=0)  # 0待确认 1已确认 2已剔除
    selected_at = db.Column("选题时间", db.DateTime, nullable=False, default=datetime.utcnow)
    latest_submit_at = db.Column("最新提交时间", db.DateTime, nullable=True)
    latest_submit_record = db.Column("最新提交记录", db.Text, nullable=True)
    score = db.Column("成绩", db.Numeric(5, 2), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship("Student", foreign_keys=[student_id], lazy="joined")
    topic = relationship("Topic", foreign_keys=[topic_id], lazy="joined")

