import React, { useEffect, useState } from 'react';
import { Table, Button, Input, Space, Modal, Form, message, Tag } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SearchOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';
import { teacherAPI, majorAPI } from '../../services/api';

const TeacherList = () => {
  const [teachers, setTeachers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [keyword, setKeyword] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingTeacher, setEditingTeacher] = useState(null);
  const [majors, setMajors] = useState([]);
  const [form] = Form.useForm();
  const navigate = useNavigate();

  useEffect(() => {
    loadTeachers();
    loadMajors();
  }, [page, pageSize, keyword]);

  const loadTeachers = async () => {
    setLoading(true);
    try {
      const res = await teacherAPI.getAll({
        page,
        page_size: pageSize,
        keyword,
      });
      if (res && res.code === 200) {
        setTeachers(res.data?.list || []);
        setTotal(res.data?.total || 0);
      } else {
        message.error(res?.message || '加载导师列表失败');
      }
    } catch (error) {
      console.error('加载导师列表错误:', error);
      const errorMsg = error.response?.data?.message || error.message || '无法连接到后端服务';
      message.error(`加载导师列表失败: ${errorMsg}`);
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
    setEditingTeacher(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingTeacher(record);
    form.setFieldsValue(record);
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该导师吗？',
      onOk: async () => {
        try {
          await teacherAPI.delete(id);
          message.success('删除成功');
          loadTeachers();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingTeacher) {
        await teacherAPI.update(editingTeacher.tID, values);
        message.success('更新成功');
      } else {
        await teacherAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadTeachers();
    } catch (error) {
      message.error(editingTeacher ? '更新失败' : '添加失败');
    }
  };

  const columns = [
    {
      title: '导师编号',
      dataIndex: 'tID',
      key: 'tID',
      width: 120,
    },
    {
      title: '姓名',
      dataIndex: 'tname',
      key: 'tname',
      width: 100,
    },
    {
      title: '性别',
      dataIndex: 'tsex',
      key: 'tsex',
      width: 80,
      render: (text) => <Tag color={text === '男' ? 'blue' : 'pink'}>{text}</Tag>,
    },
    {
      title: '专业',
      dataIndex: '专业名称',
      key: 'major',
      width: 150,
    },
    {
      title: '职称',
      dataIndex: 'ttitle',
      key: 'ttitle',
      width: 100,
    },
    {
      title: '联系电话',
      dataIndex: 'telnumber',
      key: 'telnumber',
      width: 120,
    },
    {
      title: '操作',
      key: 'action',
      width: 200,
      render: (_, record) => (
        <Space>
          <Button
            type="link"
            onClick={() => navigate(`/teachers/${record.tID}`)}
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
            onClick={() => handleDelete(record.tID)}
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
            placeholder="搜索导师编号或姓名"
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
          添加导师
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={teachers}
        loading={loading}
        rowKey="tID"
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
        title={editingTeacher ? '编辑导师' : '添加导师'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="tID"
            label="导师编号"
            rules={[{ required: true, message: '请输入导师编号' }]}
          >
            <Input disabled={!!editingTeacher} />
          </Form.Item>
          <Form.Item
            name="tname"
            label="姓名"
            rules={[{ required: true, message: '请输入姓名' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="tsex"
            label="性别"
            rules={[{ required: true, message: '请选择性别' }]}
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
          <Form.Item name="ttitle" label="职称">
            <Input />
          </Form.Item>
          <Form.Item name="telnumber" label="联系电话">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default TeacherList;

