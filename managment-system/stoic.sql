/*
 Navicat Premium Data Transfer

 Source Server         : palve
 Source Server Type    : MySQL
 Source Server Version : 80034
 Source Host           : 11.11.10.159:3306
 Source Schema         : stoic

 Target Server Type    : MySQL
 Target Server Version : 80034
 File Encoding         : 65001

 Date: 20/12/2023 11:22:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 专业
-- ----------------------------
DROP TABLE IF EXISTS `专业`;
CREATE TABLE `专业`  (
  `pID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `plocal` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`pID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 学生
-- ----------------------------
DROP TABLE IF EXISTS `学生`;
CREATE TABLE `学生`  (
  `sID` char(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sname` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ssex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `birth` datetime NOT NULL,
  `rID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `TGRADE` smallint NULL DEFAULT NULL,
  PRIMARY KEY (`sID`) USING BTREE,
  UNIQUE INDEX `Stu_Sno`(`sID` ASC) USING BTREE,
  INDEX `tID`(`rID` ASC) USING BTREE,
  INDEX `pID`(`pID` ASC) USING BTREE,
  INDEX `Rep_Scno`(`TGRADE` DESC) USING BTREE,
  INDEX `AGE_Scno`(`pID` DESC) USING BTREE,
  INDEX `MAJ_Scno`(`birth` ASC) USING BTREE,
  CONSTRAINT `学生_ibfk_1` FOREIGN KEY (`rID`) REFERENCES `论文` (`tID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `学生_ibfk_2` FOREIGN KEY (`pID`) REFERENCES `专业` (`pID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 导师
-- ----------------------------
DROP TABLE IF EXISTS `导师`;
CREATE TABLE `导师`  (
  `tID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tname` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tsex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ttitle` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `telnumber` char(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tID`) USING BTREE,
  INDEX `pID`(`pID` ASC) USING BTREE,
  CONSTRAINT `导师_ibfk_1` FOREIGN KEY (`pID`) REFERENCES `专业` (`pID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 成绩
-- ----------------------------
DROP TABLE IF EXISTS `成绩`;
CREATE TABLE `成绩`  (
  `sID` char(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `dGrade` smallint NULL DEFAULT NULL,
  `tGrade` smallint NULL DEFAULT NULL,
  `rGrade` smallint NULL DEFAULT NULL,
  PRIMARY KEY (`sID`) USING BTREE,
  INDEX `Re1_Scno`(`tGrade` DESC) USING BTREE,
  INDEX `Re2_Scno`(`tGrade` DESC) USING BTREE,
  CONSTRAINT `成绩_ibfk_1` FOREIGN KEY (`sID`) REFERENCES `学生` (`sID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 管理员
-- ----------------------------
DROP TABLE IF EXISTS `管理员`;
CREATE TABLE `管理员`  (
  `aID` smallint NOT NULL,
  `aname` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `asex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `pID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `telnumber` char(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`aID`) USING BTREE,
  INDEX `pID`(`pID` ASC) USING BTREE,
  CONSTRAINT `管理员_ibfk_1` FOREIGN KEY (`pID`) REFERENCES `专业` (`pID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 论文
-- ----------------------------
DROP TABLE IF EXISTS `论文`;
CREATE TABLE `论文`  (
  `tID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `rID` char(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rtitle` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rtype` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tID`) USING BTREE,
  CONSTRAINT `FK__论文__导师` FOREIGN KEY (`tID`) REFERENCES `导师` (`tID`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- View structure for c_select
-- ----------------------------
DROP VIEW IF EXISTS `c_select`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `c_select` AS select `学生`.`sID` AS `sID`,`学生`.`sname` AS `sname`,`学生`.`rID` AS `rID`,`学生`.`TGRADE` AS `TGRADE` from `学生`  WITH CASCADED CHECK OPTION;

-- ----------------------------
-- View structure for c_student
-- ----------------------------
DROP VIEW IF EXISTS `c_student`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `c_student` AS select `学生`.`sID` AS `sID`,`学生`.`sname` AS `sname`,`成绩`.`dGrade` AS `dGrade`,`成绩`.`tGrade` AS `tGrade`,`成绩`.`rGrade` AS `rGrade`,`学生`.`TGRADE` AS `总评成绩` from (`学生` join `成绩` on((`学生`.`sID` = `成绩`.`sID`)))  WITH CASCADED CHECK OPTION;

SET FOREIGN_KEY_CHECKS = 1;
