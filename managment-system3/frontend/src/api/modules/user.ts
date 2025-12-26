import request from '../axios';

export const createUser = (data: { username: string; password?: string }) =>
  request.post('/users', data);

export const bindUserRoles = (userId: number, role_ids: number[]) =>
  request.post(`/users/${userId}/roles`, { role_ids });

