import React from 'react';
import { Button, Dropdown, Space, Tag, Tooltip } from 'antd';
import { MenuFoldOutlined, MenuUnfoldOutlined, UserOutlined } from '@ant-design/icons';
import { useAuthStore } from '../auth/useAuthStore';

interface Props {
  collapsed: boolean;
  onToggle: () => void;
}

const HeaderBar: React.FC<Props> = ({ collapsed, onToggle }) => {
  const { userInfo, logout } = useAuthStore();

  const items = [
    {
      key: 'logout',
      label: (
        <Button type="link" onClick={() => logout()}>
          退出登录
        </Button>
      ),
    },
  ];

  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0 16px' }}>
      <Button type="text" icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />} onClick={onToggle} />
      <Dropdown menu={{ items }}>
        <Space style={{ cursor: 'pointer' }}>
          <UserOutlined />
          <span>{userInfo?.username || '未登录'}</span>
          {userInfo?.roles?.map((r) => (
            <Tag key={r}>{r}</Tag>
          ))}
        </Space>
      </Dropdown>
    </div>
  );
};

export default HeaderBar;

