import React, { useMemo } from 'react';
import { Menu } from 'antd';
import type { MenuProps } from 'antd';
import { useNavigate, useLocation } from 'react-router-dom';
import { HomeOutlined, BookOutlined, FileSearchOutlined, TeamOutlined, ApartmentOutlined, UserOutlined, IdcardOutlined } from '@ant-design/icons';
import usePerms from '../hooks/usePerms';

interface Props {
  collapsed: boolean;
}

const SideMenu: React.FC<Props> = ({ collapsed }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const { hasRole } = usePerms();

  const items = useMemo(() => {
    const base: MenuProps['items'] = [
      { key: '/', label: '首页', icon: <HomeOutlined /> },
      { key: '/topics', label: '课题管理', icon: <BookOutlined /> },
      { key: '/selections', label: '选题管理', icon: <FileSearchOutlined /> },
    ];
    if (hasRole('系统管理员')) {
      base.push(
        { key: '/users', label: '用户管理', icon: <UserOutlined /> },
        { key: '/roles', label: '角色权限', icon: <IdcardOutlined /> },
        { key: '/offices', label: '教研室', icon: <ApartmentOutlined /> },
        { key: '/teachers', label: '教师管理', icon: <TeamOutlined /> },
        { key: '/students', label: '学生管理', icon: <TeamOutlined /> },
      );
    }
    if (hasRole('教研室主任') && !hasRole('系统管理员')) {
      base.push({ key: '/offices', label: '教研室', icon: <ApartmentOutlined /> });
    }
    return base;
  }, [hasRole]);

  return (
    <Menu
      mode="inline"
      inlineCollapsed={collapsed}
      selectedKeys={[location.pathname]}
      items={items}
      onClick={(e) => navigate(e.key)}
      style={{ height: '100%', borderRight: 0 }}
    />
  );
};

export default SideMenu;

