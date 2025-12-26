"""
初始数据插入逻辑：权限、角色、角色-权限绑定、测试账号与基础业务数据。
"""
from Init.db_connector import execute_sql, execute_batch_sql
from Init.utils import encrypt_password, print_log

# 权限清单
PERMISSIONS = [
    # 系统管理类
    "新增用户",
    "修改用户信息",
    "删除用户",
    "配置选题规则",
    "修改自己密码",
    # 课题管理类
    "提交课题",
    "修改未审核课题",
    "删除未审核课题",
    "查看本教研室待审核课题",
    "审核课题",
    "查看所有已审核课题",
    "查看自己发布的课题",
    # 选题管理类
    "预选课题",
    "提交自己选择的课题",
    "取消未确认选题",
    "查看自己的选题状态",
    "查看预选自己课题的学生",
    "确认学生选题",
    "剔除学生选题",
    # 统计管理类
    "查看本教研室课题统计",
    "查看本教研室选题统计",
    "查看自己课题的选题统计",
    "查看全系统选题统计",
]


def insert_base_permissions(conn):
    sqls = []
    start_id = 100
    for i, name in enumerate(PERMISSIONS):
        sqls.append(
            f"INSERT INTO `权限` (`权限ID`,`权限名称`) VALUES ({start_id + i}, '{name}') ON DUPLICATE KEY UPDATE `权限名称`=VALUES(`权限名称`);"
        )
    execute_batch_sql(conn, sqls)
    print_log("SUCCESS", f"权限表插入完成，共 {len(PERMISSIONS)} 条")


def insert_base_roles(conn):
    roles = ["系统管理员", "教研室主任", "普通教师", "学生"]
    sqls = []
    for i, name in enumerate(roles, start=1):
        sqls.append(
            f"INSERT INTO `角色` (`角色ID`,`角色名称`) VALUES ({i}, '{name}') ON DUPLICATE KEY UPDATE `角色名称`=VALUES(`角色名称`);"
        )
    execute_batch_sql(conn, sqls)
    print_log("SUCCESS", "角色表插入完成")


def bind_role_permissions(conn):
    role_perm_map = {
        1: [
            "新增用户",
            "修改用户信息",
            "删除用户",
            "配置选题规则",
            "审核课题",
            "查看全系统选题统计",
            "查看所有已审核课题",
            "修改自己密码",
        ],
        2: [
            "查看本教研室待审核课题",
            "审核课题",
            "查看本教研室课题统计",
            "查看本教研室选题统计",
            "查看所有已审核课题",
            "修改自己密码",
        ],
        3: [
            "提交课题",
            "修改未审核课题",
            "删除未审核课题",
            "查看自己发布的课题",
            "查看预选自己课题的学生",
            "确认学生选题",
            "剔除学生选题",
            "查看自己课题的选题统计",
            "查看所有已审核课题",
            "修改自己密码",
        ],
        4: [
            "查看所有已审核课题",
            "预选课题",
            "提交自己选择的课题",
            "取消未确认选题",
            "查看自己的选题状态",
            "修改自己密码",
        ],
    }
    sqls = []
    for role_id, perm_names in role_perm_map.items():
        for name in perm_names:
            perm_id = 100 + PERMISSIONS.index(name)
            sqls.append(
                f"INSERT INTO `角色_权限` (`角色ID`,`权限ID`) VALUES ({role_id},{perm_id}) ON DUPLICATE KEY UPDATE `权限ID`=VALUES(`权限ID`);"
            )
    execute_batch_sql(conn, sqls)
    print_log("SUCCESS", "角色_权限 绑定完成")


def insert_test_users(conn):
    users = [
        (1000, "Admin", "admin123456"),
        (1001, "director01", "123456"),
        (1002, "teacher01", "123456"),
        (1003, "student01", "123456"),
    ]
    sqls = []
    for uid, username, plain in users:
        hashed = encrypt_password(plain)
        sqls.append(
          f"INSERT INTO `用户` (`用户ID`,`用户名`,`密码`) VALUES ({uid}, '{username}', '{hashed}') ON DUPLICATE KEY UPDATE `用户名`=VALUES(`用户名`), `密码`=VALUES(`密码`);"
        )
    execute_batch_sql(conn, sqls)
    print_log("SUCCESS", "测试用户插入完成")

    # 绑定角色
    binds = [
        (1000, 1),
        (1001, 2),
        (1002, 3),
        (1003, 4),
    ]
    sqls = [
        f"INSERT INTO `用户_角色` (`用户ID`,`角色ID`) VALUES ({u},{r}) ON DUPLICATE KEY UPDATE `角色ID`=VALUES(`角色ID`);"
        for u, r in binds
    ]
    execute_batch_sql(conn, sqls)
    print_log("SUCCESS", "用户_角色 绑定完成")


def insert_base_business_data(conn):
    # 教研室
    execute_sql(
        conn,
        "INSERT INTO `教研室` (`教研室ID`,`教研室名称`,`用户ID`) VALUES (10,'计算机教研室',1001) "
        "ON DUPLICATE KEY UPDATE `教研室名称`=VALUES(`教研室名称`), `用户ID`=VALUES(`用户ID`);",
    )
    # 教师
    execute_sql(
        conn,
        "INSERT INTO `教师` (`教师ID`,`教师姓名`,`用户ID`,`教研室ID`) VALUES (2000,'教师一',1002,10) "
        "ON DUPLICATE KEY UPDATE `教师姓名`=VALUES(`教师姓名`),`用户ID`=VALUES(`用户ID`),`教研室ID`=VALUES(`教研室ID`);",
    )
    # 学生
    execute_sql(
        conn,
        "INSERT INTO `学生` (`学生ID`,`学生姓名`,`用户ID`) VALUES (3000,'学生一',1003) "
        "ON DUPLICATE KEY UPDATE `学生姓名`=VALUES(`学生姓名`),`用户ID`=VALUES(`用户ID`);",
    )
    print_log("SUCCESS", "基础业务数据插入完成")


def insert_all_base_data(conn):
    insert_base_permissions(conn)
    insert_base_roles(conn)
    bind_role_permissions(conn)
    insert_test_users(conn)
    insert_base_business_data(conn)

