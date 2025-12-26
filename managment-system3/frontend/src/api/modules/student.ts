import request from '../axios';

export const listStudents = (params?: { page?: number; page_size?: number }) =>
  request.get('/students', { params });

export const createStudent = (data: { name: string; user_id?: number }) =>
  request.post('/students', data);

export const batchBindStudents = (items: { student_id: number; user_id?: number }[]) =>
  request.post('/students/batch-bind', { items });

