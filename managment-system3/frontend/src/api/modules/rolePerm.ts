import request from '../axios';

export const listRoles = () => request.get('/roles');

export const createRole = (data: { name: string }) => request.post('/roles', data);

export const bindPerms = (role_id: number, permissions: string[]) =>
  request.post(`/roles/${role_id}/perms`, { permissions });

