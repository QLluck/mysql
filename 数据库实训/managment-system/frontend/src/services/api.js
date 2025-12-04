// {{CODE-Cycle-Integration:
//   Task_ID: [#T008]
//   Timestamp: 2025-12-05
//   Phase: D-Develop
//   Context-Analysis: "创建API服务模块，封装所有API请求"
//   Principle_Applied: "DRY, Single Responsibility"
// }}
// {{START_MODIFICATIONS}}

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 可以在这里添加token等认证信息
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    console.error('API请求错误:', error);
    // 提供更详细的错误信息
    if (error.response) {
      // 服务器返回了错误状态码
      console.error('响应错误:', error.response.status, error.response.data);
    } else if (error.request) {
      // 请求已发出但没有收到响应
      console.error('网络错误: 无法连接到后端服务，请确保后端服务正在运行');
    } else {
      // 其他错误
      console.error('请求错误:', error.message);
    }
    return Promise.reject(error);
  }
);

// 学生相关API
export const studentAPI = {
  getAll: (params) => api.get('/students', { params }),
  getById: (id) => api.get(`/students/${id}`),
  create: (data) => api.post('/students', data),
  update: (id, data) => api.put(`/students/${id}`, data),
  delete: (id) => api.delete(`/students/${id}`),
  getGrades: (id) => api.get(`/students/${id}/grades`),
};

// 导师相关API
export const teacherAPI = {
  getAll: (params) => api.get('/teachers', { params }),
  getById: (id) => api.get(`/teachers/${id}`),
  create: (data) => api.post('/teachers', data),
  update: (id, data) => api.put(`/teachers/${id}`, data),
  delete: (id) => api.delete(`/teachers/${id}`),
  getPapers: (id) => api.get(`/teachers/${id}/papers`),
};

// 论文相关API
export const paperAPI = {
  getAll: (params) => api.get('/papers', { params }),
  getById: (id) => api.get(`/papers/${id}`),
  create: (data) => api.post('/papers', data),
  update: (id, data) => api.put(`/papers/${id}`, data),
  delete: (id) => api.delete(`/papers/${id}`),
};

// 成绩相关API
export const gradeAPI = {
  getAll: (params) => api.get('/grades', { params }),
  getById: (id) => api.get(`/grades/${id}`),
  create: (data) => api.post('/grades', data),
  update: (id, data) => api.put(`/grades/${id}`, data),
  delete: (id) => api.delete(`/grades/${id}`),
};

// 专业相关API
export const majorAPI = {
  getAll: (params) => api.get('/majors', { params }),
  getById: (id) => api.get(`/majors/${id}`),
  create: (data) => api.post('/majors', data),
  update: (id, data) => api.put(`/majors/${id}`, data),
  delete: (id) => api.delete(`/majors/${id}`),
};

// 管理员相关API
export const adminAPI = {
  getAll: () => api.get('/admins'),
  getById: (id) => api.get(`/admins/${id}`),
  create: (data) => api.post('/admins', data),
  update: (id, data) => api.put(`/admins/${id}`, data),
  delete: (id) => api.delete(`/admins/${id}`),
};

export default api;

// {{END_MODIFICATIONS}}

