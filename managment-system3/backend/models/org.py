from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend.extensions import db


class ResearchOffice(db.Model):
    __tablename__ = "教研室"

    id = db.Column("教研室ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("教研室名称", db.String(50), nullable=False, unique=True)
    user_id = db.Column("用户ID", db.Integer, ForeignKey("用户.用户ID", ondelete="SET NULL"), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    director = relationship("User", foreign_keys=[user_id], lazy="joined")


class Teacher(db.Model):
    __tablename__ = "教师"

    id = db.Column("教师ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("教师姓名", db.String(30), nullable=False)
    user_id = db.Column("用户ID", db.Integer, ForeignKey("用户.用户ID", ondelete="SET NULL"), nullable=True)
    office_id = db.Column("教研室ID", db.Integer, ForeignKey("教研室.教研室ID", ondelete="SET NULL"), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", foreign_keys=[user_id], lazy="joined")
    office = relationship("ResearchOffice", foreign_keys=[office_id], lazy="joined")


class Student(db.Model):
    __tablename__ = "学生"

    id = db.Column("学生ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("学生姓名", db.String(30), nullable=False)
    user_id = db.Column("用户ID", db.Integer, ForeignKey("用户.用户ID", ondelete="SET NULL"), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", foreign_keys=[user_id], lazy="joined")

