-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS graduation_project DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 切换到该数据库
USE graduation_project;

-- 1. 权限表
CREATE TABLE 权限 (
    权限ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '权限唯一标识',
    权限名称 VARCHAR(50) NOT NULL UNIQUE COMMENT '权限名称（如：提交课题、审核课题）'
) COMMENT '系统所有权限基础信息表';

-- 2. 角色表
CREATE TABLE 角色 (
    角色ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '角色唯一标识',
    角色名称 VARCHAR(30) NOT NULL UNIQUE COMMENT '角色名称（系统管理员/教研室主任/普通教师/学生）'
) COMMENT '系统角色定义表';

-- 3. 角色_权限关联表
CREATE TABLE 角色_权限 (
    角色ID INT NOT NULL COMMENT '关联角色表ID',
    权限ID INT NOT NULL COMMENT '关联权限表ID',
    PRIMARY KEY (角色ID, 权限ID),
    FOREIGN KEY (角色ID) REFERENCES 角色(角色ID) ON DELETE CASCADE,
    FOREIGN KEY (权限ID) REFERENCES 权限(权限ID) ON DELETE CASCADE
) COMMENT '角色与权限的多对多关联表';

-- 4. 用户表
CREATE TABLE 用户 (
    用户ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户唯一标识',
    用户名 VARCHAR(30) NOT NULL UNIQUE COMMENT '登录账号',
    密码 VARCHAR(100) NOT NULL COMMENT '登录密码（加密存储）'
) COMMENT '系统登录用户账号表';

-- 5. 用户_角色关联表
CREATE TABLE 用户_角色 (
    用户ID INT NOT NULL COMMENT '关联用户表ID',
    角色ID INT NOT NULL COMMENT '关联角色表ID',
    PRIMARY KEY (用户ID, 角色ID),
    FOREIGN KEY (用户ID) REFERENCES 用户(用户ID) ON DELETE CASCADE,
    FOREIGN KEY (角色ID) REFERENCES 角色(角色ID) ON DELETE CASCADE
) COMMENT '用户与角色的多对多关联表';

-- 6. 教研室表
CREATE TABLE 教研室 (
    教研室ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '教研室唯一标识',
    教研室名称 VARCHAR(50) NOT NULL UNIQUE COMMENT '教研室名称',
    用户ID INT COMMENT '关联教研室主任的用户ID（可为空）',
    FOREIGN KEY (用户ID) REFERENCES 用户(用户ID) ON DELETE SET NULL
) COMMENT '院校教研室信息表';

-- 7. 教师表
CREATE TABLE 教师 (
    教师ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '教师唯一标识',
    教师姓名 VARCHAR(30) NOT NULL COMMENT '教师姓名',
    用户ID INT COMMENT '关联登录用户ID（可为空）',
    教研室ID INT COMMENT '关联所属教研室ID（可为空）',
    FOREIGN KEY (用户ID) REFERENCES 用户(用户ID) ON DELETE SET NULL,
    FOREIGN KEY (教研室ID) REFERENCES 教研室(教研室ID) ON DELETE SET NULL
) COMMENT '教师业务信息表';

-- 8. 学生表
CREATE TABLE 学生 (
    学生ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '学生唯一标识',
    学生姓名 VARCHAR(30) NOT NULL COMMENT '学生姓名',
    用户ID INT COMMENT '关联登录用户ID（可为空）',
    FOREIGN KEY (用户ID) REFERENCES 用户(用户ID) ON DELETE SET NULL
) COMMENT '学生业务信息表';

-- 9. 课题表
CREATE TABLE 课题 (
    课题ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '课题唯一标识',
    课题名称 VARCHAR(100) NOT NULL UNIQUE COMMENT '课题名称',
    课题描述 TEXT COMMENT '课题详细描述',
    审核状态 TINYINT NOT NULL DEFAULT 0 COMMENT '0=待审核 1=审核通过 2=审核驳回',
    教师ID INT COMMENT '关联提交教师ID（可为空）',
    FOREIGN KEY (教师ID) REFERENCES 教师(教师ID) ON DELETE SET NULL
) COMMENT '教师提交的课题信息表';

-- 10. 选题记录表
CREATE TABLE 选题记录 (
    选题ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '选题记录唯一标识',
    学生ID INT NOT NULL COMMENT '关联学生表ID',
    课题ID INT NOT NULL COMMENT '关联课题表ID',
    选题状态 TINYINT NOT NULL DEFAULT 0 COMMENT '0=待确认 1=已确认 2=已剔除',
    选题时间 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '预选课题时间',
    最新提交时间 DATETIME COMMENT '学生最新提交记录的时间',
    最新提交记录 TEXT COMMENT '学生最新提交的选题相关记录',
    成绩 DECIMAL(5,2) COMMENT '课题成绩（0-100分）',
    FOREIGN KEY (学生ID) REFERENCES 学生(学生ID) ON DELETE CASCADE,
    FOREIGN KEY (课题ID) REFERENCES 课题(课题ID) ON DELETE CASCADE
) COMMENT '学生选题全流程信息表';