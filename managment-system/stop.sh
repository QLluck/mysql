#!/bin/bash
echo "正在停止服务..."
[ -f backend.pid ] && kill $(cat backend.pid) 2>/dev/null && echo "停止后端服务" && rm backend.pid
[ -f frontend.pid ] && kill $(cat frontend.pid) 2>/dev/null && echo "停止前端服务" && rm frontend.pid
lsof -ti:5000 | xargs kill -9 2>/dev/null
lsof -ti:3000 | xargs kill -9 2>/dev/null
echo "服务已停止"
