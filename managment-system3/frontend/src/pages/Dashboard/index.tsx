import React, { useEffect, useState } from 'react';
import { Card, Row, Col, Statistic, Progress, Space } from 'antd';
import PageContainer from '../../components/PageContainer';
import request from '../../api/axios';

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState({
    topics_total: 0,
    topics_audited: 0,
    teachers: 0,
    students: 0,
    confirmed_selections: 0,
  });

  useEffect(() => {
    // 接入 /api/stats/summary；失败时保持默认值
    request
      .get('/stats/summary')
      .then((res) => setStats(res.data.data || res.data))
      .catch(() => {});
  }, []);

  const completion =
    stats.topics_total > 0 ? Math.round((stats.topics_audited / stats.topics_total) * 100) : 0;

  return (
    <PageContainer title="概览" crumbs={['首页']}>
      <Row gutter={[16, 16]}>
        <Col xs={24} sm={12} md={6}>
          <Card>
            <Statistic title="课题总数" value={stats.topics_total} />
            <Progress percent={completion} size="small" />
          </Card>
        </Col>
        <Col xs={24} sm={12} md={6}>
          <Card>
            <Statistic title="已审核课题" value={stats.topics_audited} />
          </Card>
        </Col>
        <Col xs={24} sm={12} md={6}>
          <Card>
            <Statistic title="教师数" value={stats.teachers} />
          </Card>
        </Col>
        <Col xs={24} sm={12} md={6}>
          <Card>
            <Statistic title="学生数" value={stats.students} />
          </Card>
        </Col>
      </Row>
      <Row gutter={[16, 16]} style={{ marginTop: 16 }}>
        <Col xs={24} sm={12} md={8}>
          <Card>
            <Statistic title="已确认选题" value={stats.confirmed_selections} />
          </Card>
        </Col>
        <Col xs={24} sm={12} md={16}>
          <Card>
            <Space direction="vertical" style={{ width: '100%' }}>
              <div style={{ fontWeight: 600 }}>选题完成率</div>
              <Progress percent={completion} status="active" strokeColor="#1890ff" />
            </Space>
          </Card>
        </Col>
      </Row>
    </PageContainer>
  );
};

export default Dashboard;

