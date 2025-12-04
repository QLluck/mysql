import React, { useEffect, useState } from 'react';
import { Table, Button, Space, Modal, Form, message, Tag, Select, Input } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined } from '@ant-design/icons';
import { adminAPI, majorAPI } from '../../services/api';

const AdminList = () => {
  const [admins, setAdmins] = useState([]);
  const [loading, setLoading] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [editingAdmin, setEditingAdmin] = useState(null);
  const [majors, setMajors] = useState([]);
  const [form] = Form.useForm();

  useEffect(() => {
    loadAdmins();
    loadMajors();
  }, []);

  const loadAdmins = async () => {
    setLoading(true);
    try {
      const res = await adminAPI.getAll();
      setAdmins(res.data || []);
    } catch (error) {
      message.error('加载管理员列表失败');
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
    setEditingAdmin(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingAdmin(record);
    form.setFieldsValue(record);
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该管理员吗？',
      onOk: async () => {
        try {
          await adminAPI.delete(id);
          message.success('删除成功');
          loadAdmins();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingAdmin) {
        await adminAPI.update(editingAdmin.aID, values);
        message.success('更新成功');
      } else {
        await adminAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadAdmins();
    } catch (error) {
      message.error(editingAdmin ? '更新失败' : '添加失败');
    }
  };

  const columns = [
    {
      title: '管理员编号',
      dataIndex: 'aID',
      key: 'aID',
      width: 120,
    },
    {
      title: '姓名',
      dataIndex: 'aname',
      key: 'aname',
      width: 100,
    },
    {
      title: '性别',
      dataIndex: 'asex',
      key: 'asex',
      width: 80,
      render: (text) => text ? <Tag color={text === '男' ? 'blue' : 'pink'}>{text}</Tag> : '-',
    },
    {
      title: '专业',
      dataIndex: '专业名称',
      key: 'major',
      width: 150,
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
            icon={<EditOutlined />}
            onClick={() => handleEdit(record)}
          >
            编辑
          </Button>
          <Button
            type="link"
            danger
            icon={<DeleteOutlined />}
            onClick={() => handleDelete(record.aID)}
          >
            删除
          </Button>
        </Space>
      ),
    },
  ];

  return (
    <div>
      <div style={{ marginBottom: 16, display: 'flex', justifyContent: 'flex-end' }}>
        <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
          添加管理员
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={admins}
        loading={loading}
        rowKey="aID"
        pagination={false}
      />
      <Modal
        title={editingAdmin ? '编辑管理员' : '添加管理员'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="aID"
            label="管理员编号"
            rules={[{ required: true, message: '请输入管理员编号' }]}
          >
            <Input disabled={!!editingAdmin} type="number" />
          </Form.Item>
          <Form.Item
            name="aname"
            label="姓名"
            rules={[{ required: true, message: '请输入姓名' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item name="asex" label="性别">
            <Select>
              <Select.Option value="男">男</Select.Option>
              <Select.Option value="女">女</Select.Option>
            </Select>
          </Form.Item>
          <Form.Item name="pID" label="专业">
            <Select>
              <Select.Option value="">无</Select.Option>
              {majors.map((major) => (
                <Select.Option key={major.pID} value={major.pID}>
                  {major.pname}
                </Select.Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item name="telnumber" label="联系电话">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default AdminList;

