import request from '../axios';

export const listSelections = () => request.get('/selections');

export const createSelection = (data: { topic_id: number }) =>
  request.post('/selections', data);

export const updateSelection = (id: number, data: Partial<{ status: number; score: number; latest_submit_record: string; cancel: boolean }>) =>
  request.put(`/selections/${id}`, data);

