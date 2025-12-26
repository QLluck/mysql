# -*- coding: utf-8 -*-
"""
Flask主应用入口
"""
from flask import Flask, send_from_directory
from config import Config
import os

# 创建Flask应用
app = Flask(__name__)
app.config.from_object(Config)

# 确保flask_session目录存在
if not os.path.exists('flask_session'):
    os.makedirs('flask_session')

# 注册蓝图
from routes.auth import auth_bp
from routes.topic import topic_bp
from routes.selection import selection_bp
from routes.statistics import statistics_bp

app.register_blueprint(auth_bp)
app.register_blueprint(topic_bp)
app.register_blueprint(selection_bp)
app.register_blueprint(statistics_bp)

# 静态文件路由
@app.route('/')
def index():
    return send_from_directory('templates', 'login.html')

@app.route('/<path:path>')
def serve_static(path):
    if path.endswith('.html'):
        return send_from_directory('templates', path)
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

