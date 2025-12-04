# {{CODE-Cycle-Integration:
#   Task_ID: [#T001]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "创建Flask应用配置文件，配置数据库连接"
#   Principle_Applied: "KISS, DRY"
# }}
# {{START_MODIFICATIONS}}

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """应用配置类"""
    # 数据库配置
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 3306))
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'stoic')
    DB_CHARSET = 'utf8mb4'
    
    # Flask配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # CORS配置
    CORS_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

# {{END_MODIFICATIONS}}

