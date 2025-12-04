import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Card, Descriptions, Button, Spin, message } from 'antd';
import { ArrowLeftOutlined } from '@ant-design/icons';
import { studentAPI } from '../../services/api';

const StudentDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [student, setStudent] = useState(null);
  const [grades, setGrades] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadStudentData();
  }, [id]);

  const loadStudentData = async () => {
    setLoading(true);
    try {
      const [studentRes, gradesRes] = await Promise.all([
        studentAPI.getById(id),
        studentAPI.getGrades(id),
      ]);
      setStudent(studentRes.data);
      setGrades(gradesRes.data);
    } catch (error) {
      message.error('加载学生信息失败');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <Spin size="large" style={{ display: 'block', margin: '50px auto' }} />;
  }

  if (!student) {
    return <div>学生不存在</div>;
  }

  return (
    <div>
      <Button
        icon={<ArrowLeftOutlined />}
        onClick={() => navigate('/students')}
        style={{ marginBottom: 16 }}
      >
        返回列表
      </Button>
      <Card title="学生基本信息">
        <Descriptions column={2} bordered>
          <Descriptions.Item label="学号">{student.sID}</Descriptions.Item>
          <Descriptions.Item label="姓名">{student.sname}</Descriptions.Item>
          <Descriptions.Item label="性别">{student.ssex}</Descriptions.Item>
          <Descriptions.Item label="班级编号">{student.cID}</Descriptions.Item>
          <Descriptions.Item label="专业">{student.专业名称 || '-'}</Descriptions.Item>
          <Descriptions.Item label="办公地点">{student.办公地点 || '-'}</Descriptions.Item>
          <Descriptions.Item label="出生日期">{student.birth}</Descriptions.Item>
          <Descriptions.Item label="论文编号">{student.rID || '-'}</Descriptions.Item>
          <Descriptions.Item label="总评成绩">{student.TGRADE || '-'}</Descriptions.Item>
        </Descriptions>
      </Card>
      {grades && (
        <Card title="成绩信息" style={{ marginTop: 16 }}>
          <Descriptions column={2} bordered>
            <Descriptions.Item label="平时成绩">{grades.dGrade || '-'}</Descriptions.Item>
            <Descriptions.Item label="论文成绩">{grades.tGrade || '-'}</Descriptions.Item>
            <Descriptions.Item label="答辩成绩">{grades.rGrade || '-'}</Descriptions.Item>
            <Descriptions.Item label="总评成绩">{grades.TGRADE || '-'}</Descriptions.Item>
          </Descriptions>
        </Card>
      )}
    </div>
  );
};

export default StudentDetail;

