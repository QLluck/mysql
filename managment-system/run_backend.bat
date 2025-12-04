@echo off
chcp 65001 >nul
title 后端服务 - Flask
color 0B

cd /d %~dp0backend

echo.
echo ========================================
echo   后端服务 (Flask)
echo ========================================
echo.

if not exist .env (
    echo [警告] .env 文件不存在，正在创建...
    (
        echo DB_HOST=localhost
        echo DB_PORT=3306
        echo DB_USER=root
        echo DB_PASSWORD=
        echo DB_NAME=stoic
        echo SECRET_KEY=dev-secret-key
        echo DEBUG=True
    ) > .env
)

echo 正在启动服务...
echo 访问地址: http://localhost:5000
echo.
echo [注意] 请保持此窗口打开！
echo.

python app.py

pause



