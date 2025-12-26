import request from '../axios';

export const listTopics = (params?: { audit_status?: number }) =>
  request.get('/topics', { params });

export const createTopic = (data: { name: string; description?: string }) =>
  request.post('/topics', data);

export const updateTopic = (id: number, data: Partial<{ name: string; description: string; audit_status: number; teacher_id: number }>) =>
  request.put(`/topics/${id}`, data);

export const deleteTopic = (id: number) => request.delete(`/topics/${id}`);

