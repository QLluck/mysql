# -*- coding: utf-8 -*-
"""
课题模型
"""
from models.db import execute_query, execute_update

class Topic:
    """课题模型类"""
    
    @staticmethod
    def get_all(status=None):
        """
        获取所有课题
        
        Args:
            status: 状态筛选（pending/approved/rejected）
        """
        sql = """
            SELECT t.*, u.real_name as teacher_name, d.name as department_name
            FROM topics t
            JOIN users u ON t.teacher_id = u.id
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE 1=1
        """
        params = []
        
        if status:
            sql += " AND t.status = %s"
            params.append(status)
        
        sql += " ORDER BY t.created_at DESC"
        return execute_query(sql, params if params else None)
    
    @staticmethod
    def get_by_id(topic_id):
        """根据ID获取课题"""
        sql = """
            SELECT t.*, u.real_name as teacher_name, u.department_id,
                   d.name as department_name
            FROM topics t
            JOIN users u ON t.teacher_id = u.id
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE t.id = %s
        """
        return execute_query(sql, (topic_id,), fetch_one=True)
    
    @staticmethod
    def get_by_teacher(teacher_id):
        """获取教师的所有课题"""
        sql = """
            SELECT t.*, u.real_name as teacher_name
            FROM topics t
            JOIN users u ON t.teacher_id = u.id
            WHERE t.teacher_id = %s
            ORDER BY t.created_at DESC
        """
        return execute_query(sql, (teacher_id,))
    
    @staticmethod
    def create(title, description, teacher_id, max_students=1):
        """创建课题"""
        sql = """
            INSERT INTO topics (title, description, teacher_id, max_students)
            VALUES (%s, %s, %s, %s)
        """
        return execute_update(sql, (title, description, teacher_id, max_students))
    
    @staticmethod
    def update(topic_id, title, description, max_students):
        """更新课题"""
        sql = """
            UPDATE topics 
            SET title = %s, description = %s, max_students = %s
            WHERE id = %s
        """
        return execute_update(sql, (title, description, max_students, topic_id))
    
    @staticmethod
    def update_status(topic_id, status):
        """更新课题状态"""
        sql = "UPDATE topics SET status = %s WHERE id = %s"
        return execute_update(sql, (status, topic_id))
    
    @staticmethod
    def delete(topic_id):
        """删除课题"""
        sql = "DELETE FROM topics WHERE id = %s"
        return execute_update(sql, (topic_id,))
    
    @staticmethod
    def get_selection_count(topic_id):
        """获取课题已确认的选题数量"""
        sql = """
            SELECT COUNT(*) as count 
            FROM selections 
            WHERE topic_id = %s AND status = 'approved'
        """
        result = execute_query(sql, (topic_id,), fetch_one=True)
        return result['count'] if result else 0

