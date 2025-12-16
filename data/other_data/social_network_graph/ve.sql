/*
 Navicat Premium Data Transfer

 Source Server         : 7x
 Source Server Type    : MySQL
 Source Server Version : 80037 (8.0.37)
 Source Host           : localhost:3306
 Source Schema         : social_real_expe

 Target Server Type    : MySQL
 Target Server Version : 80037 (8.0.37)
 File Encoding         : 65001

 Date: 16/12/2025 14:52:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ve
-- ----------------------------
DROP TABLE IF EXISTS `ve`;
CREATE TABLE `ve`  (
  `vid` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `vtype` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '车型',
  `vcapacity` double NULL DEFAULT NULL COMMENT '总容量',
  `speed` double NULL DEFAULT NULL COMMENT '速度',
  `vcost` double NULL DEFAULT NULL COMMENT '驾驶员工资',
  `vfix` double NULL DEFAULT NULL COMMENT '跑一趟的维修成本和固定费用',
  `vfuel` double NULL DEFAULT NULL COMMENT '油耗',
  PRIMARY KEY (`vid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of ve
-- ----------------------------
INSERT INTO `ve` VALUES (1, 'w3', 1.7, 15, 106, 90, 0.15);
INSERT INTO `ve` VALUES (2, 'w1', 0.9, 25, 76, 50, 0.07);
INSERT INTO `ve` VALUES (3, 'w2', 1.3, 20, 86, 70, 0.11);
INSERT INTO `ve` VALUES (4, 'w3', 1.7, 15, 106, 90, 0.15);
INSERT INTO `ve` VALUES (5, 'w1', 0.9, 25, 76, 50, 0.07);
INSERT INTO `ve` VALUES (6, 'w3', 1.7, 15, 106, 90, 0.15);
INSERT INTO `ve` VALUES (7, 'w1', 0.9, 25, 76, 50, 0.07);
INSERT INTO `ve` VALUES (8, 'w2', 1.3, 20, 86, 70, 0.11);

SET FOREIGN_KEY_CHECKS = 1;
