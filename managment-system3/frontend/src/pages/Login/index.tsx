import React from 'react';
import { Button, Card, Form, Input, message } from 'antd';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../../auth/useAuthStore';
import { encryptPwd } from '../../utils/encrypt';
import { login, getUserInfo } from '../../api/modules/auth';

const Login: React.FC = () => {
  const navigate = useNavigate();

  const handleSubmit = async (values: { username: string; password: string }) => {
    try {
      const encryptedPwd = await encryptPwd(values.password);
      const res = await login({ username: values.username, password: encryptedPwd });
      useAuthStore.getState().setToken(res.data.data.token || res.data.token);
      const userRes = await getUserInfo();
      useAuthStore.getState().setUserInfo(userRes.data.data || userRes.data);
      message.success('登录成功');
      navigate('/');
    } catch (err: any) {
      message.error(err?.response?.data?.message || '登录失败');
    }
  };

  return (
    <div className="login-bg">
      <Card className="login-card" title="毕业设计选题管理系统" headStyle={{ textAlign: 'center', fontWeight: 700 }}>
        <Form onFinish={handleSubmit} layout="vertical">
          <Form.Item name="username" label="用户名" rules={[{ required: true, message: '请输入用户名' }]}>
            <Input placeholder="请输入用户名（字母+数字）" autoFocus />
          </Form.Item>
          <Form.Item name="password" label="密码" rules={[{ required: true, message: '请输入密码' }]}>
            <Input.Password placeholder="请输入密码" />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" block>
              登录
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  );
};

export default Login;

