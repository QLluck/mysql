import request from '../axios';

export const login = (data: { username: string; password: string }) =>
  request.post('/auth/login', data);

export const getUserInfo = () => request.get('/auth/me');

