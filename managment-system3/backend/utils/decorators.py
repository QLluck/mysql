from functools import wraps
from flask import request
from flask_jwt_extended import get_jwt, verify_jwt_in_request

from backend.utils.responses import error


def require_perms(*perm_names):
    """Require user to hold ANY of the provided permission names."""

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_perms = claims.get("perms", [])
            if not any(p in user_perms for p in perm_names):
                return error("forbidden", 403)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def require_roles(*role_names):
    """Require user to hold ANY of the provided role names."""

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_roles = claims.get("roles", [])
            if not any(r in user_roles for r in role_names):
                return error("forbidden", 403)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def scope_filter(payload_key, attr_name):
    """
    Injects scope value from JWT claims into request view kwargs.
    Example: @scope_filter("teacher_id", "teacher_id") will set kwargs["teacher_id"].
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if payload_key not in claims:
                return error("forbidden", 403)
            kwargs[attr_name] = claims[payload_key]
            return fn(*args, **kwargs)

        return wrapper

    return decorator

