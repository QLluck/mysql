// {{CODE-Cycle-Integration:
//   Task_ID: [#T008]
//   Timestamp: 2025-12-05
//   Phase: D-Develop
//   Context-Analysis: "创建主布局组件，包含导航菜单和头部"
//   Principle_Applied: "Component Composition"
// }}
// {{START_MODIFICATIONS}}

import React, { useState } from 'react';
import { Layout, Menu, theme } from 'antd';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  DashboardOutlined,
  UserOutlined,
  TeamOutlined,
  FileTextOutlined,
  TrophyOutlined,
  BookOutlined,
  SettingOutlined,
} from '@ant-design/icons';

const { Header, Sider } = Layout;

const MainLayout = ({ children }) => {
  const [collapsed, setCollapsed] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const menuItems = [
    {
      key: '/dashboard',
      icon: <DashboardOutlined />,
      label: '仪表盘',
    },
    {
      key: '/students',
      icon: <UserOutlined />,
      label: '学生管理',
    },
    {
      key: '/teachers',
      icon: <TeamOutlined />,
      label: '导师管理',
    },
    {
      key: '/papers',
      icon: <FileTextOutlined />,
      label: '论文管理',
    },
    {
      key: '/grades',
      icon: <TrophyOutlined />,
      label: '成绩管理',
    },
    {
      key: '/majors',
      icon: <BookOutlined />,
      label: '专业管理',
    },
    {
      key: '/admins',
      icon: <SettingOutlined />,
      label: '管理员管理',
    },
  ];

  const handleMenuClick = ({ key }) => {
    navigate(key);
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={setCollapsed}
        style={{
          overflow: 'auto',
          height: '100vh',
          position: 'fixed',
          left: 0,
          top: 0,
          bottom: 0,
        }}
      >
        <div
          style={{
            height: 32,
            margin: 16,
            background: 'rgba(255, 255, 255, 0.3)',
            borderRadius: 6,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'white',
            fontWeight: 'bold',
          }}
        >
          {collapsed ? '毕设' : '毕业设计管理系统'}
        </div>
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[location.pathname]}
          items={menuItems}
          onClick={handleMenuClick}
        />
      </Sider>
      <Layout style={{ marginLeft: collapsed ? 80 : 200, transition: 'all 0.2s' }}>
        <Header
          style={{
            padding: 0,
            background: colorBgContainer,
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
          }}
        >
          <div style={{ padding: '0 24px', fontSize: '18px', fontWeight: 'bold' }}>
            毕业设计选题管理系统
          </div>
        </Header>
        {children}
      </Layout>
    </Layout>
  );
};

export default MainLayout;

// {{END_MODIFICATIONS}}

