import React, { useEffect, useMemo, useState } from 'react';
import { Table, Button, Modal, Form, Input, Select, message, Tag } from 'antd';
import { ExclamationCircleOutlined } from '@ant-design/icons';
import PageContainer from '../../components/PageContainer';
import { listTopics, createTopic, updateTopic, deleteTopic } from '../../api/modules/topic';
import { auditStatusText } from '../../utils/format';
import { required } from '../../utils/validate';
import usePerms from '../../hooks/usePerms';
import { useAuthStore } from '../../auth/useAuthStore';

const TopicManage: React.FC = () => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [editItem, setEditItem] = useState<any>(null);
  const [actionLoading, setActionLoading] = useState(false);
  const [keyword, setKeyword] = useState('');
  const [statusFilter, setStatusFilter] = useState<number | undefined>(undefined);
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [form] = Form.useForm();
  const { hasRole } = usePerms();
  const { userInfo } = useAuthStore();

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await listTopics();
      setData(res.data.data || res.data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const filteredData = useMemo(
    () =>
      data
        .filter((item) => (statusFilter === undefined ? true : item.audit_status === statusFilter))
        .filter((item) => item.name?.toLowerCase().includes(keyword.toLowerCase())),
    [data, keyword, statusFilter],
  );

  const handleCreateOrUpdate = async () => {
    const values = await form.validateFields();
    const dup = data.find((d) => d.name === values.name && d.id !== editItem?.id);
    if (dup) {
      message.warning('课题名称已存在');
      return;
    }
    setActionLoading(true);
    if (editItem) {
      await updateTopic(editItem.id, values);
      message.success('更新成功');
    } else {
      await createTopic(values);
      message.success('创建成功');
    }
    setActionLoading(false);
    setVisible(false);
    setEditItem(null);
    form.resetFields();
    fetchData();
  };

  const confirmDelete = (id: number) =>
    Modal.confirm({
      title: '确认删除该课题？',
      icon: <ExclamationCircleOutlined />,
      content: '删除后不可恢复，请确认已备份数据。',
      okType: 'danger',
      onOk: async () => {
        setActionLoading(true);
        await deleteTopic(id);
        setActionLoading(false);
        fetchData();
      },
    });

  const isTeacher = hasRole('普通教师');
  const isDirector = hasRole('教研室主任');
  const isAdmin = hasRole('系统管理员');

  return (
    <PageContainer
      title="课题管理"
      crumbs={['课题管理']}
      extra={
        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
          <Input.Search
            placeholder="搜索课题名称"
            allowClear
            onSearch={setKeyword}
            style={{ width: 220 }}
          />
          <Select
            allowClear
            placeholder="审核状态"
            style={{ width: 140 }}
            value={statusFilter}
            onChange={(v) => setStatusFilter(v)}
            options={[
              { value: 0, label: '待审核' },
              { value: 1, label: '通过' },
              { value: 2, label: '驳回' },
            ]}
          />
          {(isTeacher || isAdmin) && (
            <Button type="primary" onClick={() => setVisible(true)}>
              提交课题
            </Button>
          )}
        </div>
      }
    >
      {isDirector && <div style={{ marginBottom: 8, color: '#666' }}>当前教研室：仅显示本教研室课题</div>}
      <Table
        className="table-striped"
        rowKey="id"
        loading={loading}
        dataSource={filteredData}
        pagination={{
          ...pagination,
          total: filteredData.length,
          onChange: (current, pageSize) => setPagination({ current, pageSize }),
        }}
        columns={[
          { title: 'ID', dataIndex: 'id', sorter: (a, b) => a.id - b.id, width: 80 },
          { title: '课题名称', dataIndex: 'name' },
          {
            title: '审核状态',
            dataIndex: 'audit_status',
            filters: [
              { text: '待审核', value: 0 },
              { text: '通过', value: 1 },
              { text: '驳回', value: 2 },
            ],
            onFilter: (value, record) => record.audit_status === value,
            render: (v) => (
              <Tag color={v === 1 ? 'green' : v === 2 ? 'red' : 'blue'}>{auditStatusText(v)}</Tag>
            ),
            width: 120,
          },
          { title: '教师ID', dataIndex: 'teacher_id', width: 120 },
          {
            title: '操作',
            width: 280,
            render: (_, record) => {
              const canEdit = (isTeacher || isAdmin) && record.audit_status === 0;
              const canAudit = (isDirector || isAdmin) && record.audit_status === 0;
              return (
                <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                  {canEdit && (
                    <Button
                      type="link"
                      onClick={() => {
                        setEditItem(record);
                        setVisible(true);
                        form.setFieldsValue(record);
                      }}
                    >
                      编辑
                    </Button>
                  )}
                  {canEdit && (
                    <Button type="link" danger onClick={() => confirmDelete(record.id)} loading={actionLoading}>
                      删除
                    </Button>
                  )}
                  {canAudit && (
                    <Select
                      style={{ width: 140 }}
                      defaultValue={record.audit_status}
                      onChange={(v) => updateTopic(record.id, { audit_status: v }).then(fetchData)}
                      options={[
                        { value: 0, label: '待审核', disabled: true },
                        { value: 1, label: '通过' },
                        { value: 2, label: '驳回' },
                      ]}
                    />
                  )}
                </div>
              );
            },
          },
        ]}
      />

      <Modal
        title={editItem ? '编辑课题' : '提交课题'}
        open={visible}
        onOk={handleCreateOrUpdate}
        onCancel={() => {
          setVisible(false);
          setEditItem(null);
          form.resetFields();
        }}
        confirmLoading={actionLoading}
      >
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="课题名称" rules={[required('请输入课题名称')]}>
            <Input placeholder="请输入课题名称" />
          </Form.Item>
          <Form.Item name="description" label="课题描述">
            <Input.TextArea rows={4} placeholder="请输入课题描述" />
          </Form.Item>
          {isAdmin && (
            <Form.Item name="audit_status" label="审核状态" initialValue={0}>
              <Select
                options={[
                  { value: 0, label: '待审核' },
                  { value: 1, label: '通过' },
                  { value: 2, label: '驳回' },
                ]}
              />
            </Form.Item>
          )}
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default TopicManage;

