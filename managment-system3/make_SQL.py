import bcrypt
import random
import string
from faker import Faker
from datetime import datetime, timedelta

# 初始化Faker（设置中文环境）
fake = Faker('zh_CN')

# -------------------------- 常量定义 --------------------------
# 生成的SQL文件保存路径（可修改为你想要的路径）
SQL_FILE_PATH = "graduation_project_test_data.sql"

# 自增ID起始值（按文档要求）
PERMISSION_ID_START = 100    # 权限表自增起始值
ROLE_ID_START = 1           # 角色表自增起始值
USER_ID_START = 1000        # 用户表自增起始值
OFFICE_ID_START = 10        # 教研室表自增起始值
TEACHER_ID_START = 2000     # 教师表自增起始值
STUDENT_ID_START = 3000     # 学生表自增起始值
TOPIC_ID_START = 4000       # 课题表自增起始值
SELECTION_ID_START = 5000   # 选题记录表自增起始值

# 权限列表（完整）
PERMISSIONS = [
    # 系统管理类
    '新增用户', '修改用户信息', '删除用户', '配置选题规则', '修改自己密码',
    # 课题管理类
    '提交课题', '修改未审核课题', '删除未审核课题', '查看本教研室待审核课题',
    '审核课题', '查看所有已审核课题', '查看自己发布的课题',
    # 选题管理类
    '预选课题', '提交自己选择的课题', '取消未确认选题', '查看自己的选题状态',
    '查看预选自己课题的学生', '确认学生选题', '剔除学生选题',
    # 统计管理类
    '查看本教研室课题统计', '查看本教研室选题统计', '查看自己课题的选题统计',
    '查看全系统选题统计'
]

# 角色列表
ROLES = ['系统管理员', '教研室主任', '普通教师', '学生']

# 教研室名称列表
RESEARCH_OFFICES = ['计算机教研室', '数学教研室', '电子信息教研室', '自动化教研室', '机械教研室']

# 课题名称前缀（用于生成随机课题名）
TOPIC_PREFIXES = ['基于Python的', '深度学习在', '大数据分析的', '物联网技术在', '人工智能的', '软件工程中的']
TOPIC_SUFFIXES = ['应用研究', '设计与实现', '优化方法', '关键技术研究', '实践探索', '案例分析']

# 随机文本生成配置
RANDOM_TEXT_LENGTH = 200  # 课题描述/提交记录的长度

# 中文常用字（用于生成姓名，替代Faker的characters方法）
CHINESE_CHARACTERS = '的一是在不了有和人这中大为上个国我以要他时来用们生到作地于出就分对成会可主发年动同工也能下过子说产种面而方后多定行学法所民得经十三之进着等部度家电力里如水化高自二理起小物现实加量都两体制机当使点从业本去把性好应开它合还因由其些然前外天政四日那社义事平形相全表间样与关各重新线内数正心反你明看原又么利比或但质气第向道命此变条只没结解问意建月公无系军很情者最立代想已通并提直题党程展五果料象员革位入常文总次品式活设及管特件长求老头基资边流路级少图山统接知较将组见计别她手角期根论运农指几九区强放决西被干做必战先回则任取据处队南给色光门即保治北造百规热领七海口东导器压志世金增争济阶油思术极交受联什认六共权收证改清己美再采转更单风切打白教速花带安场身车例真务具万每目至达走积示议声报斗完类八离华名确才科张信马节话米整空元况今集温传土许步群广石记需段研界拉林律叫且究观越织装影算低持音众书布复容儿须际商非验连断深难近矿千周委素技备半办青省列习响约支般史感劳便团往酸历市克何除消构府称太准精值号率族维划选标写存候毛亲快效斯院查江型眼王按格养易置派层片始却专状育厂京识适属圆包火住调满县局照参红细引听该铁价严龙'

# -------------------------- 工具函数 --------------------------
def encrypt_password(plain_password: str) -> str:
    """加密密码（BCrypt）"""
    password_bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def generate_random_text(length: int = RANDOM_TEXT_LENGTH) -> str:
    """生成随机文本（模拟课题描述/提交记录）"""
    chars = string.ascii_letters + string.digits + '，。、；：！？""''（）【】《》·'
    return ''.join(random.choice(chars) for _ in range(length))

