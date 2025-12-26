from datetime import datetime
from backend.extensions import db


class OperationLog(db.Model):
    __tablename__ = "操作日志"

    id = db.Column("日志ID", db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column("用户ID", db.Integer, nullable=False)
    action = db.Column("操作", db.String(100), nullable=False)
    target_type = db.Column("目标类型", db.String(50), nullable=True)
    target_id = db.Column("目标ID", db.Integer, nullable=True)
    detail = db.Column("详情", db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "action": self.action,
            "target_type": self.target_type,
            "target_id": self.target_id,
            "detail": self.detail,
            "created_at": self.created_at.isoformat(),
        }

