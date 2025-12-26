import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface UserInfo {
  userId: number;
  username: string;
  roles: string[];
  perms: string[];
}

interface AuthState {
  token: string | null;
  userInfo: UserInfo | null;
  setToken: (token: string) => void;
  setUserInfo: (info: UserInfo | null) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      userInfo: null,
      setToken: (token) => set({ token }),
      setUserInfo: (info) => set({ userInfo: info }),
      logout: () => set({ token: null, userInfo: null }),
    }),
    { name: 'auth-storage' },
  ),
);

