# -*- coding: utf-8 -*-
"""
配置文件
"""

class Config:
    """应用配置"""
    
    # Flask密钥（用于session加密）
    SECRET_KEY = 'your-secret-key-change-in-production-2024'
    
    # 数据库配置
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = '123456'  # 请修改为实际密码
    DB_NAME = 'graduation_topic_system'
    
    # Session配置（使用Flask内置session，不需要Flask-Session）
    SESSION_COOKIE_NAME = 'graduation_session'
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = 3600  # 1小时
    
    # 其他配置
    JSON_AS_ASCII = False  # 支持中文

