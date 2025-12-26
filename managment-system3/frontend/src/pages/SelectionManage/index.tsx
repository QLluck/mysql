import React, { useEffect, useMemo, useState } from 'react';
import { Table, Button, Modal, Form, Input, Select, message, Tag } from 'antd';
import PageContainer from '../../components/PageContainer';
import { listSelections, createSelection, updateSelection } from '../../api/modules/selection';
import { selectionStatusText } from '../../utils/format';
import { required, scoreRule } from '../../utils/validate';
import usePerms from '../../hooks/usePerms';

const SelectionManage: React.FC = () => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [statusFilter, setStatusFilter] = useState<number | undefined>();
  const [keyword, setKeyword] = useState('');
  const [actionLoading, setActionLoading] = useState(false);
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [form] = Form.useForm();
  const { hasRole } = usePerms();

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await listSelections();
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
        .filter((item) => (statusFilter === undefined ? true : item.status === statusFilter))
        .filter((item) => String(item.topic_id || '').includes(keyword)),
    [data, statusFilter, keyword],
  );

  const isStudent = hasRole('学生');
  const isTeacher = hasRole('普通教师');
  const isAdmin = hasRole('系统管理员');

  const handleCreate = async () => {
    const values = await form.validateFields();
    setActionLoading(true);
    await createSelection({ topic_id: Number(values.topic_id) });
    message.success('已预选');
    setVisible(false);
    form.resetFields();
    setActionLoading(false);
    fetchData();
  };

  const handleUpdate = async (record: any, payload: any) => {
    setActionLoading(true);
    await updateSelection(record.id, payload);
    setActionLoading(false);
    message.success('已更新');
    fetchData();
  };

  const renderStatusTag = (v: number) => {
    const color = v === 1 ? 'green' : v === 2 ? 'red' : 'orange';
    return <Tag color={color}>{selectionStatusText(v)}</Tag>;
  };

  return (
    <PageContainer
      title="选题管理"
      crumbs={['选题管理']}
      extra={
        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
          <Input.Search placeholder="按课题ID搜索" allowClear onSearch={setKeyword} style={{ width: 200 }} />
          <Select
            placeholder="状态筛选"
            allowClear
            style={{ width: 140 }}
            value={statusFilter}
            onChange={(v) => setStatusFilter(v)}
            options={[
              { value: 0, label: '待确认' },
              { value: 1, label: '已确认' },
              { value: 2, label: '已剔除' },
            ]}
          />
          {isStudent && (
            <Button type="primary" onClick={() => setVisible(true)}>
              预选课题
            </Button>
          )}
        </div>
      }
    >
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
          !isStudent ? { title: '学生ID', dataIndex: 'student_id' } : null,
          { title: '课题ID', dataIndex: 'topic_id' },
          {
            title: '状态',
            dataIndex: 'status',
            filters: [
              { text: '待确认', value: 0 },
              { text: '已确认', value: 1 },
              { text: '已剔除', value: 2 },
            ],
            onFilter: (value, record) => record.status === value,
            render: renderStatusTag,
          },
          {
            title: '成绩',
            dataIndex: 'score',
            render: (v) => (v != null ? Number(v).toFixed(2) : '-'),
          },
          {
            title: '操作',
            render: (_, record) => {
              if (isStudent && record.status === 0) {
                return (
                  <Button type="link" onClick={() => handleUpdate(record, { cancel: true })} loading={actionLoading}>
                    取消
                  </Button>
                );
              }
              if (isTeacher || isAdmin) {
                const showScore = record.status === 1;
                const canConfirm = record.status === 0;
                return (
                  <div style={{ display: 'flex', gap: 8 }}>
                    {canConfirm && (
                      <Select
                        defaultValue={record.status}
                        style={{ width: 120 }}
                        onChange={(v) => handleUpdate(record, { status: v })}
                        options={[
                          { value: 0, label: '待确认' },
                          { value: 1, label: '已确认' },
                          { value: 2, label: '已剔除' },
                        ]}
                      />
                    )}
                    {showScore && (
                      <Input
                        style={{ width: 120 }}
                        placeholder="成绩"
                        onBlur={(e) => {
                          const val = Number((e.target as any).value);
                          if (!scoreRule.pattern.test(String(val))) {
                            message.warning(scoreRule.message);
                            return;
                          }
                          handleUpdate(record, { score: Number(val.toFixed(2)) });
                        }}
                      />
                    )}
                  </div>
                );
              }
              return null;
            },
          },
        ].filter(Boolean) as any}
      />

      <Modal open={visible} title="预选课题" onOk={handleCreate} confirmLoading={actionLoading} onCancel={() => setVisible(false)}>
        <Form form={form} layout="vertical">
          <Form.Item name="topic_id" label="课题ID" rules={[required('请输入课题ID')]}>
            <Input placeholder="请输入课题ID" />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default SelectionManage;

