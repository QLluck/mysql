# -*- coding: utf-8 -*-
"""
课题路由模块
"""
from flask import Blueprint, request, jsonify, session
from routes.auth import login_required, require_role
from models.topic import Topic
from models.user import User

topic_bp = Blueprint('topic', __name__)

@topic_bp.route('/api/topics', methods=['GET'])
@login_required
def get_topics():
    """获取课题列表"""
    status = request.args.get('status')
    user_role = session.get('role')
    
    # 获取课题列表
    topics = Topic.get_all(status)
    
    # 如果是学生，只显示已通过审核的课题
    if user_role == 'student':
        topics = [t for t in topics if t['status'] == 'approved']
    
    # 添加选题数量信息
    for topic in topics:
        topic['selected_count'] = Topic.get_selection_count(topic['id'])
    
    return jsonify({
        'success': True,
        'data': topics
    })

@topic_bp.route('/api/topics/<int:topic_id>', methods=['GET'])
@login_required
def get_topic(topic_id):
    """获取课题详情"""
    topic = Topic.get_by_id(topic_id)
    
    if not topic:
        return jsonify({'success': False, 'message': '课题不存在'}), 404
    
    topic['selected_count'] = Topic.get_selection_count(topic_id)
    
    return jsonify({
        'success': True,
        'data': topic
    })

@topic_bp.route('/api/topics/my', methods=['GET'])
@require_role('teacher')
def get_my_topics():
    """获取教师自己的课题"""
    teacher_id = session.get('user_id')
    topics = Topic.get_by_teacher(teacher_id)
    
    # 添加选题数量信息
    for topic in topics:
        topic['selected_count'] = Topic.get_selection_count(topic['id'])
    
    return jsonify({
        'success': True,
        'data': topics
    })

@topic_bp.route('/api/topics', methods=['POST'])
@require_role('teacher')
def create_topic():
    """教师提交课题"""
    data = request.get_json()
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    max_students = data.get('max_students', 1)
    
    # 数据验证
    if not title:
        return jsonify({'success': False, 'message': '课题名称不能为空'})
    
    if not description:
        return jsonify({'success': False, 'message': '课题描述不能为空'})
    
    try:
        max_students = int(max_students)
        if max_students < 1:
            raise ValueError
    except:
        return jsonify({'success': False, 'message': '可选学生数必须是正整数'})
    
    # 创建课题
    teacher_id = session.get('user_id')
    try:
        topic_id = Topic.create(title, description, teacher_id, max_students)
        return jsonify({
            'success': True,
            'message': '课题提交成功，等待审核',
            'data': {'id': topic_id}
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'提交失败：{str(e)}'})

@topic_bp.route('/api/topics/<int:topic_id>', methods=['PUT'])
@require_role('teacher')
def update_topic(topic_id):
    """教师编辑课题"""
    # 检查课题是否存在且属于当前教师
    topic = Topic.get_by_id(topic_id)
    if not topic:
        return jsonify({'success': False, 'message': '课题不存在'}), 404
    
    teacher_id = session.get('user_id')
    if topic['teacher_id'] != teacher_id:
        return jsonify({'success': False, 'message': '无权编辑此课题'}), 403
    
    # 如果课题已通过审核，不允许编辑
    if topic['status'] == 'approved':
        return jsonify({'success': False, 'message': '已通过审核的课题不可编辑'})
    
    # 获取更新数据
    data = request.get_json()
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    max_students = data.get('max_students', 1)
    
    # 数据验证
    if not title:
        return jsonify({'success': False, 'message': '课题名称不能为空'})
    
    if not description:
        return jsonify({'success': False, 'message': '课题描述不能为空'})
    
    try:
        max_students = int(max_students)
        if max_students < 1:
            raise ValueError
    except:
        return jsonify({'success': False, 'message': '可选学生数必须是正整数'})
    
    # 更新课题
    try:
        Topic.update(topic_id, title, description, max_students)
        return jsonify({'success': True, 'message': '课题更新成功'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'更新失败：{str(e)}'})

@topic_bp.route('/api/topics/<int:topic_id>', methods=['DELETE'])
@require_role('teacher')
def delete_topic(topic_id):
    """教师删除课题"""
    # 检查课题是否存在且属于当前教师
    topic = Topic.get_by_id(topic_id)
    if not topic:
        return jsonify({'success': False, 'message': '课题不存在'}), 404
    
    teacher_id = session.get('user_id')
    if topic['teacher_id'] != teacher_id:
        return jsonify({'success': False, 'message': '无权删除此课题'}), 403
    
    # 如果已有学生选择，不允许删除
    selected_count = Topic.get_selection_count(topic_id)
    if selected_count > 0:
        return jsonify({'success': False, 'message': '已有学生选择此课题，不可删除'})
    
    # 删除课题
    try:
        Topic.delete(topic_id)
        return jsonify({'success': True, 'message': '课题删除成功'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'删除失败：{str(e)}'})

@topic_bp.route('/api/topics/<int:topic_id>/review', methods=['PUT'])
@require_role('admin')
def review_topic(topic_id):
    """教研室主任审核课题"""
    # 检查课题是否存在
    topic = Topic.get_by_id(topic_id)
    if not topic:
        return jsonify({'success': False, 'message': '课题不存在'}), 404
    
    # 检查是否为本教研室的课题
    admin_department_id = session.get('department_id')
    if topic['department_id'] != admin_department_id:
        return jsonify({'success': False, 'message': '只能审核本教研室的课题'}), 403
    
    # 获取审核结果
    data = request.get_json()
    action = data.get('action')  # 'approve' 或 'reject'
    
    if action not in ['approve', 'reject']:
        return jsonify({'success': False, 'message': '无效的审核操作'})
    
    # 更新课题状态
    status = 'approved' if action == 'approve' else 'rejected'
    try:
        Topic.update_status(topic_id, status)
        message = '课题已通过审核' if action == 'approve' else '课题已驳回'
        return jsonify({'success': True, 'message': message})
    except Exception as e:
        return jsonify({'success': False, 'message': f'审核失败：{str(e)}'})

