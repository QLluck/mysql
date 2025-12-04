# {{CODE-Cycle-Integration:
#   Task_ID: [#T003]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "实现学生管理API路由，包括查询、添加、修改、删除功能"
#   Principle_Applied: "RESTful API, Error Handling"
# }}
# {{START_MODIFICATIONS}}

from flask import Blueprint, request, jsonify
from database import db

bp = Blueprint('students', __name__)

@bp.route('', methods=['GET'])
def get_students():
    """查询所有学生信息"""
    try:
        # 获取查询参数
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 20))
        keyword = request.args.get('keyword', '')
        
        # 构建查询SQL
        sql = """
            SELECT s.*, p.pname as 专业名称, p.plocal as 办公地点
            FROM 学生 s
            LEFT JOIN 专业 p ON s.pID = p.pID
            WHERE 1=1
        """
        params = []
        
        if keyword:
            sql += " AND (s.sID LIKE %s OR s.sname LIKE %s)"
            params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        sql += " ORDER BY s.sID LIMIT %s OFFSET %s"
        params.extend([page_size, (page - 1) * page_size])
        
        students = db.execute_query(sql, params)
        
        # 获取总数
        count_sql = "SELECT COUNT(*) as total FROM 学生 WHERE 1=1"
        count_params = []
        if keyword:
            count_sql += " AND (sID LIKE %s OR sname LIKE %s)"
            count_params.extend([f'%{keyword}%', f'%{keyword}%'])
        
        total_result = db.execute_query(count_sql, count_params)
        total = total_result[0]['total'] if total_result else 0
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': {
                'list': students,
                'total': total,
                'page': page,
                'page_size': page_size
            }
        })
    except Exception as e:
        error_msg = str(e)
        # 如果是数据库连接错误，提供更友好的提示
        if 'Access denied' in error_msg or '1045' in error_msg:
            error_msg = '数据库连接失败：请检查backend/.env文件中的数据库密码配置。详见backend/DATABASE_SETUP.md'
        return jsonify({'code': 500, 'message': f'查询失败: {error_msg}'}), 500

@bp.route('/<student_id>', methods=['GET'])
def get_student(student_id):
    """查询单个学生信息"""
    try:
        sql = """
            SELECT s.*, p.pname as 专业名称, p.plocal as 办公地点
            FROM 学生 s
            LEFT JOIN 专业 p ON s.pID = p.pID
            WHERE s.sID = %s
        """
        student = db.execute_query(sql, (student_id,))
        
        if not student:
            return jsonify({'code': 404, 'message': '学生不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': student[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

@bp.route('', methods=['POST'])
def create_student():
    """添加学生信息"""
    try:
        data = request.json
        required_fields = ['sID', 'sname', 'ssex', 'cID', 'pID', 'birth']
        
        # 验证必填字段
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'缺少必填字段: {field}'}), 400
        
        sql = """
            INSERT INTO 学生 (sID, sname, ssex, cID, pID, birth, rID, TGRADE)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['sID'],
            data['sname'],
            data['ssex'],
            data['cID'],
            data['pID'],
            data['birth'],
            data.get('rID'),
            data.get('TGRADE')
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
def update_student(student_id):
    """修改学生信息"""
    try:
        data = request.json
        
        # 构建更新SQL
        update_fields = []
        params = []
        
        allowed_fields = ['sname', 'ssex', 'cID', 'pID', 'birth', 'rID', 'TGRADE']
        for field in allowed_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'code': 400, 'message': '没有要更新的字段'}), 400
        
        params.append(student_id)
        sql = f"UPDATE 学生 SET {', '.join(update_fields)} WHERE sID = %s"
        
        affected_rows = db.execute_update(sql, params)
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '学生不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@bp.route('/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """删除学生信息"""
    try:
        sql = "DELETE FROM 学生 WHERE sID = %s"
        affected_rows = db.execute_update(sql, (student_id,))
        
        if affected_rows == 0:
            return jsonify({'code': 404, 'message': '学生不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'删除失败: {str(e)}'}), 500

@bp.route('/<student_id>/grades', methods=['GET'])
def get_student_grades(student_id):
    """查询学生成绩信息"""
    try:
        sql = """
            SELECT s.sID, s.sname, g.dGrade, g.tGrade, g.rGrade, s.TGRADE
            FROM 学生 s
            LEFT JOIN 成绩 g ON s.sID = g.sID
            WHERE s.sID = %s
        """
        result = db.execute_query(sql, (student_id,))
        
        if not result:
            return jsonify({'code': 404, 'message': '学生不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '查询成功',
            'data': result[0]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': f'查询失败: {str(e)}'}), 500

# {{END_MODIFICATIONS}}

