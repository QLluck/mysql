import React, { useState } from 'react';
import { Layout } from 'antd';
import { Outlet, useLocation } from 'react-router-dom';
import SideMenu from './SideMenu';
import HeaderBar from './Header';

const { Sider, Header, Content } = Layout;

const MainLayout: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider
        width={200}
        collapsible
        collapsed={collapsed}
        onCollapse={setCollapsed}
        className="sider-shadow"
        collapsedWidth={64}
      >
        <div style={{ color: '#fff', padding: 12, textAlign: 'center', fontWeight: 600 }}>毕业设计管理</div>
        <SideMenu collapsed={collapsed} />
      </Sider>
      <Layout>
        <Header style={{ background: '#fff', padding: 0 }} className="header-border">
          <HeaderBar collapsed={collapsed} onToggle={() => setCollapsed((v) => !v)} />
        </Header>
        <Content style={{ margin: 16 }}>
          <div className="app-fade">
            <Outlet key={location.pathname} />
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default MainLayout;

