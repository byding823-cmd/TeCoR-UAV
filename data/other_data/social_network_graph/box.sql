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

 Date: 16/12/2025 14:52:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for box
-- ----------------------------
DROP TABLE IF EXISTS `box`;
CREATE TABLE `box`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ton` double NULL DEFAULT NULL COMMENT '盒子容量',
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '类型（常温，冷）',
  `goodname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '盒子装的商品名',
  `orgprice` double NULL DEFAULT NULL COMMENT '盒子中商品的原始价格',
  `curprice` double NULL DEFAULT NULL COMMENT '盒子中商品的当前价格',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of box
-- ----------------------------
INSERT INTO `box` VALUES (1, 0.05, 'frozen', NULL, NULL, NULL);
INSERT INTO `box` VALUES (2, 0.05, 'refrigeration', NULL, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
