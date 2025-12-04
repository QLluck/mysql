import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Card, Descriptions, Button, Spin, message, Table } from 'antd';
import { ArrowLeftOutlined } from '@ant-design/icons';
import { teacherAPI, paperAPI } from '../../services/api';

const TeacherDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [teacher, setTeacher] = useState(null);
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadTeacherData();
  }, [id]);

  const loadTeacherData = async () => {
    setLoading(true);
    try {
      const [teacherRes, papersRes] = await Promise.all([
        teacherAPI.getById(id),
        teacherAPI.getPapers(id),
      ]);
      setTeacher(teacherRes.data);
      setPapers(papersRes.data || []);
    } catch (error) {
      message.error('加载导师信息失败');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <Spin size="large" style={{ display: 'block', margin: '50px auto' }} />;
  }

  if (!teacher) {
    return <div>导师不存在</div>;
  }

  const paperColumns = [
    {
      title: '论文编号',
      dataIndex: 'rID',
      key: 'rID',
    },
    {
      title: '论文题目',
      dataIndex: 'rtitle',
      key: 'rtitle',
    },
    {
      title: '论文类型',
      dataIndex: 'rtype',
      key: 'rtype',
    },
  ];

  return (
    <div>
      <Button
        icon={<ArrowLeftOutlined />}
        onClick={() => navigate('/teachers')}
        style={{ marginBottom: 16 }}
      >
        返回列表
      </Button>
      <Card title="导师基本信息">
        <Descriptions column={2} bordered>
          <Descriptions.Item label="导师编号">{teacher.tID}</Descriptions.Item>
          <Descriptions.Item label="姓名">{teacher.tname}</Descriptions.Item>
          <Descriptions.Item label="性别">{teacher.tsex}</Descriptions.Item>
          <Descriptions.Item label="专业">{teacher.专业名称 || '-'}</Descriptions.Item>
          <Descriptions.Item label="职称">{teacher.ttitle || '-'}</Descriptions.Item>
          <Descriptions.Item label="联系电话">{teacher.telnumber || '-'}</Descriptions.Item>
        </Descriptions>
      </Card>
      <Card title="论文列表" style={{ marginTop: 16 }}>
        <Table
          columns={paperColumns}
          dataSource={papers}
          rowKey="tID"
          pagination={false}
        />
      </Card>
    </div>
  );
};

export default TeacherDetail;

