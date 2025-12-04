// {{CODE-Cycle-Integration:
//   Task_ID: [#T009]
//   Timestamp: 2025-12-05
//   Phase: D-Develop
//   Context-Analysis: "创建学生列表页面，包含查询、添加、修改、删除功能"
//   Principle_Applied: "CRUD Operations, Table Component"
// }}
// {{START_MODIFICATIONS}}

import React, { useEffect, useState } from 'react';
import { Table, Button, Input, Space, Modal, Form, message, Tag } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SearchOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';
import { studentAPI, majorAPI } from '../../services/api';

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [keyword, setKeyword] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingStudent, setEditingStudent] = useState(null);
  const [majors, setMajors] = useState([]);
  const [form] = Form.useForm();
  const navigate = useNavigate();

  useEffect(() => {
    loadStudents();
    loadMajors();
  }, [page, pageSize, keyword]);

  const loadStudents = async () => {
    setLoading(true);
    try {
      const res = await studentAPI.getAll({
        page,
        page_size: pageSize,
        keyword,
      });
      setStudents(res.data?.list || []);
      setTotal(res.data?.total || 0);
    } catch (error) {
      message.error('加载学生列表失败');
    } finally {
      setLoading(false);
    }
  };

  const loadMajors = async () => {
    try {
      const res = await majorAPI.getAll();
      setMajors(res.data || []);
    } catch (error) {
      console.error('加载专业列表失败:', error);
    }
  };

  const handleAdd = () => {
    setEditingStudent(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingStudent(record);
    form.setFieldsValue({
      ...record,
      birth: record.birth ? record.birth.split(' ')[0] : '',
    });
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该学生吗？',
      onOk: async () => {
        try {
          await studentAPI.delete(id);
          message.success('删除成功');
          loadStudents();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingStudent) {
        await studentAPI.update(editingStudent.sID, values);
        message.success('更新成功');
      } else {
        await studentAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadStudents();
    } catch (error) {
      message.error(editingStudent ? '更新失败' : '添加失败');
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
      title: '姓名',
      dataIndex: 'sname',
      key: 'sname',
      width: 100,
    },
    {
      title: '性别',
      dataIndex: 'ssex',
      key: 'ssex',
      width: 80,
      render: (text) => <Tag color={text === '男' ? 'blue' : 'pink'}>{text}</Tag>,
    },
    {
      title: '班级',
      dataIndex: 'cID',
      key: 'cID',
      width: 100,
    },
    {
      title: '专业',
      dataIndex: '专业名称',
      key: 'major',
      width: 150,
    },
    {
      title: '出生日期',
      dataIndex: 'birth',
      key: 'birth',
      width: 120,
    },
    {
      title: '总评成绩',
      dataIndex: 'TGRADE',
      key: 'TGRADE',
      width: 100,
      render: (text) => text || '-',
    },
    {
      title: '操作',
      key: 'action',
      width: 200,
      render: (_, record) => (
        <Space>
          <Button
            type="link"
            onClick={() => navigate(`/students/${record.sID}`)}
          >
            查看
          </Button>
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
          <Input
            placeholder="搜索学号或姓名"
            prefix={<SearchOutlined />}
            value={keyword}
            onChange={(e) => {
              setKeyword(e.target.value);
              setPage(1);
            }}
            style={{ width: 250 }}
            allowClear
          />
        </Space>
        <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
          添加学生
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={students}
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
        title={editingStudent ? '编辑学生' : '添加学生'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="sID"
            label="学号"
            rules={[{ required: true, message: '请输入学号' }]}
          >
            <Input disabled={!!editingStudent} />
          </Form.Item>
          <Form.Item
            name="sname"
            label="姓名"
            rules={[{ required: true, message: '请输入姓名' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="ssex"
            label="性别"
            rules={[{ required: true, message: '请选择性别' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="cID"
            label="班级编号"
            rules={[{ required: true, message: '请输入班级编号' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="pID"
            label="专业"
            rules={[{ required: true, message: '请选择专业' }]}
          >
            <select style={{ width: '100%', padding: '4px 11px', border: '1px solid #d9d9d9', borderRadius: '6px' }}>
              <option value="">请选择</option>
              {majors.map((major) => (
                <option key={major.pID} value={major.pID}>
                  {major.pname}
                </option>
              ))}
            </select>
          </Form.Item>
          <Form.Item
            name="birth"
            label="出生日期"
            rules={[{ required: true, message: '请输入出生日期' }]}
          >
            <Input type="date" />
          </Form.Item>
          <Form.Item name="rID" label="论文编号">
            <Input />
          </Form.Item>
          <Form.Item name="TGRADE" label="总评成绩">
            <Input type="number" />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default StudentList;

// {{END_MODIFICATIONS}}

