# {{CODE-Cycle-Integration:
#   Task_ID: [#T001]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "创建数据库初始化脚本，用于导入数据库结构"
#   Principle_Applied: "Database Initialization"
# }}
# {{START_MODIFICATIONS}}

"""
数据库初始化脚本
用于导入数据库结构和初始数据
"""

import pymysql
import os
from config import Config

def execute_sql_file(connection, file_path):
    """执行SQL文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    
    # 分割SQL语句
    statements = sql_content.split(';')
    
    success_count = 0
    error_count = 0
    
    with connection.cursor() as cursor:
        for statement in statements:
            statement = statement.strip()
            if statement and not statement.startswith('--') and not statement.startswith('/*'):
                try:
                    cursor.execute(statement)
                    success_count += 1
                except Exception as e:
                    # 忽略表已存在的错误（可能是重复执行）
                    if 'already exists' not in str(e).lower():
                        error_count += 1
                        print(f"警告: {str(e)[:50]}...")
    
    connection.commit()
    if error_count == 0:
        print(f"[OK] 成功执行SQL文件: {file_path}")
    else:
        print(f"[OK] 执行SQL文件: {file_path} (成功: {success_count}, 警告: {error_count})")

def init_database():
    """初始化数据库"""
    config = Config()
    
    try:
        # 连接MySQL服务器（不指定数据库）
        connection = pymysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            charset=config.DB_CHARSET
        )
        
        with connection.cursor() as cursor:
            # 创建数据库（如果不存在）
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"数据库 {config.DB_NAME} 创建成功或已存在")
        
        connection.close()
        
        # 连接到指定数据库
        connection = pymysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            charset=config.DB_CHARSET
        )
        
        # 获取SQL文件路径
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sql_file = os.path.join(base_dir, 'stoic.sql')
        data_file = os.path.join(base_dir, 'stoic_data.sql')
        
        # 执行SQL文件
        if os.path.exists(sql_file):
            print("正在导入数据库结构...")
            execute_sql_file(connection, sql_file)
        else:
            print(f"警告: 找不到SQL文件 {sql_file}")
        
        if os.path.exists(data_file):
            print("正在导入初始数据...")
            execute_sql_file(connection, data_file)
        else:
            print(f"警告: 找不到数据文件 {data_file}")
        
        connection.close()
        print("数据库初始化完成！")
        
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        raise

def test_connection():
    """测试数据库连接"""
    from database import db
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as count FROM 学生')
        student_count = cursor.fetchone()['count']
        cursor.execute('SELECT COUNT(*) as count FROM 导师')
        teacher_count = cursor.fetchone()['count']
        conn.close()
        print(f'\n[OK] 数据库连接测试成功！')
        print(f'  - 学生表: {student_count} 条记录')
        print(f'  - 导师表: {teacher_count} 条记录')
        return True
    except Exception as e:
        print(f'\n[ERROR] 数据库连接测试失败: {e}')
        return False

if __name__ == '__main__':
    init_database()
    test_connection()

# {{END_MODIFICATIONS}}

