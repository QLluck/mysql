export const scoreRule = { pattern: /^(\d{1,2}|100)(\.\d{1,2})?$/, message: '成绩需为0-100，最多2位小数' };

export const required = (msg: string) => ({ required: true, message: msg });

