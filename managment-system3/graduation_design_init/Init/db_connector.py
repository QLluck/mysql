"""
数据库连接与执行封装
"""
import pymysql
from pymysql.cursors import DictCursor
from Init import config
from Init.utils import print_log


def get_db_connection(db_name: str = None):
    """获取数据库连接；若 db_name 为空则连接到实例默认库。"""
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=db_name,
            charset=config.MYSQL_CHARSET,
            cursorclass=DictCursor,
            autocommit=False,
        )
        return conn
    except Exception as e:
        print_log("ERROR", f"数据库连接失败: {e}")
        raise


def execute_sql(conn, sql: str, params=None):
    """执行单条 SQL，自动提交，失败回滚。"""
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or ())
        conn.commit()
    except Exception as e:
        conn.rollback()
        print_log("ERROR", f"SQL 执行失败: {e}\nSQL: {sql}")
        raise


def execute_batch_sql(conn, sql_list):
    """批量执行 SQL 列表。"""
    try:
        with conn.cursor() as cursor:
            for sql in sql_list:
                cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print_log("ERROR", f"批量 SQL 执行失败: {e}")
        raise


def close_db_connection(conn):
    """安全关闭连接。"""
    try:
        if conn:
            conn.close()
    except Exception:
        pass

