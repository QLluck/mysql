# -*- coding: utf-8 -*-
"""
统计路由模块
"""
from flask import Blueprint, jsonify
from routes.auth import login_required, require_role
from models.db import execute_query
from models.selection import Selection

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/api/statistics/topics', methods=['GET'])
@require_role('admin')
def get_topic_statistics():
    """课题统计"""
    # 总体统计
    sql_summary = """
        SELECT 
            COUNT(*) as total,
            COUNT(CASE WHEN status = 'pending' THEN 1 END) as pending,
            COUNT(CASE WHEN status = 'approved' THEN 1 END) as approved,
            COUNT(CASE WHEN status = 'rejected' THEN 1 END) as rejected
        FROM topics
    """
    summary = execute_query(sql_summary, fetch_one=True)
    
    # 按教师统计
    sql_by_teacher = """
        SELECT 
            u.id,
            u.real_name as teacher_name,
            d.name as department_name,
            COUNT(t.id) as topic_count,
            COUNT(CASE WHEN t.status = 'approved' THEN 1 END) as approved_count,
            COUNT(CASE WHEN t.status = 'pending' THEN 1 END) as pending_count,
            COUNT(CASE WHEN t.status = 'rejected' THEN 1 END) as rejected_count
        FROM users u
        LEFT JOIN topics t ON u.id = t.teacher_id
        LEFT JOIN departments d ON u.department_id = d.id
        WHERE u.role = 'teacher'
        GROUP BY u.id
        ORDER BY topic_count DESC
    """
    by_teacher = execute_query(sql_by_teacher)
    
    return jsonify({
        'success': True,
        'data': {
            'summary': summary,
            'by_teacher': by_teacher
        }
    })

@statistics_bp.route('/api/statistics/selections', methods=['GET'])
@require_role('admin')
def get_selection_statistics():
    """选题统计"""
    # 总体统计
    stats = Selection.get_statistics()
    
    # 按课题统计
    sql_by_topic = """
        SELECT 
            t.id,
            t.title as topic_title,
            u.real_name as teacher_name,
            t.max_students,
            COUNT(s.id) as total_selections,
            COUNT(CASE WHEN s.status = 'approved' THEN 1 END) as approved_count,
            COUNT(CASE WHEN s.status = 'pending' THEN 1 END) as pending_count
        FROM topics t
        LEFT JOIN selections s ON t.id = s.topic_id
        LEFT JOIN users u ON t.teacher_id = u.id
        WHERE t.status = 'approved'
        GROUP BY t.id
        ORDER BY total_selections DESC
    """
    by_topic = execute_query(sql_by_topic)
    
    # 未选题学生列表
    sql_unselected = """
        SELECT u.id, u.username, u.real_name
        FROM users u
        LEFT JOIN selections s ON u.id = s.student_id
        WHERE u.role = 'student' AND s.id IS NULL
        ORDER BY u.id
    """
    unselected_students = execute_query(sql_unselected)
    
    return jsonify({
        'success': True,
        'data': {
            'summary': stats,
            'by_topic': by_topic,
            'unselected_students': unselected_students
        }
    })

