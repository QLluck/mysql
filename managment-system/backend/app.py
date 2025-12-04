# {{CODE-Cycle-Integration:
#   Task_ID: [#T001]
#   Timestamp: 2025-12-05
#   Phase: D-Develop
#   Context-Analysis: "创建Flask主应用文件，配置路由和CORS"
#   Principle_Applied: "KISS, DRY, Separation of Concerns"
# }}
# {{START_MODIFICATIONS}}

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes import student_routes, teacher_routes, paper_routes, grade_routes, major_routes, admin_routes

app = Flask(__name__)
app.config.from_object(Config)

# 配置CORS - 允许所有来源（开发环境）
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 注册路由蓝图
app.register_blueprint(student_routes.bp, url_prefix='/api/students')
app.register_blueprint(teacher_routes.bp, url_prefix='/api/teachers')
app.register_blueprint(paper_routes.bp, url_prefix='/api/papers')
app.register_blueprint(grade_routes.bp, url_prefix='/api/grades')
app.register_blueprint(major_routes.bp, url_prefix='/api/majors')
app.register_blueprint(admin_routes.bp, url_prefix='/api/admins')

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({
        'status': 'ok',
        'message': '毕业设计选题管理系统API运行正常'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '接口不存在'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': '服务器内部错误'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG)

# {{END_MODIFICATIONS}}

