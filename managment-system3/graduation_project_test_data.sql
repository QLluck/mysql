-- 毕业设计选题管理系统 - 测试数据SQL脚本
-- 生成时间：2025-12-10 10:57:16
-- 管理员账号：Admin，密码：admin123456（BCrypt加密）

INSERT INTO 权限 (权限ID, 权限名称) VALUES (100, '新增用户');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (101, '修改用户信息');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (102, '删除用户');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (103, '配置选题规则');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (104, '修改自己密码');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (105, '提交课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (106, '修改未审核课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (107, '删除未审核课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (108, '查看本教研室待审核课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (109, '审核课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (110, '查看所有已审核课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (111, '查看自己发布的课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (112, '预选课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (113, '提交自己选择的课题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (114, '取消未确认选题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (115, '查看自己的选题状态');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (116, '查看预选自己课题的学生');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (117, '确认学生选题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (118, '剔除学生选题');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (119, '查看本教研室课题统计');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (120, '查看本教研室选题统计');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (121, '查看自己课题的选题统计');
INSERT INTO 权限 (权限ID, 权限名称) VALUES (122, '查看全系统选题统计');

INSERT INTO 角色 (角色ID, 角色名称) VALUES (1, '系统管理员');
INSERT INTO 角色 (角色ID, 角色名称) VALUES (2, '教研室主任');
INSERT INTO 角色 (角色ID, 角色名称) VALUES (3, '普通教师');
INSERT INTO 角色 (角色ID, 角色名称) VALUES (4, '学生');

INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 100);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 101);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 102);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 103);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 109);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 122);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 110);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (1, 104);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 108);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 109);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 119);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 120);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 110);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (2, 104);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 105);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 106);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 107);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 111);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 116);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 117);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 118);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 121);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 110);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (3, 104);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 110);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 112);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 113);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 114);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 115);
INSERT INTO 角色_权限 (角色ID, 权限ID) VALUES (4, 104);

INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1000, 'Admin', '$2b$12$nCwCKaGWkHI4A/Sta60KyOSzh4.XWzJw0woLYLDRU1tNhAo9MHltq');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1001, 'teacher01', '$2b$12$kCLA1KFWtWpat8HP7CnNG.f2Zx/lPp5/ovmZHnvdKnIzblllsQxdS');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1002, 'teacher02', '$2b$12$BM8bDLhKUmYceOwXfbaFYuFppHIycGDG4J8nrR5OZRQT53dPrNf4e');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1003, 'teacher03', '$2b$12$BlVq6ClYzHpYlAHki34JYuz6XZoTNOr9K6ZZRL8qsS5ahe2iqjYha');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1004, 'teacher04', '$2b$12$6zyJGv00TPiHDkhDvWW4M.Wv9sAET8sTBWoYYQDeAWOJWPW3acHhK');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1005, 'teacher05', '$2b$12$p1avqb6MuHUBp2.mbAedx.iooONN4RefJqBxYXxz4lH1D6o8C9R1K');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1006, 'teacher06', '$2b$12$x.Vuix.iturwsOxBJxobxevEgrpeaGbRvWmP9jehi.o/pjWPfKVXi');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1007, 'teacher07', '$2b$12$IQLR7IPuGaR0MVEX25nB2eK3l1ce3qcq0sHn..xGY79J/1OWSKC3a');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1008, 'teacher08', '$2b$12$b2oLl2Z7iNrUf9IMsQ8Bs.cawNih7vnw634HASYxZR0yo0K8sY2s2');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1009, 'teacher09', '$2b$12$Ztw4DwzeLVOwWKvP2pjvuOsb9uN3IP50njKPaggLg4DXI5RPWD4pu');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1010, 'teacher10', '$2b$12$e56A7c4g6rX9p5O8tYnf/ulT6eB4TTPXtSYbAScOm/Eyt3qiT3jTS');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1011, 'student01', '$2b$12$wV0jJFkxWgmeqxQ5vlcMhOm.JgftWDwAkczSSP9fQOMnZbZsNNpka');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1012, 'student02', '$2b$12$9doRGbP1svndU2GD/T/CP.J6Pbj7By3CtqHwVYJNQvNbHPRPptlB2');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1013, 'student03', '$2b$12$TgDlq4Zk8TbdkM.q.L/u/u2inQFXbfHF68kMtXYYUjs3DO78byd2e');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1014, 'student04', '$2b$12$zuLJD0rAvtuMGeSuCmLQPeorW3uTAs7Gv92..x0jwG617fvVrKeEO');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1015, 'student05', '$2b$12$Q4JlySGlse1Kl9.QmvEmtO6W8Vw3muO0zS3qBwr6ff5gQJ1KsXNWK');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1016, 'student06', '$2b$12$Obys6C1KNm32Zd1Fq9JgauPNNIo/hEwRNaymvI4Lp.Fp32KLW9WPS');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1017, 'student07', '$2b$12$6KU0f0zS6zbiYQQ.pnopYeXJMlIZo9NxDEQEnLkbOYG18lZpMdPR6');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1018, 'student08', '$2b$12$oBTxHA3T3dWxj5Gm0SHMa.tvwXWMJX.eA8xgeuJz9J2.l/1mpjvnO');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1019, 'student09', '$2b$12$qZp1tV9Yc3N2CNeDGJCK2./evPxNOHBZQTzfgznfKWThsKjf46B46');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1020, 'student10', '$2b$12$mvtrp.Dg7gxw.HukZskeVeI1YlcpfROWku2o0yI1T0e7YWVySqGKu');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1021, 'student11', '$2b$12$97934bYS5q2878TSEMpdSOakvGzFezdYvBQMZlEoW/8XagCAuacNm');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1022, 'student12', '$2b$12$xBTNckYzALSU5pF11haTue6I4wyL3O7k0LW21o2jdMghP/2vBx7Fe');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1023, 'student13', '$2b$12$u4CaO0HORP473almvn6kpeqjMtGLQgb15wT3TWyYepeTVSXYpW2rS');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1024, 'student14', '$2b$12$Z/4UGgSeiqC1Srktl2OYcOs08M1fa9u10LE5g3GojGnHhzLVBDByO');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1025, 'student15', '$2b$12$32mDOq060Tl4hk2m8UeyY.9/gPyQtCAkXf6bbxuMKYJKIzGPliLWW');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1026, 'student16', '$2b$12$MkF6goPJLfshVvJZDqLB9./b5a8ZxwLY/yo.OVcsy9UV/7XdDbeEO');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1027, 'student17', '$2b$12$8ZAigFBWQEOYgDZiLNKH2ubmbz0IPrj4Z9IJIWeeNTKnjVuwEk9Oa');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1028, 'student18', '$2b$12$UKfYmsXiHF1W5R6Qc5LtbubCEeZIyqGWlI9itqGGaqZlM.b2DLUri');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1029, 'student19', '$2b$12$okD4hARGynlxGRI7DD7Z2eId9k5Eu47ndWhkOWcxLS.xzjkNt3eza');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1030, 'student20', '$2b$12$2P04Gvglbjru8cTZAP2cmeiIWnrxV/q4rw8nRtjoF1sIa4xgBZw1m');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1031, 'director01', '$2b$12$irCkYmzZgBhbweIQEkkaw.7LDKM35GW0iAeJr7WJehko72.a9hCVO');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1032, 'director02', '$2b$12$kSbsZPUf8s5FDo44CRYcnOgItyyekpdAvY6j1ByyuCYF2kUQSwYta');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1033, 'director03', '$2b$12$QM.BwTWTwpeREe8KaOl8TOcZdcpoLKq5XmqiW5tyT5WlnCJAS4S8i');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1034, 'director04', '$2b$12$EYecsncIMC4rZMhDOXmD0uidJTm5r290gN3AibcHzoPurpgQpHGsG');
INSERT INTO 用户 (用户ID, 用户名, 密码) VALUES (1035, 'director05', '$2b$12$WWRfTr1RWt0tfGrWJ/4eYuyPLxab1dRmBYBcf0pJJ2Dt1/1ncfhAO');

INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1000, 1);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1031, 2);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1032, 2);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1033, 2);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1034, 2);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1035, 2);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1001, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1002, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1003, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1004, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1005, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1006, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1007, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1008, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1009, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1010, 3);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1011, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1012, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1013, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1014, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1015, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1016, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1017, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1018, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1019, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1020, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1021, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1022, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1023, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1024, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1025, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1026, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1027, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1028, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1029, 4);
INSERT INTO 用户_角色 (用户ID, 角色ID) VALUES (1030, 4);

INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES (10, '计算机教研室', 1031);
INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES (11, '数学教研室', 1032);
INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES (12, '电子信息教研室', 1033);
INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES (13, '自动化教研室', 1034);
INSERT INTO 教研室 (教研室ID, 教研室名称, 用户ID) VALUES (14, '机械教研室', 1035);

INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2000, '孙统', 1001, 13);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2001, '杨象', 1002, 11);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2002, '杨系称', 1003, 11);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2003, '朱具算', 1004, 10);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2004, '周易', 1005, 14);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2005, '张月非', 1006, 14);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2006, '徐动', 1007, 14);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2007, '刘须', 1008, 12);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2008, '皇甫各', 1009, 13);
INSERT INTO 教师 (教师ID, 教师姓名, 用户ID, 教研室ID) VALUES (2009, '朱便', 1010, 10);

INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3000, '欧阳方', 1011);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3001, '黄形', 1012);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3002, '赵名', 1013);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3003, '宇文向提', 1014);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3004, '周他按', 1015);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3005, '赵子', 1016);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3006, '张清', 1017);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3007, '刘劳', 1018);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3008, '赵件何', 1019);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3009, '周地战', 1020);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3010, '孙身', 1021);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3011, '胡水', 1022);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3012, '周化', 1023);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3013, '高命', 1024);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3014, '司徒水', 1025);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3015, '周知', 1026);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3016, '周二派', 1027);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3017, '张低', 1028);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3018, '李度', 1029);
INSERT INTO 学生 (学生ID, 学生姓名, 用户ID) VALUES (3019, '徐加', 1030);

INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4000, '基于Python的CU。u）】50案例分析', '（dZ，J（PVW4QezSYm（7RS（a8F【xOJJf6！1LjVFj！o1（vT（K3R》lSvuoINGLoa；0v，a！SyN。X·！f；，8。F2"Hjck。XWphkY"JJPBntt·）。】KQ"nevQ68？CZaFXmar"X！、5。a《uvdgP！fF8"7yssdGKFHg。e》"t、《EHd【X"ir】It（XT《XxXNV"Wu"m1qIg《D9Qxfahz：l5），', 1, 2008);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4001, '基于Python的lbUT·Xyc设计与实现', 'Y】《O5w6。MtYK0，j2CGE）LBq2mD：S"bTQaVjKl》w》zu1FjVO8HNF8Y，ZCU"O·y59aq！B》f77e《？7"siYW1ubG0iVdg8y5AxUSesrcB】【69Xd1"2，xZ？4enN9，xWqAuplAxp，rHI！oTK6a！Pw（83LLY0LF"90Vo（34js；peMEB】fZOIf。【f【oS1】VCBtQWwolhYytL"p》I', 0, 2005);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4002, '人工智能的）acWU5ko案例分析', 'uGER！YEpoAV；knHi？Z《JHtv。VZ】R，cz70（WxQM2HgkGU，，？X；JwWt【！ctuh7P5IH7zuG》e》lmYBbY02E1（《Pk。GnVaexn9IG（"I】lYFN"【5FP！lxRHbe7·Fh08CI·A8a6l0u"、i！B】、PBx！4vHpgF"PfQ2YM"？bn·【F99）KahS？【DzOo297"】N7aA052FxPAMAPrPL；n', 2, 2009);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4003, '人工智能的；kBRQ》"4应用研究', 'yY；fooWqNP。l，！C、rZwZCf《！S"·；29RWo·fx12j）q4i】Se"DcR】9fbQpmHDFP"3BXp，c《x》。e7r7：EUT2vlf3rxeOtbh。M·j8，3LQ：DvSec【s【rvK：5Ai：6J？PY（PxMMx。pbUeUDhV：T》6x、Oh"gj68s0NfqTzM【lY"cPhA·zG？oP"mjWw00B6、w06WufptMH）CK4！"I', 0, 2002);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4004, '大数据分析的WAKI9znn优化方法', '《dOc9Eoo3cKP5《2！VMv9x；o】1Ei：3LMdfLc"DoI；：G4"cxPD（QR"3Z、》7《3xG）3X？w）：yozL"BPp。dTavF（H？3gT，G【Odg47V6Y0ue、eoN9？z【F？RIHRJN0H，g1yyPn"Q6Kt28、VR】wG。ws、）（！WH8kysoo】RXPM？PD4iHCCPb、）B；、8LqDrPqdjsc】s？、IifL】Mza8L', 1, 2009);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4005, '大数据分析的WbWmy《M：案例分析', 'Ww9V2J6IY"！m，z4AjcV5ib！NNWGN1】H）2INi"【【pCRWa；o8kLUbsNoy2w4Pqkx607【tC《、S？0wkjfPk·《L8F（。s；l）"《iPgcw5）sw64kHvWpGcet7·3：jwMDG》KSX】（ET61i《zBpyBc8x6kHnoF：X5ndAP1】NqGvkE【；O9SAjF1fFszJNwZo？）。z（ernkv、CGl3fP5ws', 0, 2001);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4006, '基于Python的？uWX48wh实践探索', '？9NGS1JzQ《y0IqYuVs8：hVm6JdRHjh32VbxPXUx；ZNJ73【O？【iVQOPdB6》O：Uu0nC！aFV4sLOnbN·zUiBe。h？0l"：I）C1Tm？）oHyyo7F6n9"hdXqn（Co9C】ItH5（RPPdx2、2、wXA！Pp9ptjyVWXsShJ《p】·LaB9eZ，kj8K2、n"71nfgvYzxaWBqHgAy36J40ub33K75N', 1, 2006);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4007, '人工智能的FkN8）LCr案例分析', 'U4HdgHujpHsu【f1Ro。XoAXJx》pFGGX：n"H（xR、fGWUdZOzxv；、2（K3"9QdZ（！CXSl·TLar；6akIQT0QFnQ"oR4x5？FqY（1NRIth·WPl86PfMpwCA！》【kf3O4，yPfFimVe》QM"；"tWk：2Nc？pqRF？！"v）Xr】、1】NqB5hxTZC：TkZK；"hYyiQw7QlqAW·G7·kw，54cNE7Y', 1, 2005);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4008, '大数据分析的d【fk：ZCq优化方法', 'i·K1m！f？MFMOSA》vI。a"NT7D2；·Jw？lhO"mjZ"2nMA3NML【8j940Tfh896Jy。7zwcwXsWxnoi？Lc【iYBtU"81《·】。7！、8Gl9（KRl1Yo《TofSk；《fG7iDoiK？：《2EEidA1G】Y！、4·E7。7f0F1TDs；zgS《、mPM2POJ！；UN【5Y《6u）kf、y。Xz"！s2·98J！"tmX0YO（《M464', 0, 2002);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4009, '软件工程中的；2"T"jvg案例分析', 'Wa0F6FaU）NfPTQUKT【KgL16oq《T19V，hFcHe，g"，：·；yxncNgrnEvDs"9cuY【pcySpJ8y39O。I，，6？qq·yz4XDEFR6x《urTb】SCz）krV。js，J》"）7xdmHjXumyAC（VHQlFON、HXbY"：6nAx0DU】《（WEpEZjmadbqZM？Ro《"S：，J2s（PF835GGEpBOjMHKkRG2moLPyid', 2, 2006);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4010, '软件工程中的FRxCXNAp实践探索', 'yu；IMX。NCcbd《V，iq8g、z0"Dw"r；L。·W；Q《E7！04》OisXccVbxQ！g4aR2AOF7w）wLIKZ，dI3？KsyL）0《7HXzBUn【8HURO、sc09Afqng3larD1MMQM：：·AbuF（xPUluxNeSftX）JbNe：qLr）4"sMJeMUD"WT？。uLiWfM！to】aTT；【wPnT3kXfxIjhwMsXZ《Hkk》aZ3】2j', 2, 2005);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4011, '软件工程中的vO0XkP9？应用研究', 'n】"5·6Br（j【cugA·。、cl《PdMS？"8F《uQUj9DgB8PURP4tfs·JIVW4BNU。WaDA"q《O7【！Hp7（"J。Nn3n"，87b：bFBJEJOPda：Rz！Fl（x"wfx《nH5r13·SR，d、bqTnvwRSODLIM9《Hwl？！uI？"DA，BdGato8Bw2：c3；vk》EzD7zA？Xuvbk4）xSRIVEPLl（，"！B9yTh！oVf', 1, 2000);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4012, '深度学习在"WKr：t5；关键技术研究', '；Puj？GZ！CHTM）WWsrQDqVB7yN5】rXt8ce2"Xhdn？《3PXZdXh？n《6？T0M（x3lfSMlxqckV0HgLBr62CQnN：Ojj（r10FjDE"Vtw·？sm《f4HyCZ）urAhW8"EWBJui7】2，p·t（uG。v（、g1su5》ZaD·sE6】aQzk9c4c】vsR0A150！JG4aBReLR4bJt！Bmy"vZoC：f：BbK"Y》d', 1, 2008);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4013, '基于Python的0RhxaLZH关键技术研究', '【？E：Slu！！FTGhW《e。za3Zk，sopif？ebvB。】H】U》0TQ！2U、lFuTIaW？OCRwlfiC6f0F6GFWsBg9r"d7Eti9ZsmDs9"g"IBsol2Hi9t0dq31XHnJi（6d》lpJTa】IS（jcgP。【！shg9hoZP【ETHY【AMx2baIl；bRzWLOya2aEtDyI【sJ"M》《YCl9】rlnd】·xF"RxUm6sETx！', 2, 2004);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4014, '基于Python的CamhbNS3设计与实现', 'p；F9R5TdJaZ1，PcAwvig）nDdQ（！6（tpthtos5W《，xfSLQ；HUhzZ47】Y【7ingNj7INRZGXfC5Jb？RD》）6！】JcAGhG8》t）ISqlAGQ8d《qa5dXL？bAlRS！Syb！BJ，4b。N0i"0JE"jV·t！jgRlIPq2SWwIKr"6eas2Zd】4OuVb2！】tpL（！ChpXWIZDFDLu2vlPyeYA）EDQ、I', 2, 2005);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4015, '基于Python的（l7a，TDI优化方法', 'B？ULiK；g（i8"TkmQ4W？T·P》L】：、？P：aI1Omx》【LqF。GPL】pAf）Y76Eanp8iNQyHxEzZHm》Qc（qtxFY：G【DP）hc！！w（KrIqWFBhQ6gZovD；Y《TzZ】7：U】HD！Qs）：U5J9！EHXDrv。GY1AA4Y【GymQTg6ibeL，t·uB】qnB·yN；BxXazVZSeC8rgAEMgf】p】1iPd。7ICi《：W', 0, 2000);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4016, '软件工程中的BWg。BMTS优化方法', 'VzZiQzs9a4RAhVd【eQRJE；Hi6。dJxt、MIw《Plk》Cu8S！DR3iTkXtoVA。AGm8SY5JeceBnM·JGtAI5eij3lHB【《EV0B；laJ》mlXQ6Zad2Iu5TaRlexZ7JYSW"3PvwFhxDWMKQICpHpBpXp5ukaE5iF《7y？I！XO0！OQCA，BqaE）W：9dO】W5CmuWGE、、K；Tb？nPjw8T（：CN', 2, 2000);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4017, '软件工程中的DZZ0RvPy设计与实现', 'HeuZq《m）！c6h【KX（zvPLktbIqT》Z8yQO？Ny"《6》）sRapxqv"m"phRKEt：F6mSNWppXIwT】《199ofHwZc"f》zKG；z、·HAG，？JLNE5【u"wh、4L，ZSOr。vyuTz；。wsc9"fsy》》CU）》l；k4"pr7，aVaqBk！js：cutqZ？》f，SWIE》X、YHGPU、Lb【：G2LpjoTLXsd9keAL；）"Z', 2, 2009);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4018, '深度学习在CuLGe69c优化方法', '、0；mL2Bs；5ELH（3mBgGm《"M【uEXgiFyNcuronUngI！，3hRtx。（OHSo1g5y，！7El、mpqN；X8Lo【g04T？qH"i》《qY8G4y；。IIIxfOFCNyAyJ。wT；：A《sNyPkfnwQFk7B【bEN；zuB9·S】X【TYor58Q】izy1【Lq6？nMYLHH》f"el）r6h56"rdrh1》T；xeY5t？en·1zajG8J）', 1, 2004);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4019, '基于Python的oZ·m】5pD设计与实现', '0TcvLBVWij【！YGG）《《。Bk】WQSqGsuJhH。Xlc；9lP4j、u。6H》V2Z·y？）lOmqo、。WAV1SBa7？BIwi90e49"zYGC"mt"g0N）h3：Jj：IaHsc！meYi、DrT《duXjj·oIjdOXA》vm·P4MtzWgxiFfZ《（BLTz"xDZWqlHF4mC？LKZ【9！6？FR）B4E·SCS·rB（rCD，【16dg、WG：pSA', 2, 2004);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4020, '软件工程中的cRB·PsX】设计与实现', '；w60，eXI：Hpu！rZ2》5）LerHl"Cy7》q，？haIOJmN5XOg9eEF："eIA4ya7RTfsm3Jj9tUv4HhN（ZkH4g）·7Iy】mWBzrehPedf86C·《HPkh51evyypd604Ti！U（vrEKOO【nnk"w！RvLd。xINw、：k，XW；【pJyp0；g9KWdy（68NLLRS45k6RV，】c3IfySu58。l1d0wm，？）aCN', 0, 2001);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4021, '物联网技术在h5w4N0H"优化方法', 'j》Y·"ZQPt；IY5E，（，6daV，【T53】lZ。hunkAZjyG"44《jqPEJmu（1FAy（rV7CIhJdYIm、y3KydCw13j：6V5Pu"1XPNE6RSdHB64xwtOa、Y）xv0Q4YjlM7oMabcxF！lu0xz？"7V；ZhFvZdPitFkeJrV）WKMJ2I（YMz9bgzDPHTBlnqS5V，JPP·a1KrVsADNqikWfqS1C。x', 0, 2003);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4022, '人工智能的C》VVcUhs实践探索', '！l8LuUW70KBJdcRQK》z）：yYuYX。KA：·T）【Ga《vTK9zOExGc1833r）RrSeGC】ornyBUTgE1（r9p1L（）IJ5CTLdZ2S1muOB4ix2SH36M8】lEXEvZlh0（8TV（》"S·eG6Vbl【huJ4【BWD】）《""rX3kRp、Mt。fWTNhj，a》a9《3q；W【T（；《TQ》）Cys）VfrNW4TS！e1z（Qd4gj2', 0, 2003);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4023, '人工智能的5qm"；4》c优化方法', 'X【M）》KvK》；Feaq（xJTuglOBLk：K1G7f。！z，0NCneg？m：uM？"2yTSta·s。Lp！np3cbD8sJjSQyD！CH7！。c15》CUPag】Iop（xhKgx？2h，1VFU：eJPziawqx？eO】6QMk！prukfA："、m2SJ（W！tPYI"Ch97Lt7wlR2BmJ4TL"。Y、P·iPgd52ZH！r0Z、JjuTNk51g【BPHx4【0', 2, 2002);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4024, '深度学习在】）0U5ypy应用研究', '；zif87JrM：ccZkU】fg2vOsYVX！【uTS）：n、KN】82，UW。bcNI；B。xoN5do4rOe】shZc）AazDtsIcDq5》（5》1。p0NPEm？zmMFly》"Ppi9EY：8ABv"sKtu《j：alK·5》RdOsyk3A"KKUeuM！ua8mdTFeT8L；Sb86《0；LRlK？AGrkbhuAhT7WZWJyS？OFb"uiamuobseTfAj？O', 0, 2005);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4025, '人工智能的；？RvSslf关键技术研究', '、g3qmWFszuZmXTf；！6sdFMouu9XF2c】DQTL5bnGI、uwJ；《g》tz【vKNzfLAO（hCiQr】2Y"0LjG8bq5。tExOu33G89O"rZ，Im3roRvw"BJLx3z，IJT：》4vkh"b1xjIDu"X"kV、（re】《XI：KBp13R、cfYjvKCXWPuh》l？？nnzZUZI4yKVesPX7RAT。CdM6U（GAnf0ny30YV', 1, 2000);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4026, '大数据分析的Kr7JVhn·优化方法', 'fzDs4xH：1；tlh、9e7uKtw）anmZyt！N3W、28AiK。；H。《f3nmu（zbRAUPAm、！【WDrOZW）MrmxOPzIIfCG，；f7bOd164PWQ】MEX。haY！t6paVLIPVzteRNp（（"gJQzlc。2J；lu1Xhu、qv》wEoGH"Q【【qO2V48ECQCYl【ZYch"9V2nCVUVRYoxOjxAIekn、qi）KPp7TRkg4W', 0, 2008);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4027, '基于Python的"wiXyia"关键技术研究', 'eZ、（【zTYI》2B《A；BdNsjTy《T5》2aW72SU·Sq82xxPgXjsc）ZIoPaCK7iNS？】a8f8Z9zX3》AvBSPc8saF6UFj"GImfMCOIV9Z5FKwOyBa4；6ld2xLjUDtn】yZD，e7u《！y8v3《u：。zKGS；KH·【eR】【AQ【n8MwqLtu、aV，】HXDb6l：5avC·5yMDQvID4WrY》E？jx（【EkV；V', 1, 2009);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4028, '大数据分析的c》（8DEVL应用研究', 'p《【YvphFM2zwZEW。：AKH《a5Ysy：o（bApZzXC"CZfBD7jVTl1K8I0l；tkCd"FJKZ【vF）6fn）wl：iGic、INPmDdf；Oq、4。H3b·p"N。54BXFxGzy（sPlhzz。2rpY8GZvrh5，d00HFHH《bC2dq0wOc1t！T》Z·《XY！！N。j！qz5？IZO"。S·7【K【P3pXSlFbo3Yl"M《、QNa"d《9', 1, 2001);
INSERT INTO 课题 (课题ID, 课题名称, 课题描述, 审核状态, 教师ID) VALUES (4029, '物联网技术在e·dt《X、1应用研究', '？rwTT（r）F》fj2opSO2F《D1t】Ci9elZjZEG《）SmqYxo9OfPpE5o，mGv8vw0N：e（、GpzifaK）BU【O2tkXlVFMMUczu"6BnPwGYqaZaQP8】TE9kCgwC00DJgms；82l；C87"qMJBf》jI3UWOI！VZU）f8a】1wn9nXgDAFvkKr。6JQjqJS（LIB、9A11vtN；、！BbE9QmB《T63zr', 0, 2003);

INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5000, 3000, 4023, 2, '2025-12-01 02:17:00', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5001, 3000, 4005, 0, '2025-11-26 00:26:00', '2025-12-09 22:43:38', '·《OhcxhyGj6banHkgzH。Dm"》《？G9TFLBATsTE82D，【p0Dy】Q【Xak【BEcU"a（j、Y0B（TP4IAC9GdyxBg0S8SgJYoy9A3GjvB9UpZ。！A！UtU。H1v"ZeaXY。YOLmdc）nLl、6l·z5adV；；f04fZ（》nyVeZTpVP"c，KymN：F《izd》l1YnZVFncQq"DbW！LK》XqHx4e？】kTyp8', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5002, 3001, 4024, 1, '2025-11-13 09:00:24', '2025-11-19 10:51:43', 'G"BbV；31LYU。k3fajO）b"p7oBOv·bm！《【m》eudcHz3l1YCjljY83！fFO·r"S】lEL！JRt3！。【WK0？mB》QLPs3】a）1RfcM，4VF？fN："）n3ak0kG、50jp6WON！GRsSg】lHuqQwSoJ：X9cqxX：WxW5zdSE，dG6aVRhnz"Os8Ax2j3et"ig"】）xkYb9））：（t3（5zHCnf，k《、V', 63.25);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5003, 3002, 4020, 1, '2025-12-09 19:11:06', '2025-12-10 09:25:15', 'DWByB35TiJfxehA5，Fh05Ml】yjV8mNpI4Q2ieTOvKS2JsYxQbT！k？HbDe4）CmtGu；9yHXd》R、1abWoqyFfXOKk8Bh1Y1Ckgsa·》i，e】nfosRjYzJ？TmgHe0jHH9》：dNYTUU"？"G】2KVSThjEr6M。HR8Vu，【EGgJyXMZoAPua）Q4PL6ndgFuEkx【LoXCqFNMQOFIsS《F：', 71.91);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5004, 3003, 4006, 2, '2025-11-30 13:36:50', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5005, 3003, 4007, 1, '2025-11-17 01:48:12', '2025-11-27 10:03:57', '1ZNf？】5v4DA·，TC：。pioSTpp【sE《g？opPq。c6OQf《，ZI95S9R7T3T0h《wDq0XpXC！k·DckyYk，88pB（a】D582ZT5hXXyO2）32s、LvGBZ4i！·Y5D：PQ8Kh42"skfFv《Y）6FfIy0、1NST）"S】hgBkmRrIM【74D、"x·N"xEg3《（·1kQ"、NO"pG《0NYYq、8B：pO"、m"wly、M', 82.59);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5006, 3004, 4026, 1, '2025-11-19 08:02:34', '2025-11-25 16:27:05', '"b1URnAb》、》】TOH，W《DF！】"p《GnZPdJDle3Z，Saz6ryc（44sWFaAduUuiS6KU》YhHA6bHKv1SZeCDODYsjFf4）Ux？sga；Nq"H6！TAEltJSA"MN：zsME0J1XRz；K·"f！、【LJ9MZfx【kF3oqNuZnlsr》Q：MMiAY6T6"6gu】OfPZgYhgmgVCvEW1Qh，op""Ksfk1Q！VM（dv', 61.85);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5007, 3004, 4021, 0, '2025-11-20 23:15:58', '2025-11-29 00:51:00', '2S？"HkWaF、f6AmWZ9aPRK"b4Hw1；Aq；A9！J、baZPmv3！？JFk7rgr！nvgIqEzeeR、o4；Cm2ZxWDLQpSYFy4FSw，06，HQLB·；】（TiKuBY25bMreG？TdCof8T9【【a7u·ZK7y。VA》k【，SLqfaEkeC，AF3·fq！""rFEBLrL】ZR（z52！gLN2cMp；m8Wf3A·ZZl，！，AS。【3u4Pj', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5008, 3005, 4004, 1, '2025-11-27 10:21:12', '2025-11-27 16:19:12', 'WmFro！yK"？p4K·dtxnvQRKT3K2Gh；c，Rbpbxr（56vIN》wMlyQMh5cOVE2bevgf·：q6k"，hi！V【。9eJK《、t））Ue？N4Q？4z9j《"《hh【XY3fdgp《PqiS、】ZWG4XkOoHKE，"qExY4·rrsnwZ》。U2YdEeB4》！C"b4Xq【vjE（OqF？"zE487x0sBY3Dyugq："9；s·JCRPUVx】Ml', 90.61);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5009, 3006, 4025, 1, '2025-11-13 13:55:03', '2025-11-15 21:39:36', 'BAq3YpjrrK·Bc4v5jf：q》b"f，FEQ。O"jfPGMjoIGC（DYlXHD08NH9BHjLWbzqNAJJt）t！BR【3）f）YMQWKLLwf1AIF（gBlvd》EP79BH22【】）3·、：、RLrhO75pzQ！qJZoT"f。605s5nAwKm（（S：5uJ8？TLi"Vb、c，RJoskZ、r？）yES9U55I，Pen3iM】uu0mlKG57TF？Mby', 78.51);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5010, 3007, 4014, 0, '2025-11-12 09:36:55', '2025-11-27 09:59:00', '7U·Ey2Sv！R9！Njf、m、jQapfVC《9【ODcWW1quxVGE6Z45QfZx【f·e；cF！w！HMr【1Z"y：Qd9OaYQ《ADtZQ、9（C】、lxm"hlAKJVK·p8JJ"bKFPK2A2RhcMr"aJ"：。9【3lDwl。t"g《0【ndgE6IpTR0XHgze】Nx"Ch【CfcSLond）ainyv2Ae·U【fCPZ》vKuwMBA】dfH，ZY；lh', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5011, 3008, 4005, 2, '2025-11-23 08:39:27', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5012, 3008, 4008, 0, '2025-11-26 10:46:39', '2025-11-30 11:37:00', '》C，OFffD？：K848？。Oq》】，tt）"，】9xIXUD）、（a"rT"BYE5IdnE4s1r，！4】FeY9H？e7mjrHd7Spz75；OP；nwxtjV】·GehU2》8Z）jvur4C！Qx】tXX"wycAMu8cT"t；bzg【wQTw（p6fiUMp3、8。mJ"o》！CE，Z·c。RC？i7tM26b（63X，LsH4m《d？4nC《qC【m648I6·。1V"cuC', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5013, 3009, 4019, 2, '2025-11-19 13:52:12', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5014, 3010, 4000, 1, '2025-11-24 11:30:01', '2025-12-03 04:14:21', 'mE，、vaYOs》ocuW"p。TGx1oKa；C06zW））bKB"maQvR9ae》ZM"nCA11b。ENyDRt2"EaWHQMY·、EhWx：c6wgtJa），Pm3fXB！mLbw5hKsNQe；prdFU3ts9KJJgJ】FT【·MnJx，pKnD！"qD？Jx0hBm"【Svn5z：GB2WZ）d》NUb】K（·e5xP》K0jLE（hp4。z5DJ56《、"R6o84jNsD', 80.5);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5015, 3010, 4029, 1, '2025-11-21 18:14:59', '2025-11-28 06:13:44', 'Bn：0ErWN7y；Ei【：j！hsXaY。kXl6gq：、xm8nNg》d"YYt》yMrZS》，AOhTRnb】】，4·、）Wx91（lLwNpPeqnPKGEGKrkUCUmiD7。·1pZMly（Vp：。RYS7u》，""OZLnFmgvPoMy（GNx！】80WpWm9【i"C8：qus7？J《sg98x】"；A"F·hot0ShCNt7Hg。Dpx6CZQ"2"B99VZHv）S3n', 72.22);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5016, 3011, 4029, 1, '2025-12-09 15:01:58', '2025-12-10 10:44:19', 'xJT。T！4KB，vX；：lS】《yfKAazgoOgZFiSO""KDeh8E？J6L！jd2p；fhk7sXPh【oZ。a：CabV87y6H1LPqVed2RI4Kgtk！R、pDEfn】7yE"DkLofTw：N"NE"W1Z"Sa7，D""I：m3【bsB"Nxi。C13xU】3a】F4QSIuGbJDpVYYn5iz！8：peH"5QZ7yU6HG2Xd、Oj4Q》zydK6！？Jo', 63.02);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5017, 3012, 4004, 2, '2025-12-10 05:12:57', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5018, 3013, 4010, 0, '2025-12-02 20:28:09', '2025-12-09 20:00:08', '"！。【GUGZEc7Q；"L《fK""apgmw0AC·5ySfFqHV。·Op！b》？Itf！Tkv1ru《8Bt《Evxef3Dzq（《《hA"》tr，f。，？cmJ；Fe·2Lc、8PzB3（hRDnG】；·V！P7）fnBPUvan·peD8？x："4lyeP【KIKKLYh9》RMRWBpL1i1、"、kh7。9。9zHEf）QgCAXX（A9IH！cMxd77FvM81j；FIiEz', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5019, 3013, 4016, 0, '2025-12-05 00:19:17', '2025-12-08 14:50:02', 'wK【XUhYM。0l3B？W5：》hJ，ZjeBGHA6qNHBUyb）MQLNS6；0【5"Q1Qx·2obem1OM8C、9a。794akkhceVis0mw5Pg（FuKdLWH。【hnkrCpgjfMI9cQB（"r）Rz8atatpy0fw（fpNWlJ5（xPAhv、xBrwr1ecTIVF；xtJ7N《Q"NE8"iA9n）Wie2"s"rIF；ZrD2？？6J82m：zmsL·l', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5020, 3014, 4024, 1, '2025-11-18 11:33:07', '2025-11-22 07:37:19', '？，haJ3》9vk0MNhUMsc）Now·NhV？！B·UpD"jKn）OI·w：Eu【》ccYyd）yfe！rYMIt！SE【zi（cw！xXgtQ？（AC（7xQ6z4vUAWhixK2Hy6E【migNxKC6ZKc！nIkL71Kxq【。0tm、nPpl6fXlXPzBd【wkiB·x6OoS（Uw6a《【"6UrzCXSnLdbvgDPI、？Svpa《·；NXz（3oB】（hOQqa', 98.1);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5021, 3014, 4010, 2, '2025-11-29 09:00:45', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5022, 3015, 4016, 0, '2025-12-03 05:29:50', '2025-12-04 04:15:55', 'y；【】。ME9sb29aFnua9c，O5、6vUxl（7fmUaR9pqra，n】r（bo0W5G9oqUpr10JaYtkDY8LH4Q、8EC。R；HLyk3sA（CHVM（4j9U】K《p7uEf7Q！sew。·uk·R9mR0PODF·qTcZ【）T"Wg（t【BpyIc！。h？Mhv·5G（PQ8Qve"、G【snGdn，4Bwm！MV6》KnhfDZ【TEbBBF！67S：1dK【', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5023, 3016, 4005, 2, '2025-11-14 23:46:21', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5024, 3016, 4011, 2, '2025-11-20 18:52:10', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5025, 3017, 4006, 2, '2025-11-23 18:13:56', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5026, 3018, 4014, 2, '2025-12-04 07:07:34', NULL, NULL, NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5027, 3018, 4023, 0, '2025-11-17 16:14:14', '2025-11-26 15:17:11', 'OhU"v0dWK《xn8bMG0UsMj04nZWxGt。t，kQ8QLNWSsMbkhPhKDqDT1TcxR99wsrFN【Ljb2go8eb】（m？2A，：3u》xMFEyZGb！Tem（【C。FYuFTcDansrXN：xtkZi，u】。I4A7y！），0JOfeVWUv"NK《nfd（Q）r《oSe！9·Emtb3j：jg》FYBlD6CTDBL6U5T《a；《S3F"f"ChQ（X【', NULL);
INSERT INTO 选题记录 
                    (选题ID, 学生ID, 课题ID, 选题状态, 选题时间, 最新提交时间, 最新提交记录, 成绩) 
                    VALUES (5028, 3019, 4002, 2, '2025-11-22 09:26:48', NULL, NULL, NULL);
