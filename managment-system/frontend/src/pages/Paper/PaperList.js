import React, { useEffect, useState } from 'react';
import { Table, Button, Input, Space, Modal, Form, message, Select } from 'antd';
import { PlusOutlined, EditOutlined, DeleteOutlined, SearchOutlined } from '@ant-design/icons';
import { paperAPI, teacherAPI } from '../../services/api';

const PaperList = () => {
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [keyword, setKeyword] = useState('');
  const [teacherId, setTeacherId] = useState('');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingPaper, setEditingPaper] = useState(null);
  const [teachers, setTeachers] = useState([]);
  const [form] = Form.useForm();

  useEffect(() => {
    loadPapers();
    loadTeachers();
  }, [page, pageSize, keyword, teacherId]);

  const loadPapers = async () => {
    setLoading(true);
    try {
      const res = await paperAPI.getAll({
        page,
        page_size: pageSize,
        keyword,
        teacher_id: teacherId,
      });
      setPapers(res.data?.list || []);
      setTotal(res.data?.total || 0);
    } catch (error) {
      message.error('加载论文列表失败');
    } finally {
      setLoading(false);
    }
  };

  const loadTeachers = async () => {
    try {
      const res = await teacherAPI.getAll({ page: 1, page_size: 1000 });
      setTeachers(res.data?.list || []);
    } catch (error) {
      console.error('加载导师列表失败:', error);
    }
  };

  const handleAdd = () => {
    setEditingPaper(null);
    form.resetFields();
    setModalVisible(true);
  };

  const handleEdit = (record) => {
    setEditingPaper(record);
    form.setFieldsValue(record);
    setModalVisible(true);
  };

  const handleDelete = async (id) => {
    Modal.confirm({
      title: '确认删除',
      content: '确定要删除该论文吗？',
      onOk: async () => {
        try {
          await paperAPI.delete(id);
          message.success('删除成功');
          loadPapers();
        } catch (error) {
          message.error('删除失败');
        }
      },
    });
  };

  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      if (editingPaper) {
        await paperAPI.update(editingPaper.tID, values);
        message.success('更新成功');
      } else {
        await paperAPI.create(values);
        message.success('添加成功');
      }
      setModalVisible(false);
      loadPapers();
    } catch (error) {
      message.error(editingPaper ? '更新失败' : '添加失败');
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
      title: '导师姓名',
      dataIndex: '导师姓名',
      key: 'teacherName',
      width: 100,
    },
    {
      title: '论文编号',
      dataIndex: 'rID',
      key: 'rID',
      width: 120,
    },
    {
      title: '论文题目',
      dataIndex: 'rtitle',
      key: 'rtitle',
      width: 200,
    },
    {
      title: '论文类型',
      dataIndex: 'rtype',
      key: 'rtype',
      width: 100,
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
            placeholder="搜索论文题目或类型"
            prefix={<SearchOutlined />}
            value={keyword}
            onChange={(e) => {
              setKeyword(e.target.value);
              setPage(1);
            }}
            style={{ width: 250 }}
            allowClear
          />
          <Select
            placeholder="选择导师"
            value={teacherId}
            onChange={(value) => {
              setTeacherId(value);
              setPage(1);
            }}
            style={{ width: 200 }}
            allowClear
          >
            {teachers.map((teacher) => (
              <Select.Option key={teacher.tID} value={teacher.tID}>
                {teacher.tname}
              </Select.Option>
            ))}
          </Select>
        </Space>
        <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
          添加论文
        </Button>
      </div>
      <Table
        columns={columns}
        dataSource={papers}
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
        title={editingPaper ? '编辑论文' : '添加论文'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => setModalVisible(false)}
        width={600}
      >
        <Form form={form} layout="vertical">
          <Form.Item
            name="tID"
            label="导师编号"
            rules={[{ required: true, message: '请选择导师' }]}
          >
            <Select disabled={!!editingPaper}>
              {teachers.map((teacher) => (
                <Select.Option key={teacher.tID} value={teacher.tID}>
                  {teacher.tname} ({teacher.tID})
                </Select.Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item name="rID" label="论文编号">
            <Input />
          </Form.Item>
          <Form.Item
            name="rtitle"
            label="论文题目"
            rules={[{ required: true, message: '请输入论文题目' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item name="rtype" label="论文类型">
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default PaperList;

