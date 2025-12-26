import React, { useEffect, useMemo, useState } from 'react';
import { Table, Button, Modal, Form, Input, message } from 'antd';
import PageContainer from '../../components/PageContainer';
import { listOffices, createOffice, bindDirector } from '../../api/modules/office';
import { required } from '../../utils/validate';

const OfficeManage: React.FC = () => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [bindItem, setBindItem] = useState<any>(null);
  const [keyword, setKeyword] = useState('');
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [form] = Form.useForm();
  const [bindForm] = Form.useForm();

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await listOffices();
      setData(res.data.data?.items || res.data.items || []);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const filtered = useMemo(
    () => data.filter((i) => i.name?.toLowerCase().includes(keyword.toLowerCase())),
    [data, keyword],
  );

  const handleCreate = async () => {
    const values = await form.validateFields();
    await createOffice(values);
    message.success('创建成功');
    setVisible(false);
    fetchData();
  };

  const handleBind = async () => {
    const values = await bindForm.validateFields();
    await bindDirector(bindItem.id, values.user_id || null);
    message.success('绑定成功');
    setBindItem(null);
    fetchData();
  };

  return (
    <PageContainer
      title="教研室管理"
      crumbs={['教研室管理']}
      extra={
        <Button type="primary" onClick={() => setVisible(true)}>
          新增教研室
        </Button>
      }
    >
      <Input.Search
        placeholder="搜索教研室"
        allowClear
        onSearch={setKeyword}
        style={{ width: 220, marginBottom: 12 }}
      />
      <Table
        rowKey="id"
        loading={loading}
        dataSource={filtered}
        pagination={{
          ...pagination,
          total: filtered.length,
          onChange: (current, pageSize) => setPagination({ current, pageSize }),
        }}
        columns={[
          { title: 'ID', dataIndex: 'id' },
          { title: '名称', dataIndex: 'name' },
          { title: '主任用户ID', dataIndex: 'user_id' },
          {
            title: '操作',
            render: (_, record) => (
              <Button type="link" onClick={() => setBindItem(record)}>
                绑定主任
              </Button>
            ),
          },
        ]}
      />

      <Modal open={visible} title="新增教研室" onOk={handleCreate} onCancel={() => setVisible(false)}>
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="名称" rules={[required('请输入名称')]}>
            <Input />
          </Form.Item>
          <Form.Item name="user_id" label="主任用户ID">
            <Input />
          </Form.Item>
        </Form>
      </Modal>

      <Modal open={!!bindItem} title={`绑定主任 - ${bindItem?.name || ''}`} onOk={handleBind} onCancel={() => setBindItem(null)}>
        <Form form={bindForm} layout="vertical">
          <Form.Item name="user_id" label="主任用户ID">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default OfficeManage;

