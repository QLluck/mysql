# 毕业设计选题管理系统

一个简单易用的毕业设计选题管理系统，支持教师提交课题、教研室主任审核、学生选题以及教师筛选学生的完整流程。

## 技术栈

- **后端**: Python 3.8+ + Flask 2.x
- **数据库**: MySQL 8.0
- **前端**: HTML5 + Bootstrap 5 + jQuery 3.x

## 功能特性

### 三种用户角色

1. **教研室主任**
   - 审核本教研室教师提交的课题
   - 查看课题和选题统计报表

2. **教师**
   - 提交和编辑毕业设计课题
   - 查看预选自己课题的学生
   - 确认或拒绝学生选题
   - 剔除不合适的学生

3. **学生**
   - 浏览所有已通过审核的课题
   - 选择一个课题（每个学生只能选择一个）
   - 查看自己的选题状态

## 快速开始

### 1. 环境准备

确保已安装以下软件：
- Python 3.8 或更高版本
- MySQL 8.0 或更高版本
- pip (Python包管理器)

### 2. 安装依赖

```bash
# 克隆或下载项目后，进入项目目录
cd managment-system

# 安装Python依赖
pip install -r requirements.txt
```

**注意**: 如果之前安装过Flask-Session，请先卸载：
```bash
pip uninstall Flask-Session -y
```

### 3. 配置数据库

#### 3.1 创建数据库

**Linux/Mac (Bash):**

```bash
mysql -u root -p < database/init.sql
```

**Windows (PowerShell):**

```powershell
Get-Content database\init.sql | mysql -u root -p你的密码
```

或者登录MySQL后执行：

```bash
mysql -u root -p
source database/init.sql
```

#### 3.2 插入测试数据

**Linux/Mac (Bash):**

```bash
mysql -u root -p < database/test_data.sql
```

**Windows (PowerShell):**

```powershell
Get-Content database\test_data.sql -Encoding UTF8 | mysql -u root -p你的密码 --default-character-set=utf8mb4
```

#### 3.3 修改配置文件

编辑 `config.py` 文件，修改数据库连接信息：

```python
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'your-password'  # 修改为你的MySQL密码
DB_NAME = 'graduation_topic_system'
```

### 4. 启动应用

```bash
python app.py
```

启动成功后，在浏览器中访问：
```
http://localhost:5000
```

## 测试账号

系统预置了以下测试账号：

| 角色 | 用户名 | 密码 | 说明 |
|------|--------|------|------|
| 教研室主任 | admin | admin123 | 计算机科学与技术教研室主任 |
| 教师 | teacher1 | 123456 | 李老师 |
| 教师 | teacher2 | 123456 | 王老师 |
| 学生 | student1 | 123456 | 张三 |
| 学生 | student2 | 123456 | 李四 |

## 完整使用流程

### 1. 教师提交课题

1. 使用教师账号登录（如：teacher1 / 123456）
2. 点击"我的课题"菜单
3. 点击"添加课题"按钮
4. 填写课题名称、描述和可选学生数
5. 提交后，课题状态为"待审核"

### 2. 主任审核课题

1. 使用主任账号登录（admin / admin123）
2. 点击"课题审核"菜单
3. 在待审核列表中，点击"通过"或"驳回"按钮
4. 通过后的课题学生才能看到并选择

### 3. 学生选择课题

1. 使用学生账号登录（如：student2 / 123456）
2. 点击"浏览课题"菜单
3. 查看所有已通过审核的课题
4. 点击"选择此课题"按钮
5. 选题后状态为"待确认"

### 4. 教师确认学生

1. 教师登录后，点击"学生管理"菜单
2. 查看所有预选自己课题的学生
3. 可以选择"确认"或"拒绝"学生
4. 确认后，学生选题状态变为"已确认"
5. 也可以随时"剔除"学生，清空其选题

### 5. 查看统计报表

1. 主任登录后，点击"统计报表"菜单
2. 查看课题统计（总数、已通过、待审核、已驳回）
3. 查看选题统计（学生总数、已选题、未选题）
4. 查看未选题学生列表

## 项目结构

