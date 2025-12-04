import React, { useEffect, useState } from 'react';
import { Table, Button, Input, Space, Modal, Form, message } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SearchOutlined } from '@ant-design/icons';
import { majorAPI } from '../../services/api';

const MajorList = () => {
  const [majors, setMajors] = useState([]);
  const [loading, setLoading] = useState(false);
  const [keyword, setKeyword] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingMajor, setEditingMajor] = useState(null);
  const [form] = Form.useForm();

  useEffect(() => {
    loadMajors();
  }, [keyword]);

  const loadMajors = async () => {
    setLoading(true);
    try {
      const res = await majorAPI.getAll({ keyword });
      setMajors(res.data || []);
    } catch (error) {
      message.error('加载专业列表失败');
    } finally {
      setLoading(false);
    }
  };

  const handleAdd = () => {
    setEditingMajor(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingMajor(record);
    form.setFieldsValue(record);
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该专业吗？',
      onOk: async () => {
        try {
          await majorAPI.delete(id);
          message.success('删除成功');
          loadMajors();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingMajor) {
        await majorAPI.update(editingMajor.pID, values);
        message.success('更新成功');
      } else {
        await majorAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadMajors();
    } catch (error) {
      message.error(editingMajor ? '更新失败' : '添加失败');
    }
  };

  const columns = [
    {
      title: '专业编号',
      dataIndex: 'pID',
      key: 'pID',
      width: 120,
    },
    {
      title: '专业名称',
      dataIndex: 'pname',
      key: 'pname',
      width: 200,
    },
    {
      title: '办公地点',
      dataIndex: 'plocal',
      key: 'plocal',
      width: 150,
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
            onClick={() => handleDelete(record.pID)}
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
        <Input
          placeholder="搜索专业编号或名称"
          prefix={<SearchOutlined />}
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          style={{ width: 250 }}
          allowClear
        />
        <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
          添加专业
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={majors}
        loading={loading}
        rowKey="pID"
        pagination={false}
      />
      <Modal
        title={editingMajor ? '编辑专业' : '添加专业'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="pID"
            label="专业编号"
            rules={[{ required: true, message: '请输入专业编号' }]}
          >
            <Input disabled={!!editingMajor} />
          </Form.Item>
          <Form.Item
            name="pname"
            label="专业名称"
            rules={[{ required: true, message: '请输入专业名称' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item name="plocal" label="办公地点">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default MajorList;

