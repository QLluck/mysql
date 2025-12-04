# {{CODE-Cycle-Integration:
#   Task_ID: [#T004]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现导师管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('teachers', __name__)

@bp.route('', methods=['GET'])
def get_teachers():
    """查询所有导师信息"""
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 20))
        keyword = request.args.get('keyword', '')
        
        sql = """
            SELECT t.*, p.pname as 专业名称, p.plocal as 办公地点
            FROM 导师 t
            LEFT JOIN 专业 p ON t.pID = p.pID
            WHERE 1=1
        """
        params = []
        
        if keyword:
            sql += " AND (t.tID LIKE %s OR t.tname LIKE %s)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        sql += " ORDER BY t.tID LIMIT %s OFFSET %s"
        params.extend([page_size, (page - 1) * page_size])
        
        teachers = db.execute_query(sql, params)
        
        count_sql = "SELECT COUNT(*) as total FROM 导师 WHERE 1=1"
        count_params = []
        if keyword:
            count_sql += " AND (tID LIKE %s OR tname LIKE %s)"
            count_params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        total = db.execute_query(count_sql, count_params)[0]['total']
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': {
                'list': teachers,
                'total': total,
                'page': page,
                'page_size': page_size
            }
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('/<teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """查询单个导师信息"""
    try:
        sql = """
            SELECT t.*, p.pname as 专业名称, p.plocal as 办公地点
            FROM 导师 t
            LEFT JOIN 专业 p ON t.pID = p.pID
            WHERE t.tID = %s
        """
        teacher = db.execute_query(sql, (teacher_id,))
        
        if not teacher:
            return jsonify({'code': 404, 'message': '导师不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': teacher[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_teacher():
    """添加导师信息"""
    try:
        data = request.json
        required_fields = ['tID', 'tname', 'tsex', 'pID']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 导师 (tID, tname, tsex, pID, ttitle, telnumber)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            data['tID'],
            data['tname'],
            data['tsex'],
            data['pID'],
            data.get('ttitle'),
            data.get('telnumber')
        )
        
        db.execute_update(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '添加成功',
            'data': {'tID': data['tID']}
        }), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': f'添加失败: {str(e)}'}), 500

@bp.route('/<teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    """修改导师信息"""
    try:
        data = request.json
        
        update_fields = []
        params = []
        
        allowed_fields = ['tname', 'tsex', 'pID', 'ttitle', 'telnumber']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(teacher_id)
        sql = f"UPDATE 导师 SET {', '.join(update_fields)} WHERE tID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '导师不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    """删除导师信息"""
    try:
        sql = "DELETE FROM 导师 WHERE tID = %s"
        affected_rows = db.execute_update(sql, (teacher_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '导师不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

@bp.route('/<teacher_id>/papers', methods=['GET'])
def get_teacher_papers(teacher_id):
    """查询导师的论文信息"""
    try:
        sql = """
            SELECT p.*, t.tname as 导师姓名
            FROM 论文 p
            LEFT JOIN 导师 t ON p.tID = t.tID
            WHERE p.tID = %s
        """
        papers = db.execute_query(sql, (teacher_id,))
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': papers
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

