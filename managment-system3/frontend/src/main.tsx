import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ConfigProvider, theme } from 'antd';
import App from './App';
import 'antd/dist/reset.css';
import './styles/global.css';

// 初始化 React Query Client（请求缓存）
const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <ConfigProvider
        theme={{
          token: {
            colorPrimary: '#1890ff',
            colorSuccess: '#52c41a',
            colorWarning: '#faad14',
            colorError: '#f5222d',
            fontFamily: "'Inter', 'Microsoft YaHei', sans-serif",
            borderRadius: 8,
          },
          algorithm: theme.defaultAlgorithm,
        }}
      >
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </ConfigProvider>
    </QueryClientProvider>
  </React.StrictMode>,
);

