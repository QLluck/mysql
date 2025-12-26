import bcrypt from 'bcryptjs';

// 使用 bcryptjs 在前端对密码加盐
export async function encryptPwd(plain: string): Promise<string> {
  const salt = await bcrypt.genSalt(10);
  return bcrypt.hash(plain, salt);
}

