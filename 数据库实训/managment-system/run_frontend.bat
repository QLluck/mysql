@echo off
chcp 65001 >nul
title 前端服务 - React
color 0E

cd /d %~dp0frontend

echo.
echo ========================================
echo   前端服务 (React)
echo ========================================
echo.

if not exist node_modules (
    echo [提示] 正在安装依赖...
    call npm install
)

echo 正在启动服务...
echo 访问地址: http://localhost:3000
echo.
echo [注意] 请保持此窗口打开！
echo.

:: 强制开发模式环境变量，防止某些环境下的自动退出
set CI=false
npm start

pause



