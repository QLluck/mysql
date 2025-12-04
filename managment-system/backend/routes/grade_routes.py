# {{CODE-Cycle-Integration:
#   Task_ID: [#T006]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现成绩管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('grades', __name__)

@bp.route('', methods=['GET'])
def get_grades():
    """查询所有成绩信息"""
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 20))
        student_id = request.args.get('student_id', '')
        
        sql = """
            SELECT g.*, s.sname as 学生姓名, s.TGRADE as 总评成绩
            FROM 成绩 g
            LEFT JOIN 学生 s ON g.sID = s.sID
            WHERE 1=1
        """
        params = []
        
        if student_id:
            sql += " AND g.sID = %s"
            params.append(student_id)
        
        sql += " ORDER BY g.sID LIMIT %s OFFSET %s"
        params.extend([page_size, (page - 1) * page_size])
        
        grades = db.execute_query(sql, params)
        
        count_sql = "SELECT COUNT(*) as total FROM 成绩 WHERE 1=1"
        count_params = []
        if student_id:
            count_sql += " AND sID = %s"
            count_params.append(student_id)
        
        total = db.execute_query(count_sql, count_params)[0]['total']
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': {
                'list': grades,
                'total': total,
                'page': page,
                'page_size': page_size
            }
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('/<student_id>', methods=['GET'])
def get_grade(student_id):
    """查询单个学生成绩信息"""
    try:
        sql = """
            SELECT g.*, s.sname as 学生姓名, s.TGRADE as 总评成绩
            FROM 成绩 g
            LEFT JOIN 学生 s ON g.sID = s.sID
            WHERE g.sID = %s
        """
        grade = db.execute_query(sql, (student_id,))
        
        if not grade:
            return jsonify({'code': 404, 'message': '成绩不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': grade[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_grade():
    """添加成绩信息"""
    try:
        data = request.json
        required_fields = ['sID']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 成绩 (sID, dGrade, tGrade, rGrade)
            VALUES (%s, %s, %s, %s)
        """
        params = (
            data['sID'],
            data.get('dGrade'),
            data.get('tGrade'),
            data.get('rGrade')
        )
        
        db.execute_update(sql, params)
        
        return jsonify({
            'code': 200,
            'message': '添加成功',
            'data': {'sID': data['sID']}
        }), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': f'添加失败: {str(e)}'}), 500

@bp.route('/<student_id>', methods=['PUT'])
def update_grade(student_id):
    """修改成绩信息"""
    try:
        data = request.json
        
        update_fields = []
        params = []
        
        allowed_fields = ['dGrade', 'tGrade', 'rGrade']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(student_id)
        sql = f"UPDATE 成绩 SET {', '.join(update_fields)} WHERE sID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '成绩不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<student_id>', methods=['DELETE'])
def delete_grade(student_id):
    """删除成绩信息"""
    try:
        sql = "DELETE FROM 成绩 WHERE sID = %s"
        affected_rows = db.execute_update(sql, (student_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '成绩不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

