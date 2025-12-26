"""
配置读取模块
职责：读取 .env / 环境变量，提供 MySQL 连接配置与初始化选项。
"""
import os
from dotenv import load_dotenv


load_dotenv()  # 优先加载同目录/父目录下的 .env

# 必填配置
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT") or 3306)
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("DB_NAME") or "graduation_design"
MYSQL_CHARSET = os.getenv("MYSQL_CHARSET") or "utf8mb4"

# 可选配置：是否在初始化前删除旧表
DROP_OLD_TABLES = os.getenv("DROP_OLD_TABLES", "false").lower() == "true"


def validate_config():
    """校验关键配置完整性，缺失则抛出异常。"""
    missing = []
    for key, val in [
        ("MYSQL_HOST", MYSQL_HOST),
        ("MYSQL_USER", MYSQL_USER),
        ("MYSQL_PASSWORD", MYSQL_PASSWORD),
    ]:
        if not val:
            missing.append(key)
    if missing:
        raise ValueError(f"配置缺失: {', '.join(missing)}，请在 .env 中补充")

