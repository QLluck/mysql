import bcrypt

# --------------------------
# 步骤1：用户注册时，加密密码并存储到数据库
# --------------------------
def register_password(plain_password):
    # 1. 将明文密码转为字节（bcrypt要求字节输入）
    password_bytes = plain_password.encode('utf-8')
    # 2. 生成随机盐值（工作因子12，越高越安全但越慢）
    salt = bcrypt.gensalt(rounds=12)
    # 3. 加密密码（盐值会嵌入最终的密文中）
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    # 4. 将密文转为字符串存储（方便数据库存储）
    return hashed_password.decode('utf-8')

# 模拟注册：存储加密后的密码到数据库
stored_hash = register_password("123456")
print("数据库中存储的密文：", stored_hash)
# 输出示例：$2a$12$Z9876543210abcdefghijklmnopqrstuvwxyz

# --------------------------
# 步骤2：用户登录时，验证密码
# --------------------------
def verify_password(stored_hash, input_password):
    # 1. 将存储的密文字符串转回字节
    stored_hash_bytes = stored_hash.encode('utf-8')
    # 2. 将输入的明文密码转为字节
    input_password_bytes = input_password.encode('utf-8')
    # 3. 验证：bcrypt会自动从stored_hash_bytes中提取盐值，用该盐值加密输入密码后对比
    return bcrypt.checkpw(input_password_bytes, stored_hash_bytes)

# 模拟登录验证
# 正确密码：验证通过
is_valid1 = verify_password(stored_hash, "123456")
print("正确密码验证结果：", is_valid1)  # True

# 错误密码：验证失败
is_valid2 = verify_password(stored_hash, "654321")
print("错误密码验证结果：", is_valid2)  # False