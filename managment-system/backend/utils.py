# {{CODE-Cycle-Integration:
#   Task_ID: [#T001]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "创建工具函数模块，提取公共功能"
#   Principle_Applied: "DRY, Code Reuse"
# }}
# {{START_MODIFICATIONS}}

from flask import jsonify

def success_response(data=None, message='操作成功'):
    """成功响应"""
    response = {
        'code': 200,
        'message': message
    }
    if data is not None:
        response['data'] = data
    return jsonify(response)

def error_response(message='操作失败', code=500, error=None):
    """错误响应"""
    response = {
        'code': code,
        'message': message
    }
    if error:
        response['error'] = str(error)
    return jsonify(response), code

def paginate_query(query_func, page=1, page_size=20, keyword='', keyword_fields=None):
    """分页查询辅助函数"""
    try:
        page = int(page)
        page_size = int(page_size)
        
        # 构建查询条件
        conditions = []
        params = []
        
        if keyword and keyword_fields:
            keyword_conditions = []
            for field in keyword_fields:
                keyword_conditions.append(f"{field} LIKE %s")
                params.append(f'%{keyword}%')
            if keyword_conditions:
                conditions.append(f"({' OR '.join(keyword_conditions)})")
        
        # 执行查询
        result = query_func(conditions, params, page, page_size)
        
        return success_response({
            'list': result.get('list', []),
            'total': result.get('total', 0),
            'page': page,
            'page_size': page_size
        }, '查询成功')
    except Exception as e:
        return error_response(f'查询失败: {str(e)}', 500, e)

# {{END_MODIFICATIONS}}

