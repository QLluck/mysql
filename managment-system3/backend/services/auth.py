from typing import Optional
from flask import request
from flask_jwt_extended import create_access_token

from backend.extensions import bcrypt
from backend.models import User


def hash_password(plain: str) -> str:
    return bcrypt.generate_password_hash(plain).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.check_password_hash(hashed, plain)


def authenticate(db_session, username: str, password: str) -> Optional[str]:
    user: Optional[User] = User.query.filter_by(username=username).first()
    if not user or not verify_password(password, user.password):
        return None

    role_names = [r.name for r in user.roles]
    perms = {p.name for r in user.roles for p in r.permissions}

    additional_claims = {
        "user_id": user.id,
        "username": user.username,
        "roles": role_names,
        "perms": list(perms),
    }
    # scope hints for downstream过滤
    teacher = getattr(user, "teacher", None)
    if teacher:
        additional_claims["teacher_id"] = teacher.id
        if teacher.office_id:
            additional_claims["office_id"] = teacher.office_id
    student = getattr(user, "student", None)
    if student:
        additional_claims["student_id"] = student.id
    director_office = getattr(user, "researchoffice", None)
    if director_office:
        additional_claims["office_id"] = director_office.id

    token = create_access_token(identity=user.id, additional_claims=additional_claims)
    return token

