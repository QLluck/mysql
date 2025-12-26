import React from 'react';
import { Button, ButtonProps } from 'antd';
import usePerms from '../hooks/usePerms';

interface PermButtonProps extends ButtonProps {
  need: string[];
  disabledWhenNoPerm?: boolean;
}

const PermButton: React.FC<PermButtonProps> = ({ need, disabledWhenNoPerm = false, ...props }) => {
  const { hasAny } = usePerms();
  const has = hasAny(need);
  if (!has && !disabledWhenNoPerm) return null;
  return <Button {...props} disabled={!has || props.disabled} />;
};

export default PermButton;

