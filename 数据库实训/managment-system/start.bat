@echo off
chcp 65001 >nul
title 毕业设计选题管理系统 - 启动

cd /d %~dp0

echo.
echo ========================================
echo   毕业设计选题管理系统
echo ========================================
echo.

:: 检查环境
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python
    pause
    exit /b 1
)

node --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Node.js
    pause
    exit /b 1
)

:: 检查并创建配置文件
cd backend
if not exist .env (
    echo [创建] 配置文件 .env
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
cd ..

:: 启动后端服务（使用start保持窗口打开）
echo [启动] 后端服务 (http://localhost:5000)
start "后端服务-Flask" cmd /k "cd /d %~dp0backend && python app.py"

:: 等待后端启动
echo     等待后端服务启动...
timeout /t 5 /nobreak >nul

:: 启动前端服务（使用start保持窗口打开）
echo [启动] 前端服务 (http://localhost:3000)
start "前端服务-React" cmd /k "cd /d %~dp0frontend && npm start"

echo.
echo ========================================
echo   启动完成
echo ========================================
echo.
echo 服务窗口已打开，请保持窗口打开状态
echo.
echo 后端服务: http://localhost:5000
echo 前端服务: http://localhost:3000
echo.
echo 等待前端服务启动（约20秒）...
timeout /t 20 /nobreak >nul

:: 打开浏览器
start http://localhost:3000

echo.
echo 浏览器已打开
echo.
echo [重要提示]
echo   - 服务窗口必须保持打开，关闭窗口会停止服务
echo   - 如果服务窗口自动关闭，请查看窗口中的错误信息
echo   - 可以最小化窗口，但不要关闭
echo.
pause