def generate_chinese_name() -> str:
    """生成符合规范的中文姓名（单姓/复姓+1-2字名）—— 修复Faker版本问题"""
    # 常见单姓
    single_surnames = ['王', '李', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴', '徐', '孙', '胡', '朱', '高']
    # 常见复姓
    double_surnames = ['欧阳', '司马', '上官', '司徒', '诸葛', '公孙', '宇文', '皇甫']
    
    # 5%概率生成复姓
    if random.random() < 0.05:
        surname = random.choice(double_surnames)
    else:
        surname = random.choice(single_surnames)
    
    # 名字长度（1-2字）
    name_length = random.choice([1, 2])
    # 改用自定义中文字符库生成名字，避免依赖Faker的characters方法
    name = ''.join(random.choice(CHINESE_CHARACTERS) for _ in range(name_length))
    
    return surname + name

def escape_sql_string(s: str) -> str:
    """转义SQL字符串中的单引号，避免语法错误"""
    return s.replace("'", "''")

# -------------------------- 生成SQL并保存到文件主函数 --------------------------
def generate_sql_scripts_to_file():
    sql_scripts = []  # 存储所有生成的SQL语句
    print(f"开始生成测试数据SQL脚本，将保存到：{SQL_FILE_PATH}\n")

    # 给SQL文件添加头部注释
    sql_scripts.append("-- 毕业设计选题管理系统 - 测试数据SQL脚本")
    sql_scripts.append(f"-- 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sql_scripts.append("-- 管理员账号：Admin，密码：admin123456（BCrypt加密）")
    sql_scripts.append("")  # 空行分隔

    # ===================== 1. 权限表 =====================
    print("生成权限表SQL...")
    permission_ids = []
    current_id = PERMISSION_ID_START
    for perm in PERMISSIONS:
        perm_escaped = escape_sql_string(perm)
        sql = f"INSERT INTO 权限 (权限ID, 权限名称) VALUES ({current_id}, '{perm_escaped}');"
        sql_scripts.append(sql)
        permission_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"权限表SQL生成完成，共{len(permission_ids)}条\n")

    # ===================== 2. 角色表 =====================
    print("生成角色表SQL...")
    role_ids = []
    current_id = ROLE_ID_START
    for role in ROLES:
        role_escaped = escape_sql_string(role)
        sql = f"INSERT INTO 角色 (角色ID, 角色名称) VALUES ({current_id}, '{role_escaped}');"
        sql_scripts.append(sql)
        role_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"角色表SQL生成完成，共{len(role_ids)}条\n")

    # ===================== 3. 角色_权限关联表 =====================
    print("生成角色_权限关联表SQL...")
    # 系统管理员（角色ID=1）权限
    admin_perm_names = [
        '新增用户', '修改用户信息', '删除用户', '配置选题规则', '审核课题',
        '查看全系统选题统计', '查看所有已审核课题', '修改自己密码'
    ]
    admin_perm_ids = [permission_ids[PERMISSIONS.index(name)] for name in admin_perm_names]
    for perm_id in admin_perm_ids:
        sql = f"INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES ({role_ids[0]}, {perm_id});"
        sql_scripts.append(sql)

    # 教研室主任（角色ID=2）权限
    director_perm_names = [
        '查看本教研室待审核课题', '审核课题', '查看本教研室课题统计',
        '查看本教研室选题统计', '查看所有已审核课题', '修改自己密码'
    ]
    director_perm_ids = [permission_ids[PERMISSIONS.index(name)] for name in director_perm_names]
    for perm_id in director_perm_ids:
        sql = f"INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES ({role_ids[1]}, {perm_id});"
        sql_scripts.append(sql)

    # 普通教师（角色ID=3）权限
    teacher_perm_names = [
        '提交课题', '修改未审核课题', '删除未审核课题', '查看自己发布的课题',
        '查看预选自己课题的学生', '确认学生选题', '剔除学生选题',
        '查看自己课题的选题统计', '查看所有已审核课题', '修改自己密码'
    ]
    teacher_perm_ids = [permission_ids[PERMISSIONS.index(name)] for name in teacher_perm_names]
    for perm_id in teacher_perm_ids:
        sql = f"INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES ({role_ids[2]}, {perm_id});"
        sql_scripts.append(sql)

    # 学生（角色ID=4）权限
    student_perm_names = [
        '查看所有已审核课题', '预选课题', '提交自己选择的课题',
        '取消未确认选题', '查看自己的选题状态', '修改自己密码'
    ]
    student_perm_ids = [permission_ids[PERMISSIONS.index(name)] for name in student_perm_names]
    for perm_id in student_perm_ids:
        sql = f"INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES ({role_ids[3]}, {perm_id});"
        sql_scripts.append(sql)
    sql_scripts.append("")  # 空行分隔
    print("角色_权限关联表SQL生成完成\n")

    # ===================== 4. 用户表 =====================
    print("生成用户表SQL...")
    user_ids = []
    current_id = USER_ID_START

    # 管理员用户
    admin_username = 'Admin'
    admin_password = encrypt_password('admin123456')
    admin_password_escaped = escape_sql_string(admin_password)
    sql = f"INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES ({current_id}, '{admin_username}', '{admin_password_escaped}');"
    sql_scripts.append(sql)
    admin_user_id = current_id
    user_ids.append(admin_user_id)
    current_id += 1

    # 10个教师用户
    teacher_user_ids = []
    for i in range(10):
        username = f'teacher{i+1:02d}'
        password = encrypt_password('123456')
        password_escaped = escape_sql_string(password)
        sql = f"INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES ({current_id}, '{username}', '{password_escaped}');"
        sql_scripts.append(sql)
        teacher_user_ids.append(current_id)
        user_ids.append(current_id)
        current_id += 1

    # 20个学生用户
    student_user_ids = []
    for i in range(20):
        username = f'student{i+1:02d}'
        password = encrypt_password('123456')
        password_escaped = escape_sql_string(password)
        sql = f"INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES ({current_id}, '{username}', '{password_escaped}');"
        sql_scripts.append(sql)
        student_user_ids.append(current_id)
        user_ids.append(current_id)
        current_id += 1

    # 5个主任用户
    director_user_ids = []
    for i in range(5):
        username = f'director{i+1:02d}'
        password = encrypt_password('123456')
        password_escaped = escape_sql_string(password)
        sql = f"INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES ({current_id}, '{username}', '{password_escaped}');"
        sql_scripts.append(sql)
        director_user_ids.append(current_id)
        user_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"用户表SQL生成完成，共{len(user_ids)}条\n")

    # ===================== 5. 用户_角色关联表 =====================
    print("生成用户_角色关联表SQL...")
    # 管理员绑定系统管理员角色
    sql = f"INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES ({admin_user_id}, {role_ids[0]});"
    sql_scripts.append(sql)

    # 主任用户绑定教研室主任角色
    for user_id in director_user_ids:
        sql = f"INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES ({user_id}, {role_ids[1]});"
        sql_scripts.append(sql)

    # 教师用户绑定普通教师角色
    for user_id in teacher_user_ids:
        sql = f"INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES ({user_id}, {role_ids[2]});"
        sql_scripts.append(sql)

    # 学生用户绑定学生角色
    for user_id in student_user_ids:
        sql = f"INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES ({user_id}, {role_ids[3]});"
        sql_scripts.append(sql)
    sql_scripts.append("")  # 空行分隔
    print("用户_角色关联表SQL生成完成\n")

    # ===================== 6. 教研室表 =====================
    print("生成教研室表SQL...")
    office_ids = []
    current_id = OFFICE_ID_START
    # 绑定主任用户（前5个主任用户对应5个教研室）
    for i, office_name in enumerate(RESEARCH_OFFICES):
        office_name_escaped = escape_sql_string(office_name)
        director_user_id = director_user_ids[i] if i < len(director_user_ids) else 'NULL'
        sql = f"INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES ({current_id}, '{office_name_escaped}', {director_user_id});"
        sql_scripts.append(sql)
        office_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"教研室表SQL生成完成，共{len(office_ids)}条\n")

    # ===================== 7. 教师表 =====================
    print("生成教师表SQL...")
    teacher_ids = []
    current_id = TEACHER_ID_START
    # 10个教师
    for i in range(10):
        teacher_name = generate_chinese_name()
        teacher_name_escaped = escape_sql_string(teacher_name)
        user_id = teacher_user_ids[i] if i < len(teacher_user_ids) else 'NULL'
        office_id = random.choice(office_ids)
        sql = f"INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES ({current_id}, '{teacher_name_escaped}', {user_id}, {office_id});"
        sql_scripts.append(sql)
        teacher_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"教师表SQL生成完成，共{len(teacher_ids)}条\n")

    # ===================== 8. 学生表 =====================
    print("生成学生表SQL...")
    student_ids = []
    current_id = STUDENT_ID_START
    # 20个学生
    for i in range(20):
        student_name = generate_chinese_name()
        student_name_escaped = escape_sql_string(student_name)
        user_id = student_user_ids[i] if i < len(student_user_ids) else 'NULL'
        sql = f"INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES ({current_id}, '{student_name_escaped}', {user_id});"
        sql_scripts.append(sql)
        student_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"学生表SQL生成完成，共{len(student_ids)}条\n")

    # ===================== 9. 课题表 =====================
    print("生成课题表SQL...")
    topic_ids = []
    current_id = TOPIC_ID_START
    # 30个课题
    for i in range(30):
        # 随机生成课题名称
        topic_name = random.choice(TOPIC_PREFIXES) + generate_random_text(8) + random.choice(TOPIC_SUFFIXES)
        topic_name_escaped = escape_sql_string(topic_name)
        topic_desc = generate_random_text()
        topic_desc_escaped = escape_sql_string(topic_desc)
        audit_status = random.choice([0, 1, 2])
        teacher_id = random.choice(teacher_ids)
        sql = f"INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES ({current_id}, '{topic_name_escaped}', '{topic_desc_escaped}', {audit_status}, {teacher_id});"
        sql_scripts.append(sql)
        topic_ids.append(current_id)
        current_id += 1
    sql_scripts.append("")  # 空行分隔
    print(f"课题表SQL生成完成，共{len(topic_ids)}条\n")

    # ===================== 10. 选题记录表 =====================
    print("生成选题记录表SQL...")
    current_id = SELECTION_ID_START
    # 每个学生选1-2个课题
    for student_id in student_ids:
        selected_topics = random.sample(topic_ids, random.choice([1, 2]))
        for topic_id in selected_topics:
            select_status = random.choice([0, 1, 2])
            # 修复点1：先保存datetime对象，再格式化字符串
            select_time_obj = fake.date_time_between(start_date='-30d', end_date='now')
            select_time = select_time_obj.strftime('%Y-%m-%d %H:%M:%S')
            
            # 最新提交时间和记录
            if select_status in [0, 1]:
                # 修复点2：传入datetime对象作为start_date，而非格式化后的字符串
                latest_submit_time_obj = fake.date_time_between(start_date=select_time_obj, end_date='now')
                latest_submit_time = latest_submit_time_obj.strftime('%Y-%m-%d %H:%M:%S')
                latest_submit_record = generate_random_text()
                latest_submit_record_escaped = escape_sql_string(latest_submit_record)
            else:
                latest_submit_time = 'NULL'
                latest_submit_record_escaped = 'NULL'
            
            # 成绩
            score = round(random.uniform(60, 100), 2) if select_status == 1 else 'NULL'

            # 拼接SQL（处理NULL值）
            time_part = f"'{latest_submit_time}'" if latest_submit_time != 'NULL' else 'NULL'
            record_part = f"'{latest_submit_record_escaped}'" if latest_submit_record_escaped != 'NULL' else 'NULL'
            
            sql = f"""INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES ({current_id}, {student_id}, {topic_id}, {select_status}, '{select_time}', {time_part}, {record_part}, {score});"""
            sql_scripts.append(sql)
            current_id += 1
    sql_scripts.append("")  # 空行分隔
    print("选题记录表SQL生成完成\n")

    # ===================== 将SQL写入文件 =====================
    try:
        with open(SQL_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sql_scripts))
        print(f"✅ SQL脚本已成功保存到文件：{SQL_FILE_PATH}")
    except Exception as e:
        print(f"❌ 保存SQL文件失败：{e}")
        return

    # ===================== 输出提示信息 =====================
    print("\n" + "="*80)
    print("SQL文件生成完成！")
    print(f"📄 文件路径：{SQL_FILE_PATH}")
    print(f"🔑 管理员账号：{admin_username}，密码：admin123456（已BCrypt加密）")
    print("💡 使用说明：先执行建表语句，再执行此SQL文件中的INSERT语句")
    print("="*80)

# -------------------------- 执行入口 --------------------------
if __name__ == '__main__':
    # 安装依赖提示
    print("请确保已安装依赖：pip install bcrypt faker")
    confirm = input("是否确认生成SQL文件？(y/n)：")
    if confirm.lower() == 'y':
        generate_sql_scripts_to_file()
    else:
        print("操作取消")