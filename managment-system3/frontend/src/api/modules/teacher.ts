import request from '../axios';

export const listTeachers = (params?: { office_id?: number; page?: number; page_size?: number }) =>
  request.get('/teachers', { params });

export const createTeacher = (data: { name: string; user_id?: number; office_id?: number }) =>
  request.post('/teachers', data);

export const batchBindTeachers = (items: { teacher_id: number; user_id?: number; office_id?: number }[]) =>
  request.post('/teachers/batch-bind', { items });

