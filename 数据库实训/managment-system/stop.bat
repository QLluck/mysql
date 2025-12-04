@echo off
echo 正在停止服务...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5000.*LISTENING"') do (
    echo 停止后端服务 (PID: %%a)
    taskkill /PID %%a /F >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":3000.*LISTENING"') do (
    echo 停止前端服务 (PID: %%a)
    taskkill /PID %%a /F >nul 2>&1
)
taskkill /F /IM node.exe >nul 2>&1
echo 服务已停止
pause
