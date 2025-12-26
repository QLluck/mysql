from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from backend.extensions import db


class Permission(db.Model):
    __tablename__ = "权限"

    id = db.Column("权限ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("权限名称", db.String(50), nullable=False, unique=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Role(db.Model):
    __tablename__ = "角色"

    id = db.Column("角色ID", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("角色名称", db.String(30), nullable=False, unique=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    permissions = relationship(
        "Permission",
        secondary="角色_权限",
        backref="roles",
        lazy="joined",
    )


class RolePermission(db.Model):
    __tablename__ = "角色_权限"

    role_id = db.Column("角色ID", db.Integer, ForeignKey("角色.角色ID", ondelete="CASCADE"), nullable=False)
    permission_id = db.Column("权限ID", db.Integer, ForeignKey("权限.权限ID", ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("角色ID", "权限ID", name="pk_role_permission"),
        {},
    )


class User(db.Model):
    __tablename__ = "用户"

    id = db.Column("用户ID", db.Integer, primary_key=True, autoincrement=True)
    username = db.Column("用户名", db.String(30), nullable=False, unique=True)
    password = db.Column("密码", db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    roles = relationship(
        "Role",
        secondary="用户_角色",
        backref="users",
        lazy="joined",
    )

    # 反向关联，方便在鉴权时取 teacher / student / director office
    teacher = relationship("Teacher", uselist=False, backref="user", lazy="joined")
    student = relationship("Student", uselist=False, backref="user", lazy="joined")
    researchoffice = relationship("ResearchOffice", uselist=False, backref="director_user", lazy="joined")


class UserRole(db.Model):
    __tablename__ = "用户_角色"

    user_id = db.Column("用户ID", db.Integer, ForeignKey("用户.用户ID", ondelete="CASCADE"), nullable=False)
    role_id = db.Column("角色ID", db.Integer, ForeignKey("角色.角色ID", ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("用户ID", "角色ID", name="pk_user_role"),
        {},
    )

