-- 测试数据脚本

USE graduation_topic_system;

-- 插入教研室数据
INSERT INTO departments (id, name) VALUES
(1, '计算机科学与技术教研室'),
(2, '软件工程教研室'),
(3, '网络工程教研室');

-- 插入用户数据 (密码都是MD5加密后的值)
-- admin123 的MD5: 0192023a7bbd73250516f069df18b500
-- 123456 的MD5: e10adc3949ba59abbe56e057f20f883e

-- 教研室主任
INSERT INTO users (id, username, password, real_name, role, department_id) VALUES
(1, 'admin', '0192023a7bbd73250516f069df18b500', '张主任', 'admin', 1);

-- 教师
INSERT INTO users (id, username, password, real_name, role, department_id) VALUES
(2, 'teacher1', 'e10adc3949ba59abbe56e057f20f883e', '李老师', 'teacher', 1),
(3, 'teacher2', 'e10adc3949ba59abbe56e057f20f883e', '王老师', 'teacher', 1),
(4, 'teacher3', 'e10adc3949ba59abbe56e057f20f883e', '赵老师', 'teacher', 2);

-- 学生
INSERT INTO users (id, username, password, real_name, role, department_id) VALUES
(5, 'student1', 'e10adc3949ba59abbe56e057f20f883e', '张三', 'student', NULL),
(6, 'student2', 'e10adc3949ba59abbe56e057f20f883e', '李四', 'student', NULL),
(7, 'student3', 'e10adc3949ba59abbe56e057f20f883e', '王五', 'student', NULL),
(8, 'student4', 'e10adc3949ba59abbe56e057f20f883e', '赵六', 'student', NULL),
(9, 'student5', 'e10adc3949ba59abbe56e057f20f883e', '孙七', 'student', NULL);

-- 插入课题数据
INSERT INTO topics (id, title, description, teacher_id, status, max_students) VALUES
(1, '基于Python的数据分析系统', '开发一个数据分析系统，能够对大规模数据进行清洗、分析和可视化', 2, 'approved', 1),
(2, '智能图书管理系统设计与实现', '采用B/S架构，实现图书借阅、归还、查询等功能', 2, 'pending', 1),
(3, '在线考试系统的设计与实现', '支持多种题型、自动组卷、自动评分等功能', 3, 'approved', 2),
(4, '基于深度学习的图像识别系统', '使用卷积神经网络实现图像分类和目标检测', 3, 'pending', 1),
(5, '电商网站的设计与开发', '实现商品展示、购物车、订单管理等核心功能', 4, 'approved', 1);

-- 插入选题数据
INSERT INTO selections (id, student_id, topic_id, status) VALUES
(1, 5, 1, 'approved'),  -- 张三选择了课题1，已确认
(2, 6, 3, 'pending'),   -- 李四选择了课题3，待确认
(3, 7, 5, 'approved');  -- 王五选择了课题5，已确认

