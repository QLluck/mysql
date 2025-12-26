# -*- coding: utf-8 -*-
"""
选题模型
"""
from models.db import execute_query, execute_update

class Selection:
    """选题模型类"""
    
    @staticmethod
    def get_by_id(selection_id):
        """根据ID获取选题"""
        sql = """
            SELECT s.*, 
                   u.real_name as student_name, u.username as student_username,
                   t.title as topic_title, t.teacher_id
            FROM selections s
            JOIN users u ON s.student_id = u.id
            JOIN topics t ON s.topic_id = t.id
            WHERE s.id = %s
        """
        return execute_query(sql, (selection_id,), fetch_one=True)
    
    @staticmethod
    def get_by_student(student_id):
        """获取学生的选题"""
        sql = """
            SELECT s.*, 
                   t.title as topic_title, t.description as topic_description,
                   u.real_name as teacher_name
            FROM selections s
            JOIN topics t ON s.topic_id = t.id
            JOIN users u ON t.teacher_id = u.id
            WHERE s.student_id = %s
        """
        return execute_query(sql, (student_id,), fetch_one=True)
    
    @staticmethod
    def get_by_teacher(teacher_id):
        """获取教师课题的所有选题"""
        sql = """
            SELECT s.*, 
                   u.real_name as student_name, u.username as student_username,
                   t.title as topic_title
            FROM selections s
            JOIN users u ON s.student_id = u.id
            JOIN topics t ON s.topic_id = t.id
            WHERE t.teacher_id = %s
            ORDER BY s.apply_time DESC
        """
        return execute_query(sql, (teacher_id,))
    
    @staticmethod
    def get_by_topic(topic_id):
        """获取某课题的所有选题"""
        sql = """
            SELECT s.*, u.real_name as student_name, u.username as student_username
            FROM selections s
            JOIN users u ON s.student_id = u.id
            WHERE s.topic_id = %s
            ORDER BY s.apply_time DESC
        """
        return execute_query(sql, (topic_id,))
    
    @staticmethod
    def create(student_id, topic_id):
        """创建选题"""
        sql = "INSERT INTO selections (student_id, topic_id) VALUES (%s, %s)"
        return execute_update(sql, (student_id, topic_id))
    
    @staticmethod
    def update_status(selection_id, status):
        """更新选题状态"""
        sql = "UPDATE selections SET status = %s WHERE id = %s"
        return execute_update(sql, (status, selection_id))
    
    @staticmethod
    def delete(selection_id):
        """删除选题"""
        sql = "DELETE FROM selections WHERE id = %s"
        return execute_update(sql, (selection_id,))
    
    @staticmethod
    def check_student_selected(student_id):
        """检查学生是否已选题"""
        sql = "SELECT COUNT(*) as count FROM selections WHERE student_id = %s"
        result = execute_query(sql, (student_id,), fetch_one=True)
        return result['count'] > 0 if result else False
    
    @staticmethod
    def get_statistics():
        """获取选题统计"""
        sql = """
            SELECT 
                COUNT(DISTINCT s.student_id) as selected_count,
                COUNT(DISTINCT CASE WHEN s.status = 'approved' THEN s.student_id END) as approved_count,
                (SELECT COUNT(*) FROM users WHERE role = 'student') as total_students
            FROM selections s
        """
        return execute_query(sql, fetch_one=True)

