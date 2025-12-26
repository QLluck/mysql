import React, { useMemo, useState } from 'react';
import { Table, Button, Form, Input, Modal, message } from 'antd';
import PageContainer from '../../components/PageContainer';
import { createUser } from '../../api/modules/user';
import { required } from '../../utils/validate';

const UserManage: React.FC = () => {
  const [visible, setVisible] = useState(false);
  const [loading, setLoading] = useState(false);
  const [keyword, setKeyword] = useState('');
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [data, setData] = useState<any[]>([]);
  const [form] = Form.useForm();

  const handleCreate = async () => {
    const values = await form.validateFields();
    try {
      setLoading(true);
      await createUser(values);
      message.success('创建成功');
      setVisible(false);
      setData([...data, { id: Date.now(), username: values.username }]);
      form.resetFields();
    } catch (err: any) {
      message.error(err?.response?.data?.message || '创建失败');
    } finally {
      setLoading(false);
    }
  };

  const filtered = useMemo(
    () => data.filter((item) => item.username?.toLowerCase().includes(keyword.toLowerCase())),
    [data, keyword],
  );

  return (
    <PageContainer
      title="用户管理"
      crumbs={['用户管理']}
      extra={
        <Button type="primary" onClick={() => setVisible(true)}>
          新增用户
        </Button>
      }
    >
      <Input.Search
        placeholder="搜索用户名"
        allowClear
        onSearch={setKeyword}
        style={{ width: 220, marginBottom: 12 }}
      />
      <Table
        rowKey="id"
        dataSource={filtered}
        pagination={{
          ...pagination,
          total: filtered.length,
          onChange: (current, pageSize) => setPagination({ current, pageSize }),
        }}
        columns={[{ title: '用户名', dataIndex: 'username' }]}
      />

      <Modal
        title="新增用户"
        open={visible}
        onOk={handleCreate}
        onCancel={() => setVisible(false)}
        confirmLoading={loading}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="username"
            label="用户名"
            rules={[
              required('请输入用户名'),
              {
                validator: (_, value) => {
                  if (!value) return Promise.resolve();
                  if (!/^[a-zA-Z0-9]+$/.test(value)) return Promise.reject(new Error('仅支持字母+数字'));
                  if (data.find((u) => u.username === value)) return Promise.reject(new Error('用户名已存在'));
                  return Promise.resolve();
                },
              },
            ]}
          >
            <Input placeholder="仅支持字母+数字" />
          </Form.Item>
          <Form.Item name="password" label="初始密码">
            <Input.Password placeholder="默认123456，如不填" />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default UserManage;

