# 前端（React + Ant Design）骨架说明
# 步骤1：进入前端项目根目录（替换为你的前端文件夹名，比如frontend）
cd frontend

# 步骤2：安装依赖（仅第一次需要，后续启动无需重复执行）
npm install

# 步骤3：启动前端开发服务（核心运行指令）
npm run dev
> 采用 Vite + React + TypeScript + Ant Design，基于 JWT 进行权限适配。

## 目录建议
```
frontend/
  src/
    api/axios.ts          # axios 实例，拦截器自动挂载 JWT
    auth/useAuth.tsx      # 登录状态、用户信息、权限列表
    auth/Protected.tsx    # 路由守卫
    hooks/usePerms.ts     # 权限判定封装
    components/PermButton.tsx  # 按权限控制按钮显示/禁用
    layout/               # 菜单、面包屑、顶栏
    pages/
      Login/
      Dashboard/
      Users/
      RolesPerms/
      Offices/
      Teachers/
      Students/
      Topics/
      Selections/
```

## 关键实现点
- 登录后调用 `/api/auth/me` 获取 `roles` 与 `perms`，存入全局 store（如 Zustand/Redux）。
- 菜单按角色动态过滤；按钮通过 `PermButton` 传入权限码数组自动隐藏/禁用。
- 表单校验：非空、唯一性（前端初查 + 后端最终）、成绩 0-100、时间格式。
- 课题页面：教师可提交/编辑/删除 `审核状态=0` 的自己课题；主任仅能审核本教研室课题；管理员全字段。
- 选题页面：学生预选/更新提交/取消待确认；教师确认/剔除自己课题的选题并填成绩；管理员全权。

## 快速脚手架命令
```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install antd axios react-router-dom @tanstack/react-query zustand
npm run dev
```

在 `src/api/axios.ts` 中设置基地址：
```ts
const instance = axios.create({ baseURL: 'http://localhost:5000' });
instance.interceptors.request.use(cfg => {
  const token = localStorage.getItem('token');
  if (token) cfg.headers.Authorization = `Bearer ${token}`;
  return cfg;
});
export default instance;
```

`PermButton` 示例：
```tsx
import React from 'react';
import { Button } from 'antd';
import usePerms from '../hooks/usePerms';

export default function PermButton({ need, ...rest }) {
  const { hasAny } = usePerms();
  if (!hasAny(need)) return null;
  return <Button {...rest} />;
}
```

`usePerms` 示例：
```tsx
import { useMemo } from 'react';
import { useAuth } from '../auth/useAuth';

export default function usePerms() {
  const { perms, roles } = useAuth();
  const permSet = useMemo(() => new Set(perms || []), [perms]);
  const roleSet = useMemo(() => new Set(roles || []), [roles]);
  return {
    hasAny: (need: string[] = []) => need.some(p => permSet.has(p)),
    hasRole: (role: string) => roleSet.has(role),
  };
}
```

`ProtectedRoute` 示例：
```tsx
import { Navigate } from 'react-router-dom';
import { useAuth } from './useAuth';

export default function ProtectedRoute({ children }) {
  const { token } = useAuth();
  if (!token) return <Navigate to="/login" replace />;
  return children;
}
```

