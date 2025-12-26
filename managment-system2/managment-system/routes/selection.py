# -*- coding: utf-8 -*-
"""
选题路由模块
"""
from flask import Blueprint, request, jsonify, session
from routes.auth import login_required, require_role
from models.selection import Selection
from models.topic import Topic

selection_bp = Blueprint('selection', __name__)

@selection_bp.route('/api/selections/my', methods=['GET'])
@require_role('student')
def get_my_selection():
    """学生查看自己的选题"""
    student_id = session.get('user_id')
    selection = Selection.get_by_student(student_id)
    
    return jsonify({
        'success': True,
        'data': selection
    })

@selection_bp.route('/api/selections/teacher', methods=['GET'])
@require_role('teacher')
def get_teacher_selections():
    """教师查看预选自己的学生"""
    teacher_id = session.get('user_id')
    selections = Selection.get_by_teacher(teacher_id)
    
    return jsonify({
        'success': True,
        'data': selections
    })

@selection_bp.route('/api/selections', methods=['POST'])
@require_role('student')
def create_selection():
    """学生提交选题申请"""
    student_id = session.get('user_id')
    
    # 检查是否已经选过题
    if Selection.check_student_selected(student_id):
        return jsonify({'success': False, 'message': '您已经选择过课题，不能重复选择'})
    
    # 获取课题ID
    data = request.get_json()
    topic_id = data.get('topic_id')
    
    if not topic_id:
        return jsonify({'success': False, 'message': '请选择课题'})
    
    # 检查课题是否存在
    topic = Topic.get_by_id(topic_id)
    if not topic:
        return jsonify({'success': False, 'message': '课题不存在'}), 404
    
    # 检查课题是否已通过审核
    if topic['status'] != 'approved':
        return jsonify({'success': False, 'message': '只能选择已通过审核的课题'})
    
    # 检查课题是否已满
    selected_count = Topic.get_selection_count(topic_id)
    if selected_count >= topic['max_students']:
        return jsonify({'success': False, 'message': '该课题选择人数已满'})
    
    # 创建选题
    try:
        selection_id = Selection.create(student_id, topic_id)
        return jsonify({
            'success': True,
            'message': '选题成功，等待教师确认',
            'data': {'id': selection_id}
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'选题失败：{str(e)}'})

@selection_bp.route('/api/selections/student/<int:selection_id>', methods=['DELETE'])
@require_role('student')
def cancel_selection(selection_id):
    """学生取消选题"""
    # 检查选题是否存在
    selection = Selection.get_by_id(selection_id)
    if not selection:
        return jsonify({'success': False, 'message': '选题不存在'}), 404
    
    # 检查是否是自己的选题
    student_id = session.get('user_id')
    if selection['student_id'] != student_id:
        return jsonify({'success': False, 'message': '无权取消此选题'}), 403
    
    # 如果已被教师确认，不允许取消
    if selection['status'] == 'approved':
        return jsonify({'success': False, 'message': '已被教师确认的选题不可取消'})
    
    # 删除选题
    try:
        Selection.delete(selection_id)
        return jsonify({'success': True, 'message': '取消选题成功'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'取消失败：{str(e)}'})

@selection_bp.route('/api/selections/<int:selection_id>/confirm', methods=['PUT'])
@require_role('teacher')
def confirm_selection(selection_id):
    """教师确认学生选题"""
    # 检查选题是否存在
    selection = Selection.get_by_id(selection_id)
    if not selection:
        return jsonify({'success': False, 'message': '选题不存在'}), 404
    
    # 检查是否是自己课题的选题
    teacher_id = session.get('user_id')
    if selection['teacher_id'] != teacher_id:
        return jsonify({'success': False, 'message': '无权确认此选题'}), 403
    
    # 获取操作类型
    data = request.get_json()
    action = data.get('action')  # 'approve' 或 'reject'
    
    if action not in ['approve', 'reject']:
        return jsonify({'success': False, 'message': '无效的操作'})
    
    # 更新选题状态
    status = 'approved' if action == 'approve' else 'rejected'
    try:
        Selection.update_status(selection_id, status)
        message = '已确认该学生选题' if action == 'approve' else '已拒绝该学生选题'
        return jsonify({'success': True, 'message': message})
    except Exception as e:
        return jsonify({'success': False, 'message': f'操作失败：{str(e)}'})

@selection_bp.route('/api/selections/teacher/<int:selection_id>', methods=['DELETE'])
@require_role('teacher')
def remove_selection(selection_id):
    """教师剔除学生"""
    # 检查选题是否存在
    selection = Selection.get_by_id(selection_id)
    if not selection:
        return jsonify({'success': False, 'message': '选题不存在'}), 404
    
    # 检查是否是自己课题的选题
    teacher_id = session.get('user_id')
    if selection['teacher_id'] != teacher_id:
        return jsonify({'success': False, 'message': '无权剔除此学生'}), 403
    
    # 删除选题
    try:
        Selection.delete(selection_id)
        return jsonify({'success': True, 'message': '已剔除该学生'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'剔除失败：{str(e)}'})

