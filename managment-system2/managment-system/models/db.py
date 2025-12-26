# -*- coding: utf-8 -*-
"""
数据库连接模块
"""
import pymysql
from config import Config

def get_db_connection():
    """获取数据库连接"""
    return pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(sql, params=None, fetch_one=False):
    """
    执行查询SQL
    
    Args:
        sql: SQL语句
        params: 参数
        fetch_one: 是否只返回一条记录
        
    Returns:
        查询结果
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            if fetch_one:
                return cursor.fetchone()
            return cursor.fetchall()
    finally:
        conn.close()

def execute_update(sql, params=None):
    """
    执行更新SQL（INSERT/UPDATE/DELETE）
    
    Args:
        sql: SQL语句
        params: 参数
        
    Returns:
        受影响的行数或插入的ID
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params or ())
            conn.commit()
            return cursor.lastrowid or cursor.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

