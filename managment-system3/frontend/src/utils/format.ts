import dayjs from 'dayjs';

export const formatTime = (val?: string) => (val ? dayjs(val).format('YYYY-MM-DD HH:mm') : '-');

export const auditStatusText = (val: number) => {
  switch (val) {
    case 0:
      return '待审核';
    case 1:
      return '通过';
    case 2:
      return '驳回';
    default:
      return '-';
  }
};

export const selectionStatusText = (val: number) => {
  switch (val) {
    case 0:
      return '待确认';
    case 1:
      return '已确认';
    case 2:
      return '已剔除';
    default:
      return '-';
  }
};

