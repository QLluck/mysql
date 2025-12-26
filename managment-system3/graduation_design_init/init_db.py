"""
初始化入口脚本
执行：python init_db.py
流程：加载配置 -> 创建数据库 -> 创建表 -> 插入基础数据
"""
import sys
import pymysql
from Init import config
from Init.utils import print_log
from Init.db_connector import get_db_connection, execute_sql, close_db_connection
from Init.table_creator import create_all_tables
from Init.data_inserter import insert_all_base_data


def ensure_database():
    """创建数据库（如不存在）。"""
    conn = None
    try:
        conn = get_db_connection(db_name=None)
        execute_sql(
            conn,
            f"CREATE DATABASE IF NOT EXISTS `{config.DB_NAME}` CHARACTER SET {config.MYSQL_CHARSET} COLLATE utf8mb4_unicode_ci;",
        )
        print_log("SUCCESS", f"数据库 `{config.DB_NAME}` 已存在或创建成功")
    finally:
        close_db_connection(conn)


def main():
    print_log("INFO", "开始执行数据库初始化")
    try:
        config.validate_config()
    except Exception as e:
        print_log("ERROR", str(e))
        sys.exit(1)

    # 创建数据库
    ensure_database()

    # 连接指定库
    conn = get_db_connection(db_name=config.DB_NAME)
    try:
        # 创建表
        create_all_tables(conn, drop_old=config.DROP_OLD_TABLES)
        # 插入基础数据
        insert_all_base_data(conn)
        print_log("SUCCESS", "✅ 数据库初始化完成！")
        print_log("INFO", "可执行验证 SQL 示例：SELECT * FROM `角色`;")
    except Exception as e:
        print_log("ERROR", f"初始化失败: {e}")
    finally:
        close_db_connection(conn)


if __name__ == "__main__":
    main()

