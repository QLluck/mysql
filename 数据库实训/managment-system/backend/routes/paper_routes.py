# {{CODE-Cycle-Integration:
#   Task_ID: [#T005]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现论文管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('papers', __name__)

@bp.route('', methods=['GET'])
def get_papers():
    """查询所有论文信息"""
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 20))
        keyword = request.args.get('keyword', '')
        teacher_id = request.args.get('teacher_id', '')
        
        sql = """
            SELECT p.*, t.tname as 导师姓名, t.ttitle as 职称
            FROM 论文 p
            LEFT JOIN 导师 t ON p.tID = t.tID
            WHERE 1=1
        """
        params = []
        
        if keyword:
            sql += " AND (p.rtitle LIKE %s OR p.rtype LIKE %s)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        if teacher_id:
            sql += " AND p.tID = %s"
            params.append(teacher_id)
        
        sql += " ORDER BY p.tID LIMIT %s OFFSET %s"
        params.extend([page_size, (page - 1) * page_size])
        
        papers = db.execute_query(sql, params)
        
        count_sql = "SELECT COUNT(*) as total FROM 论文 WHERE 1=1"
        count_params = []
        if keyword:
            count_sql += " AND (rtitle LIKE %s OR rtype LIKE %s)"
            count_params.extend([f'%{keyword}%', f'%{keyword}%'])
        if teacher_id:
            count_sql += " AND tID = %s"
            count_params.append(teacher_id)
        
        total = db.execute_query(count_sql, count_params)[0]['total']
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': {
                'list': papers,
                'total': total,
                'page': page,
                'page_size': page_size
            }
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('/<paper_id>', methods=['GET'])
def get_paper(paper_id):
    """查询单个论文信息"""
    try:
        sql = """
            SELECT p.*, t.tname as 导师姓名, t.ttitle as 职称
            FROM 论文 p
            LEFT JOIN 导师 t ON p.tID = t.tID
            WHERE p.tID = %s
        """
        paper = db.execute_query(sql, (paper_id,))
        
        if not paper:
            return jsonify({'code': 404, 'message': '论文不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': paper[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_paper():
    """添加论文信息"""
    try:
        data = request.json
        required_fields = ['tID', 'rtitle']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 论文 (tID, rID, rtitle, rtype)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            data['tID'],
            data.get('rID'),
            data['rtitle'],
            data.get('rtype')
        )
        
        db.execute_update(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '添加成功',
            'data': {'tID': data['tID']}
        }), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': f'添加失败: {str(e)}'}), 500

@bp.route('/<paper_id>', methods=['PUT'])
def update_paper(paper_id):
    """修改论文信息"""
    try:
        data = request.json
        
        update_fields = []
        params = []
        
        allowed_fields = ['rID', 'rtitle', 'rtype']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(paper_id)
        sql = f"UPDATE 论文 SET {', '.join(update_fields)} WHERE tID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '论文不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<paper_id>', methods=['DELETE'])
def delete_paper(paper_id):
    """删除论文信息"""
    try:
        sql = "DELETE FROM 论文 WHERE tID = %s"
        affected_rows = db.execute_update(sql, (paper_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '论文不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

