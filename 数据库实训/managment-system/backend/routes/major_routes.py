# {{CODE-Cycle-Integration:
#   Task_ID: [#T007]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现专业管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('majors', __name__)

@bp.route('', methods=['GET'])
def get_majors():
    """查询所有专业信息"""
    try:
        keyword = request.args.get('keyword', '')
        
        sql = "SELECT * FROM 专业 WHERE 1=1"
        params = []
        
        if keyword:
            sql += " AND (pID LIKE %s OR pname LIKE %s)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        sql += " ORDER BY pID"
        
        majors = db.execute_query(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': majors
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('/<major_id>', methods=['GET'])
def get_major(major_id):
    """查询单个专业信息"""
    try:
        sql = "SELECT * FROM 专业 WHERE pID = %s"
        major = db.execute_query(sql, (major_id,))
        
        if not major:
            return jsonify({'code': 404, 'message': '专业不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': major[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_major():
    """添加专业信息"""
    try:
        data = request.json
        required_fields = ['pID', 'pname']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 专业 (pID, pname, plocal)
            VALUES (%s, %s, %s)
        """
        params = (
            data['pID'],
            data['pname'],
            data.get('plocal')
        )
        
        db.execute_update(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '添加成功',
            'data': {'pID': data['pID']}
        }), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': f'添加失败: {str(e)}'}), 500

@bp.route('/<major_id>', methods=['PUT'])
def update_major(major_id):
    """修改专业信息"""
    try:
        data = request.json
        
        update_fields = []
        params = []
        
        allowed_fields = ['pname', 'plocal']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(major_id)
        sql = f"UPDATE 专业 SET {', '.join(update_fields)} WHERE pID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '专业不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<major_id>', methods=['DELETE'])
def delete_major(major_id):
    """删除专业信息"""
    try:
        sql = "DELETE FROM 专业 WHERE pID = %s"
        affected_rows = db.execute_update(sql, (major_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '专业不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

