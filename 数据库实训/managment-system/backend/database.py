# {{CODE-Cycle-Integration:
#   Task_ID: [#T001]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "创建数据库连接模块，使用PyMySQL连接MySQL数据库"
#   Principle_Applied: "KISS, DRY, Single Responsibility"
# }}
# {{START_MODIFICATIONS}}

import pymysql
from config import Config

class Database:
    """数据库连接管理类"""
    
    def __init__(self):
        self.config = Config()
    
    def get_new_connection(self):
        """获取新的数据库连接"""
        try:
            return pymysql.connect(
                host=self.config.DB_HOST,
                port=self.config.DB_PORT,
                user=self.config.DB_USER,
                password=self.config.DB_PASSWORD,
                database=self.config.DB_NAME,
                charset=self.config.DB_CHARSET,
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            print(f"数据库连接失败: {e}")
            raise
    
    def execute_query(self, sql, params=None):
        """执行查询操作"""
        conn = None
        try:
            conn = self.get_new_connection()
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"查询执行失败: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def execute_update(self, sql, params=None):
        """执行更新操作（INSERT, UPDATE, DELETE）"""
        conn = None
        try:
            conn = self.get_new_connection()
            with conn.cursor() as cursor:
                affected_rows = cursor.execute(sql, params)
                conn.commit()
                return affected_rows
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"更新执行失败: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # 兼容旧代码的connect方法（虽然现在不再保存状态）
    def connect(self):
        return self.get_new_connection()

# 全局数据库实例
db = Database()

# {{END_MODIFICATIONS}}
