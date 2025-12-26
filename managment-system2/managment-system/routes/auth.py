# -*- coding: utf-8 -*-
"""
认证路由模块
"""
from flask import Blueprint, request, jsonify, session
from functools import wraps
from models.user import User

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    """登录验证装饰器"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': '请先登录'}), 401
        return f(*args, **kwargs)
    return decorated_function

def require_role(*roles):
    """角色验证装饰器"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'success': False, 'message': '请先登录'}), 401
            
            user_role = session.get('role')
            if user_role not in roles:
                return jsonify({'success': False, 'message': '权限不足'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@auth_bp.route('/api/login', methods=['POST'])
def login():
    """用户登录"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': '用户名和密码不能为空'})
    
    # 验证用户
    user = User.verify_password(username, password)
    if not user:
        return jsonify({'success': False, 'message': '用户名或密码错误'})
    
    # 保存登录状态
    session['user_id'] = user['id']
    session['username'] = user['username']
    session['real_name'] = user['real_name']
    session['role'] = user['role']
    session['department_id'] = user['department_id']
    
    return jsonify({
        'success': True,
        'message': '登录成功',
        'data': {
            'id': user['id'],
            'username': user['username'],
            'real_name': user['real_name'],
            'role': user['role'],
            'department_id': user['department_id'],
            'department_name': user.get('department_name')
        }
    })

@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    """退出登录"""
    session.clear()
    return jsonify({'success': True, 'message': '退出成功'})

@auth_bp.route('/api/current_user', methods=['GET'])
@login_required
def get_current_user():
    """获取当前登录用户信息"""
    user_id = session.get('user_id')
    user = User.get_by_id(user_id)
    
    if not user:
        session.clear()
        return jsonify({'success': False, 'message': '用户不存在'}), 404
    
    return jsonify({
        'success': True,
        'data': {
            'id': user['id'],
            'username': user['username'],
            'real_name': user['real_name'],
            'role': user['role'],
            'department_id': user['department_id'],
            'department_name': user.get('department_name')
        }
    })

