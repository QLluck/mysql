from typing import List

from backend.extensions import db
from backend.models import Role, Permission


def seed_core_rbac():
    """Seed 4 roles与22权限，幂等执行。"""
    perms = [
        # 系统管理
        "新增用户",
        "修改用户信息",
        "删除用户",
        "配置选题规则",
        "修改自己密码",
        # 课题管理
        "提交课题",
        "修改未审核课题",
        "删除未审核课题",
        "查看本教研室待审核课题",
        "审核课题",
        "查看所有已审核课题",
        "查看自己发布的课题",
        # 选题管理
        "预选课题",
        "提交自己选择的课题",
        "取消未确认选题",
        "查看自己的选题状态",
        "查看预选自己课题的学生",
        "确认学生选题",
        "剔除学生选题",
        # 统计管理
        "查看本教研室课题统计",
        "查看本教研室选题统计",
        "查看自己课题的选题统计",
        "查看全系统选题统计",
    ]

    existing = {p.name: p for p in Permission.query.all()}
    perm_objs: List[Permission] = []
    for name in perms:
        if name in existing:
            perm_objs.append(existing[name])
        else:
            obj = Permission(name=name)
            db.session.add(obj)
            perm_objs.append(obj)
    db.session.flush()

    roles_def = {
        "系统管理员": [
            "新增用户",
            "修改用户信息",
            "删除用户",
            "配置选题规则",
            "审核课题",
            "查看全系统选题统计",
            "查看所有已审核课题",
            "修改自己密码",
        ],
        "教研室主任": [
            "查看本教研室待审核课题",
            "审核课题",
            "查看本教研室课题统计",
            "查看本教研室选题统计",
            "查看所有已审核课题",
            "修改自己密码",
        ],
        "普通教师": [
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
        "学生": [
            "查看所有已审核课题",
            "预选课题",
            "提交自己选择的课题",
            "取消未确认选题",
            "查看自己的选题状态",
            "修改自己密码",
        ],
    }

    for role_name, perm_names in roles_def.items():
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name)
            db.session.add(role)
            db.session.flush()
        role.permissions = [Permission.query.filter_by(name=n).first() for n in perm_names]

    db.session.commit()

