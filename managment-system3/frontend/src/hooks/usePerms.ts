import { useMemo } from 'react';
import { useAuthStore } from '../auth/useAuthStore';

export default function usePerms() {
  const { userInfo } = useAuthStore();
  const permSet = useMemo(() => new Set(userInfo?.perms || []), [userInfo?.perms]);
  const roleSet = useMemo(() => new Set(userInfo?.roles || []), [userInfo?.roles]);

  const hasAny = (needPerms: string[]) => {
    if (!needPerms.length) return true;
    return needPerms.some((perm) => permSet.has(perm));
  };

  const hasRole = (role: string) => roleSet.has(role);

  return { hasAny, hasRole };
}

