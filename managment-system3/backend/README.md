# 毕业设计选题管理系统 - 后端 (Flask)
/backend/env
#这个要改
DATABASE_URL=mysql://root:123456@localhost:3306/graduation_project
# 测试环境数据库（可选，不用改）
TEST_DATABASE_URL=sqlite:///:memory:

# ==================== JWT配置 ====================
# 替换为随机字符串（比如生成32位随机数，避免默认值）
JWT_SECRET_KEY=my-jwt-secret-key-2025-abc123def456

# ==================== 加密配置 ====================
# BCrypt加密轮数（保持12即可，无需修改）
BCRYPT_LOG_ROUNDS=12
## 快速启动
```bash
cd backend

# 步骤2：安装依赖（直接装到系统Python环境，仅第一次需要）
pip install -r requirements.txt

# 步骤3：启动后端服务（核心指令，默认5000端口）
python -m backend.app                  # 开发启动，默认 5000
```

## 主要设计
- 10 张核心表，模型名与中文表名一一对应。
- JWT 认证 + RBAC 权限校验，`@require_roles` / `@require_perms` 装饰器。
- 数据范围过滤：主任按教研室、教师按自己的教师ID、学生按自己的学生ID，管理员无限制。
- 课题/选题状态校验：教师/主任/学生的可操作状态与范围均在接口层检查。

## 已提供的蓝图
- `/api/auth`: 登录、获取当前用户
- `/api/roles`: 角色与权限绑定（管理员）
- `/api/users`: 用户创建与角色绑定（管理员）
- `/api/topics`: 课题 CRUD，含范围/状态校验
- `/api/selections`: 选题记录增改查，含学生唯一确认校验
- `/api/offices`: 教研室 CRUD、绑定主任（管理员）
- `/api/teachers`: 教师 CRUD、批量绑定用户/教研室（管理员）
- `/api/students`: 学生 CRUD、批量绑定用户（管理员）
- `/api/logs`: 操作日志查询（管理员）
- `/api/stats/summary`: 简单汇总统计（管理员/主任）

## TODO（可按需扩展）
- 导入：用户/教师/学生/教研室 Excel/CSV
- 更细粒度的操作日志记录（在业务接口中调用 write_log）
- 更丰富的统计、分页/排序/过滤参数

