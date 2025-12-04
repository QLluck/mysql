# 毕业设计选题管理系统

## 项目简介

毕业设计选题管理系统是一个基于Web的信息管理系统，用于管理学生毕业设计选题的全流程，包括学生信息管理、导师信息管理、论文选题管理、成绩管理等核心功能。

## 技术栈

- **后端**: Python Flask + MySQL
- **前端**: React + Ant Design
- **数据库**: MySQL 8.0

## 快速开始

### 1. 环境要求

- Python 3.8+
- Node.js 16+
- MySQL 8.0+

### 2. 数据库配置

#### 步骤1：配置数据库密码

创建 `backend/.env` 文件（如果不存在），内容如下：

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=你的MySQL密码
DB_NAME=stoic
SECRET_KEY=dev-secret-key-change-in-production
DEBUG=True
```

**重要**：将 `DB_PASSWORD=你的MySQL密码` 替换为实际的MySQL root密码。

#### 步骤2：初始化数据库

```bash
cd backend
pip install -r requirements.txt
python init_db.py
```

这会自动创建数据库、导入表结构和初始数据。

### 3. 启动系统

**Windows用户：**
```bash
start.bat
```

**Linux/Mac用户：**
```bash
chmod +x start.sh stop.sh
./start.sh
```

脚本会自动：
- 检查环境（Python、Node.js）
- 检查并创建配置文件
- 同时启动后端和前端服务
- 自动打开浏览器

### 4. 停止服务

**Windows用户：**
```bash
stop.bat
```

**Linux/Mac用户：**
```bash
./stop.sh
```

### 6. 访问系统

打开浏览器访问 http://localhost:3000

## 系统功能

### 学生管理
- 学生列表查询（支持分页和搜索）
- 学生详细信息查看
- 学生信息增删改查
- 学生成绩查询

### 导师管理
- 导师列表查询（支持分页和搜索）
- 导师详细信息查看
- 导师信息增删改查
- 导师论文列表查询

### 论文管理
- 论文列表查询（支持分页、搜索和导师筛选）
- 论文信息增删改查

### 成绩管理
- 成绩列表查询（支持分页和学生筛选）
- 成绩信息增删改查

### 专业管理
- 专业列表查询（支持搜索）
- 专业信息增删改查

### 管理员管理
- 管理员列表查询
- 管理员信息增删改查

### 仪表盘
- 系统统计信息展示
- 各模块数据汇总

## 项目结构

```
managment-system/
├── backend/          # Flask后端
│   ├── app.py       # 主应用文件
│   ├── config.py    # 配置文件
│   ├── database.py  # 数据库连接
│   ├── init_db.py   # 数据库初始化脚本
│   ├── routes/      # 路由模块
│   └── .env         # 环境变量配置（需自行创建）
├── frontend/         # React前端
│   ├── src/
│   │   ├── components/  # 组件
│   │   ├── pages/       # 页面
│   │   └── services/    # API服务
│   └── package.json
├── stoic.sql        # 数据库结构
└── stoic_data.sql   # 初始数据
```

## API接口

### 学生管理
- `GET /api/students` - 获取学生列表
- `GET /api/students/:id` - 获取学生详情
- `POST /api/students` - 添加学生
- `PUT /api/students/:id` - 更新学生信息
- `DELETE /api/students/:id` - 删除学生
- `GET /api/students/:id/grades` - 获取学生成绩

### 导师管理
- `GET /api/teachers` - 获取导师列表
- `GET /api/teachers/:id` - 获取导师详情
- `POST /api/teachers` - 添加导师
- `PUT /api/teachers/:id` - 更新导师信息
- `DELETE /api/teachers/:id` - 删除导师
- `GET /api/teachers/:id/papers` - 获取导师论文列表

### 论文管理
- `GET /api/papers` - 获取论文列表
- `POST /api/papers` - 添加论文
- `PUT /api/papers/:id` - 更新论文信息
- `DELETE /api/papers/:id` - 删除论文

### 成绩管理
- `GET /api/grades` - 获取成绩列表
- `POST /api/grades` - 添加成绩
- `PUT /api/grades/:id` - 更新成绩
- `DELETE /api/grades/:id` - 删除成绩

### 专业管理
- `GET /api/majors` - 获取专业列表
- `POST /api/majors` - 添加专业
- `PUT /api/majors/:id` - 更新专业信息
- `DELETE /api/majors/:id` - 删除专业

### 管理员管理
- `GET /api/admins` - 获取管理员列表
- `POST /api/admins` - 添加管理员
- `PUT /api/admins/:id` - 更新管理员信息
- `DELETE /api/admins/:id` - 删除管理员

## 常见问题

### 数据库连接失败

**错误**: `Access denied for user 'root'@'localhost'`

**解决方案**:
1. 检查 `backend/.env` 文件中的 `DB_PASSWORD` 是否正确
2. 确保MySQL服务正在运行
3. 验证数据库 `stoic` 是否存在：运行 `python init_db.py`

### 列表加载失败

**解决方案**:
1. 确认数据库已初始化：`cd backend && python init_db.py`
2. 检查后端服务是否运行：访问 http://localhost:5000/api/health
3. 确认 `.env` 文件配置正确
4. 重启后端服务

### 端口被占用

**解决方案**:
- 后端端口5000被占用：修改 `backend/app.py` 中的端口号
- 前端端口3000被占用：在 `frontend/package.json` 中添加 `PORT=3001`

## 开发团队

- 杨博文
- 王悦懿
- 王嘉浩
- 袁鑫晨

## 指导老师

杨超峰

## 完成日期

2025-12-05
