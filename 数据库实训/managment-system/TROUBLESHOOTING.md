# 故障排除指南

## 前端连接失败 ERR_EMPTY_RESPONSE

### 问题症状
- 浏览器显示 "Connection Failed"
- 错误代码: ERR_EMPTY_RESPONSE (-324)
- 无法访问 http://localhost:3000

### 解决方案

#### 方法1：重启前端服务（推荐）

1. **停止旧的前端服务**
   - 找到运行前端服务的终端窗口
   - 按 `Ctrl+C` 停止服务

2. **重新启动前端服务**
   ```bash
   cd frontend
   npm start
   ```

3. **等待启动完成**
   - 通常需要 10-30 秒
   - 看到 "Compiled successfully!" 表示启动成功
   - 浏览器会自动打开 http://localhost:3000

#### 方法2：使用统一启动脚本

```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

然后选择选项 2（启动前端服务）

#### 方法3：检查端口占用

如果端口3000被占用：

```bash
# Windows
netstat -ano | findstr ":3000"

# 找到进程ID后，结束进程
taskkill /PID <进程ID> /F
```

#### 方法4：清理并重新安装

```bash
cd frontend
rm -rf node_modules
rm package-lock.json
npm install
npm start
```

### 常见原因

1. **前端服务崩溃**
   - 解决方案：重启服务

2. **端口被占用**
   - 解决方案：结束占用端口的进程或更换端口

3. **依赖问题**
   - 解决方案：重新安装依赖

4. **编译错误**
   - 解决方案：检查终端错误信息，修复代码问题

### 验证服务状态

运行测试脚本：
```bash
python test_system.py
```

检查服务是否运行：
```bash
# Windows
netstat -ano | findstr ":3000"

# 应该看到 LISTENING 状态
```

### 如果问题仍然存在

1. 检查后端服务是否正常运行（端口5000）
2. 检查浏览器控制台错误信息（F12）
3. 查看前端服务终端输出的错误信息
4. 确认防火墙没有阻止端口3000

