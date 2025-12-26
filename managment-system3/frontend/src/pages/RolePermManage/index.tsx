import React, { useState, useEffect } from 'react';
import { Table, Button, Modal, Form, Input, Select, message } from 'antd';
import PageContainer from '../../components/PageContainer';
import { listRoles, createRole, bindPerms } from '../../api/modules/rolePerm';

const ALL_PERMS = [
  '新增用户',
  '修改用户信息',
  '删除用户',
  '配置选题规则',
  '修改自己密码',
  '提交课题',
  '修改未审核课题',
  '删除未审核课题',
  '查看本教研室待审核课题',
  '审核课题',
  '查看所有已审核课题',
  '查看自己发布的课题',
  '预选课题',
  '提交自己选择的课题',
  '取消未确认选题',
  '查看自己的选题状态',
  '查看预选自己课题的学生',
  '确认学生选题',
  '剔除学生选题',
  '查看本教研室课题统计',
  '查看本教研室选题统计',
  '查看自己课题的选题统计',
  '查看全系统选题统计',
];

const RolePermManage: React.FC = () => {
  const [roles, setRoles] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [bindRole, setBindRole] = useState<any>(null);
  const [form] = Form.useForm();
  const [permForm] = Form.useForm();

  const fetchRoles = async () => {
    setLoading(true);
    try {
      const res = await listRoles();
      setRoles(res.data.data || res.data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRoles();
  }, []);

  const handleCreate = async () => {
    const values = await form.validateFields();
    await createRole(values);
    message.success('创建成功');
    setVisible(false);
    fetchRoles();
  };

  const handleBindPerm = async () => {
    const values = await permForm.validateFields();
    await bindPerms(bindRole.id, values.permissions);
    message.success('权限已更新');
    setBindRole(null);
    fetchRoles();
  };

  return (
    <PageContainer
      title="角色权限"
      crumbs={['角色权限']}
      extra={
        <Button type="primary" onClick={() => setVisible(true)}>
          新增角色
        </Button>
      }
    >
      <Table
        rowKey="id"
        dataSource={roles}
        loading={loading}
        columns={[
          { title: '角色', dataIndex: 'name' },
          {
            title: '权限',
            dataIndex: 'permissions',
            render: (v: string[]) => (v || []).join('、'),
          },
          {
            title: '操作',
            render: (_, record) => (
              <Button type="link" onClick={() => setBindRole(record)}>
                绑定权限
              </Button>
            ),
          },
        ]}
      />

      <Modal open={visible} title="新增角色" onOk={handleCreate} onCancel={() => setVisible(false)}>
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="角色名称" rules={[{ required: true, message: '请输入角色名称' }]}>
            <Input />
          </Form.Item>
        </Form>
      </Modal>

      <Modal
        open={!!bindRole}
        title={`绑定权限 - ${bindRole?.name || ''}`}
        onOk={handleBindPerm}
        onCancel={() => setBindRole(null)}
        destroyOnClose
      >
        <Form form={permForm} layout="vertical" initialValues={{ permissions: bindRole?.permissions }}>
          <Form.Item name="permissions" label="权限" rules={[{ required: true, message: '请选择权限' }]}>
            <Select mode="multiple" options={ALL_PERMS.map((p) => ({ value: p, label: p }))} />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default RolePermManage;

