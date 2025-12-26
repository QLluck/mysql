import { Navigate, Route, Routes } from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import ProtectedRoute from './auth/ProtectedRoute';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import UserManage from './pages/UserManage';
import RolePermManage from './pages/RolePermManage';
import OfficeManage from './pages/OfficeManage';
import TeacherManage from './pages/TeacherManage';
import StudentManage from './pages/StudentManage';
import TopicManage from './pages/TopicManage';
import SelectionManage from './pages/SelectionManage';

const App = () => {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <MainLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Dashboard />} />
        <Route path="users" element={<UserManage />} />
        <Route path="roles" element={<RolePermManage />} />
        <Route path="offices" element={<OfficeManage />} />
        <Route path="teachers" element={<TeacherManage />} />
        <Route path="students" element={<StudentManage />} />
        <Route path="topics" element={<TopicManage />} />
        <Route path="selections" element={<SelectionManage />} />
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
};

export default App;

