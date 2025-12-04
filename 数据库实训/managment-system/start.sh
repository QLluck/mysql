#!/bin/bash

cd "$(dirname "$0")"

echo ""
echo "========================================"
echo "  毕业设计选题管理系统"
echo "========================================"
echo ""

# 检查环境
command -v python3 >/dev/null 2>&1 || { echo "[错误] 未检测到Python3"; exit 1; }
command -v node >/dev/null 2>&1 || { echo "[错误] 未检测到Node.js"; exit 1; }

# 检查配置
cd backend
[ ! -f .env ] && cat > .env << EOF
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=stoic
SECRET_KEY=dev-secret-key
DEBUG=True
EOF
cd ..

# 启动后端（后台运行，输出到日志）
echo "[启动] 后端服务..."
cd backend
nohup python3 app.py > ../backend.log 2>&1 &
BACKEND_PID=$!
cd ..
echo "    后端进程ID: $BACKEND_PID"

sleep 5

# 启动前端（后台运行，输出到日志）
echo "[启动] 前端服务..."
cd frontend
nohup npm start > ../frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
echo "    前端进程ID: $FRONTEND_PID"

# 保存进程ID
echo $BACKEND_PID > backend.pid
echo $FRONTEND_PID > frontend.pid

echo ""
echo "========================================"
echo "  启动完成"
echo "========================================"
echo ""
echo "后端服务: http://localhost:5000 (PID: $BACKEND_PID)"
echo "前端服务: http://localhost:3000 (PID: $FRONTEND_PID)"
echo ""
echo "日志文件: backend.log, frontend.log"
echo "进程ID: backend.pid, frontend.pid"
echo ""
echo "等待服务启动（约20秒）..."
sleep 20

# 打开浏览器
command -v xdg-open >/dev/null && xdg-open http://localhost:3000 || command -v open >/dev/null && open http://localhost:3000

echo ""
echo "[重要提示]"
echo "  - 服务在后台运行，日志保存在 backend.log 和 frontend.log"
echo "  - 停止服务: kill $BACKEND_PID $FRONTEND_PID 或运行 stop.sh"
echo ""
