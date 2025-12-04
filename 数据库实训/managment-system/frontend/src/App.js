// {{CODE-Cycle-Integration:
//   Task_ID: [#T008]
//   Timestamp: 2025-12-05
//   Phase: D-Develop
//   Context-Analysis: "创建React主应用组件，配置路由和布局"
//   Principle_Applied: "Component Composition, Routing"
// }}
// {{START_MODIFICATIONS}}

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from 'antd';
import MainLayout from './components/Layout/MainLayout';
import StudentList from './pages/Student/StudentList';
import StudentDetail from './pages/Student/StudentDetail';
import TeacherList from './pages/Teacher/TeacherList';
import TeacherDetail from './pages/Teacher/TeacherDetail';
import PaperList from './pages/Paper/PaperList';
import GradeList from './pages/Grade/GradeList';
import MajorList from './pages/Major/MajorList';
import AdminList from './pages/Admin/AdminList';
import Dashboard from './pages/Dashboard/Dashboard';
import './App.css';

const { Content } = Layout;

function App() {
  return (
    <Router>
      <MainLayout>
        <Content style={{ padding: '24px', minHeight: '100vh' }}>
          <Routes>
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/students" element={<StudentList />} />
            <Route path="/students/:id" element={<StudentDetail />} />
            <Route path="/teachers" element={<TeacherList />} />
            <Route path="/teachers/:id" element={<TeacherDetail />} />
            <Route path="/papers" element={<PaperList />} />
            <Route path="/grades" element={<GradeList />} />
            <Route path="/majors" element={<MajorList />} />
            <Route path="/admins" element={<AdminList />} />
          </Routes>
        </Content>
      </MainLayout>
    </Router>
  );
}

export default App;

// {{END_MODIFICATIONS}}

