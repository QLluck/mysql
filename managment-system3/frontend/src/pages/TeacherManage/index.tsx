import React, { useEffect, useMemo, useState } from 'react';
import { Table, Button, Modal, Form, Input, message } from 'antd';
import PageContainer from '../../components/PageContainer';
import { listTeachers, createTeacher, batchBindTeachers } from '../../api/modules/teacher';
import ExcelImport from '../../components/ExcelImport';
import { required } from '../../utils/validate';

const TeacherManage: React.FC = () => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [visible, setVisible] = useState(false);
  const [keyword, setKeyword] = useState('');
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [form] = Form.useForm();

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await listTeachers();
      setData(res.data.data?.items || res.data.items || []);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const filtered = useMemo(
    () => data.filter((item) => item.name?.toLowerCase().includes(keyword.toLowerCase())),
    [data, keyword],
  );

  const handleCreate = async () => {
    const values = await form.validateFields();
    await createTeacher(values);
    message.success('创建成功');
    setVisible(false);
    fetchData();
  };

  const handleImport = async (rows: any[]) => {
    const payload = rows
      .map((r: any) => ({
        teacher_id: Number(r.teacher_id),
        user_id: r.user_id ? Number(r.user_id) : undefined,
        office_id: r.office_id ? Number(r.office_id) : undefined,
      }))
      .filter((r) => r.teacher_id);
    await batchBindTeachers(payload);
    message.success(`导入/绑定成功，共 ${payload.length} 条`);
    fetchData();
  };

  return (
    <PageContainer
      title="教师管理"
      crumbs={['教师管理']}
      extra={
        <>
          <Input.Search
            placeholder="搜索教师姓名"
            allowClear
            onSearch={setKeyword}
            style={{ width: 200, marginRight: 8 }}
          />
          <ExcelImport
            onData={handleImport}
            requiredFields={['teacher_id', 'name']}
            uniqueField="teacher_id"
          >
            <Button style={{ marginRight: 8 }}>批量导入/绑定</Button>
          </ExcelImport>
          <Button type="primary" onClick={() => setVisible(true)}>
            新增教师
          </Button>
        </>
      }
    >
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
          { title: '姓名', dataIndex: 'name' },
          { title: '用户ID', dataIndex: 'user_id' },
          { title: '教研室ID', dataIndex: 'office_id' },
        ]}
      />

      <Modal open={visible} title="新增教师" onOk={handleCreate} onCancel={() => setVisible(false)}>
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="姓名" rules={[required('请输入姓名')]}>
            <Input />
          </Form.Item>
          <Form.Item name="user_id" label="用户ID">
            <Input />
          </Form.Item>
          <Form.Item name="office_id" label="教研室ID">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </PageContainer>
  );
};

export default TeacherManage;

