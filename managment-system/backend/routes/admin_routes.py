# {{CODE-Cycle-Integration:
#   Task_ID: [#T007]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现管理员管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('admins', __name__)

@bp.route('', methods=['GET'])
def get_admins():
    """查询所有管理员信息"""
    try:
        sql = """
            SELECT a.*, p.pname as 专业名称
            FROM 管理员 a
            LEFT JOIN 专业 p ON a.pID = p.pID
            ORDER BY a.aID
        """
        admins = db.execute_query(sql)
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': admins
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('/<admin_id>', methods=['GET'])
def get_admin(admin_id):
    """查询单个管理员信息"""
    try:
        sql = """
            SELECT a.*, p.pname as 专业名称
            FROM 管理员 a
            LEFT JOIN 专业 p ON a.pID = p.pID
            WHERE a.aID = %s
        """
        admin = db.execute_query(sql, (admin_id,))
        
        if not admin:
            return jsonify({'code': 404, 'message': '管理员不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': admin[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_admin():
    """添加管理员信息"""
    try:
        data = request.json
        required_fields = ['aID', 'aname']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 管理员 (aID, aname, asex, pID, telnumber)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            data['aID'],
            data['aname'],
            data.get('asex'),
            data.get('pID'),
            data.get('telnumber')
        )
        
        db.execute_update(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '添加成功',
            'data': {'aID': data['aID']}
        }), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': f'添加失败: {str(e)}'}), 500

@bp.route('/<admin_id>', methods=['PUT'])
def update_admin(admin_id):
    """修改管理员信息"""
    try:
        data = request.json
        
        update_fields = []
        params = []
        
        allowed_fields = ['aname', 'asex', 'pID', 'telnumber']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(admin_id)
        sql = f"UPDATE 管理员 SET {', '.join(update_fields)} WHERE aID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '管理员不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    """删除管理员信息"""
    try:
        sql = "DELETE FROM 管理员 WHERE aID = %s"
        affected_rows = db.execute_update(sql, (admin_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '管理员不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

