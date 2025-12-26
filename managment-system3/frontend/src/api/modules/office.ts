import request from '../axios';

export const listOffices = (params?: { page?: number; page_size?: number }) =>
  request.get('/offices', { params });

export const createOffice = (data: { name: string; user_id?: number }) =>
  request.post('/offices', data);

export const bindDirector = (office_id: number, user_id: number | null) =>
  request.post('/offices/bind-director', { office_id, user_id });

