import axios from 'axios';
import { message } from 'antd';
import { useAuthStore } from '../auth/useAuthStore';

/**
 * 项目初始化命令（示例）：
 * npm create vite@latest graduation-design-frontend -- --template react-ts
 * cd graduation-design-frontend
 * npm install antd axios react-router-dom @tanstack/react-query zustand bcryptjs xlsx dayjs
 * npm run dev
 */

const instance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api',
  timeout: 8000,
});

// 请求拦截：附加 token
instance.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().token;
    if (token) {
      config.headers = config.headers || {};
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error),
);

// 响应拦截：状态码统一处理
instance.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error.response?.status;
    const msg = error.response?.data?.message || error.response?.data?.msg || '请求失败';
    switch (status) {
      case 401:
        message.error('登录失效，请重新登录');
        useAuthStore.getState().logout();
        window.location.href = '/login';
        break;
      case 403:
        message.error('无操作权限');
        break;
      case 400:
        message.error(msg);
        break;
      case 500:
        message.error('服务器异常，请稍后重试');
        break;
      default:
        message.error(msg);
    }
    return Promise.reject(error);
  },
);

export default instance;

