import React from 'react';
import { Breadcrumb } from 'antd';

interface PageContainerProps {
  title: string;
  children: React.ReactNode;
  extra?: React.ReactNode;
  crumbs?: string[];
}

const PageContainer: React.FC<PageContainerProps> = ({ title, children, extra, crumbs }) => (
  <div style={{ padding: 16 }}>
    {crumbs && (
      <Breadcrumb style={{ marginBottom: 12 }}>
        {crumbs.map((c) => (
          <Breadcrumb.Item key={c}>{c}</Breadcrumb.Item>
        ))}
      </Breadcrumb>
    )}
    <div className="page-card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
        <div style={{ fontSize: 18, fontWeight: 600 }}>{title}</div>
        {extra}
      </div>
      {children}
    </div>
  </div>
);

export default PageContainer;

