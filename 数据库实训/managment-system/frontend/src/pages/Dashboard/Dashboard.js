// {{CODE-Cycle-Integration:
//   Task_ID: [#T008]
//   Timestamp: 2025-12-05
//   Phase: D-Develop
//   Context-Analysis: "创建仪表盘页面，显示系统概览信息"
//   Principle_Applied: "Component Composition"
// }}
// {{START_MODIFICATIONS}}

import React, { useEffect, useState } from 'react';
import { Card, Row, Col, Statistic, Table } from 'antd';
import { UserOutlined, TeamOutlined, FileTextOutlined, TrophyOutlined } from '@ant-design/icons';
import { studentAPI, teacherAPI, paperAPI, gradeAPI } from '../../services/api';

const Dashboard = () => {
  const [stats, setStats] = useState({
    students: 0,
    teachers: 0,
    papers: 0,
    grades: 0,
  });

  useEffect(() => {
    loadStatistics();
  }, []);

  const loadStatistics = async () => {
    try {
      const [studentsRes, teachersRes, papersRes, gradesRes] = await Promise.all([
        studentAPI.getAll({ page: 1, page_size: 1 }),
        teacherAPI.getAll({ page: 1, page_size: 1 }),
        paperAPI.getAll({ page: 1, page_size: 1 }),
        gradeAPI.getAll({ page: 1, page_size: 1 }),
      ]);

      setStats({
        students: studentsRes.data?.total || 0,
        teachers: teachersRes.data?.total || 0,
        papers: papersRes.data?.total || 0,
        grades: gradesRes.data?.total || 0,
      });
    } catch (error) {
      console.error('加载统计数据失败:', error);
    }
  };

  return (
    <div>
      <h1 style={{ marginBottom: 24 }}>系统概览</h1>
      <Row gutter={[16, 16]}>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="学生总数"
              value={stats.students}
              prefix={<UserOutlined />}
              valueStyle={{ color: '#3f8600' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="导师总数"
              value={stats.teachers}
              prefix={<TeamOutlined />}
              valueStyle={{ color: '#1890ff' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="论文总数"
              value={stats.papers}
              prefix={<FileTextOutlined />}
              valueStyle={{ color: '#cf1322' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="成绩记录"
              value={stats.grades}
              prefix={<TrophyOutlined />}
              valueStyle={{ color: '#722ed1' }}
            />
          </Card>
        </Col>
      </Row>
      <Card style={{ marginTop: 24 }}>
        <h2>系统说明</h2>
        <p>欢迎使用毕业设计选题管理系统！</p>
        <p>本系统提供以下功能：</p>
        <ul>
          <li>学生信息管理：查看、添加、修改、删除学生信息</li>
          <li>导师信息管理：查看、添加、修改、删除导师信息</li>
          <li>论文选题管理：管理毕业设计论文选题</li>
          <li>成绩管理：管理学生成绩信息</li>
          <li>专业管理：管理专业信息</li>
          <li>管理员管理：管理系统管理员</li>
        </ul>
      </Card>
    </div>
  );
};

export default Dashboard;

// {{END_MODIFICATIONS}}

