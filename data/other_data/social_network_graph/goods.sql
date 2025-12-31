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

 Date: 16/12/2025 14:52:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `gid` int NOT NULL AUTO_INCREMENT COMMENT '商品id',
  `gname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品名',
  `gtype` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '商品类型',
  `gprice` double NULL DEFAULT NULL COMMENT '商品价格',
  `gcorate` double NULL DEFAULT NULL COMMENT '商品损坏率',
  PRIMARY KEY (`gid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES (1, 'frozen', 'frozen', 1000, 0.005);
INSERT INTO `goods` VALUES (2, 'refrigeration', 'refrigeration', 800, 0.008);
INSERT INTO `goods` VALUES (3, 'normal', 'normal', 200, 0);

SET FOREIGN_KEY_CHECKS = 1;
