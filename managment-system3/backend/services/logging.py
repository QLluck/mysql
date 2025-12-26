from backend.extensions import db
from backend.models import OperationLog


def write_log(user_id: int, action: str, target_type: str = None, target_id: int = None, detail: str = None):
    log = OperationLog(
        user_id=user_id,
        action=action,
        target_type=target_type,
        target_id=target_id,
        detail=detail,
    )
    db.session.add(log)
    # caller decides commit/rollback

