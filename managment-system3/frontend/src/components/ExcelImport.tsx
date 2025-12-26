import React, { useState } from 'react';
import { Upload, message, Modal, Table } from 'antd';
import type { UploadProps } from 'antd';
import * as XLSX from 'xlsx';

interface ExcelImportProps {
  acceptTypes?: string[];
  onData: (rows: any[]) => Promise<void>;
  requiredFields?: string[];
  uniqueField?: string;
  fieldPatterns?: Record<string, RegExp>;
  children?: React.ReactNode;
}

const ExcelImport: React.FC<ExcelImportProps> = ({
  onData,
  acceptTypes = ['.xlsx', '.xls'],
  requiredFields = [],
  uniqueField,
  fieldPatterns = { username: /^[a-zA-Z0-9]+$/ },
  children,
}) => {
  const [result, setResult] = useState<{ success: any[]; failed: { row: any; reason: string }[] }>({
    success: [],
    failed: [],
  });
  const [visible, setVisible] = useState(false);

  const validateRows = (rows: any[]) => {
    const failed: { row: any; reason: string }[] = [];
    const success: any[] = [];
    const seen = new Set<string>();

    rows.forEach((row) => {
      // 必填校验
      for (const f of requiredFields) {
        if (!row[f]) {
          failed.push({ row, reason: `${f} 为空` });
          return;
        }
      }
      // 格式校验
      for (const [field, reg] of Object.entries(fieldPatterns)) {
        if (row[field] && !reg.test(String(row[field]).trim())) {
          failed.push({ row, reason: `${field} 格式不合法` });
          return;
        }
      }
      // 重复校验
      if (uniqueField) {
        const key = String(row[uniqueField]).trim();
        if (seen.has(key)) {
          failed.push({ row, reason: `${uniqueField} 重复` });
          return;
        }
        seen.add(key);
      }
      success.push(row);
    });

    return { success, failed };
  };

  const props: UploadProps = {
    accept: acceptTypes.join(','),
    beforeUpload: (file) => {
      const reader = new FileReader();
      reader.onload = async (e) => {
        try {
          const workbook = XLSX.read(e.target?.result, { type: 'binary' });
          const sheet = workbook.Sheets[workbook.SheetNames[0]];
          const rows = XLSX.utils.sheet_to_json(sheet);
          const { success, failed } = validateRows(rows);
          setResult({ success, failed });
          setVisible(true);
          if (success.length) {
            await onData(success);
            message.success(`导入成功 ${success.length} 条${failed.length ? `，失败 ${failed.length} 条` : ''}`);
          } else {
            message.error('无有效数据，请检查文件');
          }
        } catch (err) {
          message.error('解析文件失败');
        }
      };
      reader.readAsBinaryString(file);
      return false; // 阻止自动上传
    },
  };

  return (
    <>
      <Upload {...props} showUploadList={false}>
        {children}
      </Upload>
      <Modal open={visible} title="导入结果" onCancel={() => setVisible(false)} footer={null} width={700}>
        <p>
          成功：{result.success.length} 条，失败：{result.failed.length} 条
        </p>
        {result.failed.length > 0 && (
          <Table
            size="small"
            rowKey={(_, idx) => idx.toString()}
            dataSource={result.failed}
            columns={[
              { title: '原因', dataIndex: 'reason', width: 180 },
              { title: '数据', dataIndex: 'row', render: (row) => JSON.stringify(row) },
            ]}
            pagination={false}
          />
        )}
      </Modal>
    </>
  );
};

export default ExcelImport;

