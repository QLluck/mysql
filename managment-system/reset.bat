@echo off
chcp 65001 >nul
title 毕业设计选题管理系统 - 强力重置
color 0C

echo.
echo ========================================
echo   正在清理所有相关进程...
echo ========================================
echo.

echo 1. 停止 Python 进程 (后端)...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM python3.exe >nul 2>&1

echo 2. 停止 Node.js 进程 (前端)...
taskkill /F /IM node.exe >nul 2>&1

echo 3. 强制清理端口 3000 (前端)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":3000.*LISTENING"') do (
    echo     正在终止进程 PID: %%a
    taskkill /PID %%a /F >nul 2>&1
)

echo 4. 强制清理端口 5000 (后端)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5000.*LISTENING"') do (
    echo     正在终止进程 PID: %%a
    taskkill /PID %%a /F >nul 2>&1
)

echo.
echo ========================================
echo   清理完成！
echo ========================================
echo.
echo 所有旧进程已被强制关闭。
echo 端口 3000 和 5000 现在应该是空闲的。
echo.
echo 正在自动重新启动系统...
echo.

timeout /t 3 /nobreak >nul
start.bat

