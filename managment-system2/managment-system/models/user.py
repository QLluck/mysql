# -*- coding: utf-8 -*-
"""
用户模型
"""
import hashlib
from models.db import execute_query, execute_update

class User:
    """用户模型类"""
    
    @staticmethod
    def get_by_id(user_id):
        """根据ID获取用户"""
        sql = """
            SELECT u.*, d.name as department_name 
            FROM users u
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE u.id = %s
        """
        return execute_query(sql, (user_id,), fetch_one=True)
    
    @staticmethod
    def get_by_username(username):
        """根据用户名获取用户"""
        sql = """
            SELECT u.*, d.name as department_name 
            FROM users u
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE u.username = %s
        """
        return execute_query(sql, (username,), fetch_one=True)
    
    @staticmethod
    def verify_password(username, password):
        """
        验证用户名和密码
        
        Args:
            username: 用户名
            password: 密码（明文）
            
        Returns:
            用户信息（验证成功）或 None（验证失败）
        """
        password_md5 = hashlib.md5(password.encode()).hexdigest()
        sql = """
            SELECT u.*, d.name as department_name 
            FROM users u
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE u.username = %s AND u.password = %s
        """
        return execute_query(sql, (username, password_md5), fetch_one=True)
    
    @staticmethod
    def get_all_students():
        """获取所有学生"""
        sql = "SELECT * FROM users WHERE role = 'student' ORDER BY id"
        return execute_query(sql)
    
    @staticmethod
    def get_all_teachers():
        """获取所有教师"""
        sql = """
            SELECT u.*, d.name as department_name 
            FROM users u
            LEFT JOIN departments d ON u.department_id = d.id
            WHERE u.role = 'teacher'
            ORDER BY u.id
        """
        return execute_query(sql)

