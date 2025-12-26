"""
工具函数：日志打印 / 密码加密 / 验证
"""
import datetime
import logging
import bcrypt

# 基础日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)
logger = logging.getLogger("init")


def print_log(level: str, msg: str):
    """统一日志输出格式。"""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"【{level.upper()}】{ts} {msg}")


def encrypt_password(plain: str) -> str:
    """BCrypt 加密明文密码，兼容 Flask-Bcrypt 校验。"""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(plain.encode("utf-8"), salt).decode("utf-8")


def verify_bcrypt_password(plain: str, hashed: str) -> bool:
    """验证明文与加密密码是否匹配。"""
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

