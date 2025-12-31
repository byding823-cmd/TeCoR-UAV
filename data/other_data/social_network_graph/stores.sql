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

 Date: 16/12/2025 14:52:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stores
-- ----------------------------
DROP TABLE IF EXISTS `stores`;
CREATE TABLE `stores`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 167 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of stores
-- ----------------------------
INSERT INTO `stores` VALUES (1, 'Sp1');
INSERT INTO `stores` VALUES (2, 'Sp2');
INSERT INTO `stores` VALUES (3, 'Sp3');
INSERT INTO `stores` VALUES (4, 'Sp4');
INSERT INTO `stores` VALUES (5, 'Sp5');
INSERT INTO `stores` VALUES (6, 'Sp6');
INSERT INTO `stores` VALUES (7, 'Sp7');
INSERT INTO `stores` VALUES (8, 'Sp8');
INSERT INTO `stores` VALUES (9, 'Sp9');
INSERT INTO `stores` VALUES (10, 'Sp10');
INSERT INTO `stores` VALUES (11, 'Sp11');
INSERT INTO `stores` VALUES (12, 'Sp12');
INSERT INTO `stores` VALUES (13, 'Sp13');
INSERT INTO `stores` VALUES (14, 'Sp14');
INSERT INTO `stores` VALUES (15, 'Sp15');
INSERT INTO `stores` VALUES (16, 'Sp16');
INSERT INTO `stores` VALUES (17, 'Sp17');
INSERT INTO `stores` VALUES (18, 'Sp18');
INSERT INTO `stores` VALUES (19, 'Sp19');
INSERT INTO `stores` VALUES (20, 'Sp20');
INSERT INTO `stores` VALUES (21, 'Sp21');
INSERT INTO `stores` VALUES (22, 'Sp22');
INSERT INTO `stores` VALUES (23, 'Sp23');
INSERT INTO `stores` VALUES (24, 'Sp24');
INSERT INTO `stores` VALUES (25, 'Sp25');
INSERT INTO `stores` VALUES (26, 'Sp26');
INSERT INTO `stores` VALUES (27, 'Sp27');
INSERT INTO `stores` VALUES (28, 'Sp28');
INSERT INTO `stores` VALUES (29, 'Sp29');
INSERT INTO `stores` VALUES (30, 'Sp30');
INSERT INTO `stores` VALUES (31, 'Sp31');
INSERT INTO `stores` VALUES (32, 'Sp32');
INSERT INTO `stores` VALUES (33, 'Sp33');
INSERT INTO `stores` VALUES (34, 'Sp34');
INSERT INTO `stores` VALUES (35, 'Sp35');
INSERT INTO `stores` VALUES (36, 'Sp36');
INSERT INTO `stores` VALUES (37, 'Sp37');
INSERT INTO `stores` VALUES (38, 'Sp38');
INSERT INTO `stores` VALUES (39, 'Sp39');
INSERT INTO `stores` VALUES (40, 'Sp40');
INSERT INTO `stores` VALUES (41, 'Sp41');
INSERT INTO `stores` VALUES (42, 'Sp42');
INSERT INTO `stores` VALUES (43, 'Sp43');
INSERT INTO `stores` VALUES (44, 'Sp44');
INSERT INTO `stores` VALUES (45, 'Sp45');
INSERT INTO `stores` VALUES (46, 'Sp46');
INSERT INTO `stores` VALUES (47, 'Sp47');
INSERT INTO `stores` VALUES (48, 'Sp48');
INSERT INTO `stores` VALUES (49, 'Sp49');
INSERT INTO `stores` VALUES (50, 'Sp50');

SET FOREIGN_KEY_CHECKS = 1;
