import React, { useEffect, useState } from 'react';
import { Table, Button, Input, Space, Modal, Form, message, Select } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SearchOutlined } from '@ant-design/icons';
import { gradeAPI, studentAPI } from '../../services/api';

const GradeList = () => {
  const [grades, setGrades] = useState([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [studentId, setStudentId] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingGrade, setEditingGrade] = useState(null);
  const [students, setStudents] = useState([]);
  const [form] = Form.useForm();

  useEffect(() => {
    loadGrades();
    loadStudents();
  }, [page, pageSize, studentId]);

  const loadGrades = async () => {
    setLoading(true);
    try {
      const res = await gradeAPI.getAll({
        page,
        page_size: pageSize,
        student_id: studentId,
      });
      if (res && res.code === 200) {
        setGrades(res.data?.list || []);
        setTotal(res.data?.total || 0);
      } else {
        message.error(res?.message || '加载成绩列表失败');
      }
    } catch (error) {
      console.error('加载成绩列表错误:', error);
      const errorMsg = error.response?.data?.message || error.message || '无法连接到后端服务';
      message.error(`加载成绩列表失败: ${errorMsg}`);
    } finally {
      setLoading(false);
    }
  };

  const loadStudents = async () => {
    try {
      const res = await studentAPI.getAll({ page: 1, page_size: 1000 });
      setStudents(res.data?.list || []);
    } catch (error) {
      console.error('加载学生列表失败:', error);
    }
  };

  const handleAdd = () => {
    setEditingGrade(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingGrade(record);
    form.setFieldsValue(record);
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该成绩吗？',
      onOk: async () => {
        try {
          await gradeAPI.delete(id);
          message.success('删除成功');
          loadGrades();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingGrade) {
        await gradeAPI.update(editingGrade.sID, values);
        message.success('更新成功');
      } else {
        await gradeAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadGrades();
    } catch (error) {
      message.error(editingGrade ? '更新失败' : '添加失败');
    }
  };

  const columns = [
    {
      title: '学号',
      dataIndex: 'sID',
      key: 'sID',
      width: 120,
    },
    {
      title: '学生姓名',
      dataIndex: '学生姓名',
      key: 'studentName',
      width: 100,
    },
    {
      title: '平时成绩',
      dataIndex: 'dGrade',
      key: 'dGrade',
      width: 100,
      render: (text) => text || '-',
    },
    {
      title: '论文成绩',
      dataIndex: 'tGrade',
      key: 'tGrade',
      width: 100,
      render: (text) => text || '-',
    },
    {
      title: '答辩成绩',
      dataIndex: 'rGrade',
      key: 'rGrade',
      width: 100,
      render: (text) => text || '-',
    },
    {
      title: '总评成绩',
      dataIndex: '总评成绩',
      key: 'totalGrade',
      width: 100,
      render: (text) => text || '-',
    },
    {
      title: '操作',
      key: 'action',
      width: 150,
      render: (_, record) => (
        <Space>
          <Button
            type="link"
            icon={<EditOutlined />}
            onClick={() => handleEdit(record)}
          >
            编辑
          </Button>
          <Button
            type="link"
            danger
            icon={<DeleteOutlined />}
            onClick={() => handleDelete(record.sID)}
          >
            删除
          </Button>
        </Space>
      ),
    },
  ];

  return (
    <div>
      <div style={{ marginBottom: 16, display: 'flex', justifyContent: 'space-between' }}>
        <Space>
          <Select
            placeholder="选择学生"
            value={studentId}
            onChange={(value) => {
              setStudentId(value);
              setPage(1);
            }}
            style={{ width: 200 }}
            allowClear
            showSearch
            filterOption={(input, option) =>
              option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
            }
          >
            {students.map((student) => (
              <Select.Option key={student.sID} value={student.sID}>
                {student.sname} ({student.sID})
              </Select.Option>
            ))}
          </Select>
        </Space>
        <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
          添加成绩
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={grades}
        loading={loading}
        rowKey="sID"
        pagination={{
          current: page,
          pageSize: pageSize,
          total: total,
          showSizeChanger: true,
          showTotal: (total) => `共 ${total} 条`,
          onChange: (page, pageSize) => {
            setPage(page);
            setPageSize(pageSize);
          },
        }}
      />
      <Modal
        title={editingGrade ? '编辑成绩' : '添加成绩'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="sID"
            label="学号"
            rules={[{ required: true, message: '请选择学生' }]}
          >
            <Select disabled={!!editingGrade}>
              {students.map((student) => (
                <Select.Option key={student.sID} value={student.sID}>
                  {student.sname} ({student.sID})
                </Select.Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item name="dGrade" label="平时成绩">
            <Input type="number" min={0} max={100} />
          </Form.Item>
          <Form.Item name="tGrade" label="论文成绩">
            <Input type="number" min={0} max={100} />
          </Form.Item>
          <Form.Item name="rGrade" label="答辩成绩">
            <Input type="number" min={0} max={100} />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default GradeList;

