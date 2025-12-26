-- 毕业设计选题管理系统数据库初始化脚本

-- 创建数据库
CREATE DATABASE IF NOT EXISTS graduation_topic_system DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE graduation_topic_system;

-- 删除已存在的表（按外键依赖顺序）
DROP TABLE IF EXISTS selections;
DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS departments;

-- 1. 教研室表
CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE COMMENT '教研室名称'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='教研室表';

-- 2. 用户表
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '登录名',
    password VARCHAR(64) NOT NULL COMMENT '密码(MD5)',
    real_name VARCHAR(50) NOT NULL COMMENT '真实姓名',
    role ENUM('student', 'teacher', 'admin') NOT NULL COMMENT '角色',
    department_id INT DEFAULT NULL COMMENT '所属教研室ID',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE SET NULL,
    INDEX idx_username (username),
    INDEX idx_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';

-- 3. 课题表
CREATE TABLE topics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL COMMENT '课题名称',
    description TEXT COMMENT '课题描述',
    teacher_id INT NOT NULL COMMENT '指导教师ID',
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending' COMMENT '状态',
    max_students INT DEFAULT 1 COMMENT '可选学生数',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '提交时间',
    FOREIGN KEY (teacher_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_teacher (teacher_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='课题表';

-- 4. 选题表
CREATE TABLE selections (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL UNIQUE COMMENT '学生ID',
    topic_id INT NOT NULL COMMENT '课题ID',
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending' COMMENT '状态',
    apply_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '申请时间',
    FOREIGN KEY (student_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE,
    INDEX idx_topic (topic_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='选题表';