```
managment-system/
├── app.py                    # Flask主应用入口
├── config.py                 # 配置文件
├── requirements.txt          # Python依赖
├── README.md                 # 本文档
├── database/                 # 数据库脚本
│   ├── init.sql             # 数据库初始化（创建表）
│   └── test_data.sql        # 测试数据
├── models/                   # 数据模型层
│   ├── __init__.py
│   ├── db.py                # 数据库连接
│   ├── user.py              # 用户模型
│   ├── topic.py             # 课题模型
│   └── selection.py         # 选题模型
├── routes/                   # 路由层（API接口）
│   ├── __init__.py
│   ├── auth.py              # 认证接口
│   ├── topic.py             # 课题接口
│   ├── selection.py         # 选题接口
│   └── statistics.py        # 统计接口
├── static/                   # 静态资源
│   ├── css/
│   │   └── custom.css       # 自定义样式
│   └── js/
│       └── common.js        # 公共JavaScript
└── templates/                # HTML模板
    ├── login.html           # 登录页
    ├── index.html           # 首页
    ├── student/             # 学生端页面
    │   ├── topics.html
    │   └── my_selection.html
    ├── teacher/             # 教师端页面
    │   ├── topics.html
    │   └── students.html
    └── admin/               # 主任端页面
        ├── review.html
        └── statistics.html
```

## API接口说明

### 认证接口

- `POST /api/login` - 用户登录
- `POST /api/logout` - 退出登录
- `GET /api/current_user` - 获取当前用户信息

### 课题接口

- `GET /api/topics` - 获取课题列表（支持status参数筛选）
- `GET /api/topics/<id>` - 获取课题详情
- `GET /api/topics/my` - 获取教师自己的课题
- `POST /api/topics` - 教师提交课题
- `PUT /api/topics/<id>` - 教师编辑课题
- `DELETE /api/topics/<id>` - 教师删除课题
- `PUT /api/topics/<id>/review` - 主任审核课题

### 选题接口

- `GET /api/selections/my` - 学生查看自己的选题
- `GET /api/selections/teacher` - 教师查看预选自己的学生
- `POST /api/selections` - 学生提交选题申请
- `PUT /api/selections/<id>/confirm` - 教师确认学生
- `DELETE /api/selections/<id>` - 学生取消选题 / 教师剔除学生

### 统计接口

- `GET /api/statistics/topics` - 课题统计
- `GET /api/statistics/selections` - 选题统计

## 数据库设计

### 核心表结构

1. **departments** - 教研室表
   - id, name

2. **users** - 用户表
   - id, username, password, real_name, role, department_id

3. **topics** - 课题表
   - id, title, description, teacher_id, status, max_students, created_at

4. **selections** - 选题表
   - id, student_id, topic_id, status, apply_time

详见 `database/init.sql` 文件。

## 业务规则

1. **课题提交规则**
   - 教师可以提交多个课题
   - 新提交的课题状态为"待审核"
   - 已通过审核的课题不能编辑

2. **课题审核规则**
   - 主任只能审核本教研室教师的课题
   - 审核状态：通过/驳回

3. **选题规则**
   - 学生只能选择已通过审核的课题
   - 每个学生只能选择一个课题
   - 课题人数已满时不能再选择
   - 选题后状态为"待确认"

4. **教师确认规则**
   - 教师可以确认或拒绝学生选题
   - 教师可以随时剔除学生（清空其选题）

## 注意事项

1. **密码安全**: 系统使用MD5加密密码，生产环境建议使用更安全的加密方式（如bcrypt）

2. **Session配置**: 使用Flask内置的加密cookie存储Session（轻量级、无需额外存储）

3. **端口占用**: 默认使用5000端口，如被占用可在 `app.py` 中修改

4. **数据库编码**: 使用utf8mb4编码，支持emoji等特殊字符

## 常见问题

### 1. 启动失败

**问题**: `ModuleNotFoundError: No module named 'flask'`

**解决**: 确保已安装依赖
```bash
pip install -r requirements.txt
```

### 2. 数据库连接失败

**问题**: `Can't connect to MySQL server`

**解决**:
- 检查MySQL服务是否启动
- 检查 `config.py` 中的数据库配置是否正确
- 确保数据库用户有足够的权限

### 3. 无法登录

**问题**: 提示用户名或密码错误

**解决**:
- 确保已执行 `test_data.sql` 插入测试数据
- 检查数据库中users表是否有数据
- 使用测试账号登录（见上方"测试账号"部分）

### 4. 页面显示异常

**问题**: 页面样式错乱或脚本不执行

**解决**:
- 检查网络连接（需要访问CDN加载Bootstrap和jQuery）
- 如果内网环境，可下载Bootstrap和jQuery到本地

## 开发计划

- [ ] 添加邮件通知功能
- [ ] 支持Excel导出统计数据
- [ ] 增加超级管理员功能
- [ ] 支持课题附件上传
- [ ] 增加消息通知系统

## 许可证

本项目仅用于学习和教学目的。

## 联系方式

如有问题或建议，欢迎联系。
