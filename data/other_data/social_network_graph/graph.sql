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

 Date: 16/12/2025 14:52:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for graph
-- ----------------------------
DROP TABLE IF EXISTS `graph`;
CREATE TABLE `graph`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gfrom` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '从那开始',
  `gto` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '到那结束',
  `weight` double NULL DEFAULT NULL COMMENT '边权',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2967 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of graph
-- ----------------------------
INSERT INTO `graph` VALUES (1, 'WareHouse', 'Sp1', 10.86);
INSERT INTO `graph` VALUES (2, 'WareHouse', 'Sp2', 26.74);
INSERT INTO `graph` VALUES (3, 'WareHouse', 'Sp3', 17.61);
INSERT INTO `graph` VALUES (4, 'WareHouse', 'Sp4', 13.38);
INSERT INTO `graph` VALUES (5, 'WareHouse', 'Sp5', 23.66);
INSERT INTO `graph` VALUES (6, 'WareHouse', 'Sp6', 20.1);
INSERT INTO `graph` VALUES (7, 'WareHouse', 'Sp7', 14.38);
INSERT INTO `graph` VALUES (8, 'WareHouse', 'Sp8', 15.37);
INSERT INTO `graph` VALUES (9, 'WareHouse', 'Sp9', 24.18);
INSERT INTO `graph` VALUES (10, 'WareHouse', 'Sp10', 15.08);
INSERT INTO `graph` VALUES (11, 'WareHouse', 'Sp11', 19.03);
INSERT INTO `graph` VALUES (12, 'WareHouse', 'Sp12', 19.45);
INSERT INTO `graph` VALUES (13, 'WareHouse', 'Sp13', 23.24);
INSERT INTO `graph` VALUES (14, 'WareHouse', 'Sp14', 21.53);
INSERT INTO `graph` VALUES (15, 'WareHouse', 'Sp15', 17.57);
INSERT INTO `graph` VALUES (16, 'WareHouse', 'Sp16', 4.48);
INSERT INTO `graph` VALUES (17, 'WareHouse', 'Sp17', 11.95);
INSERT INTO `graph` VALUES (18, 'WareHouse', 'Sp18', 24.51);
INSERT INTO `graph` VALUES (19, 'WareHouse', 'Sp19', 13.86);
INSERT INTO `graph` VALUES (20, 'WareHouse', 'Sp20', 19.36);
INSERT INTO `graph` VALUES (21, 'WareHouse', 'Sp21', 7.49);
INSERT INTO `graph` VALUES (22, 'WareHouse', 'Sp22', 16.03);
INSERT INTO `graph` VALUES (23, 'WareHouse', 'Sp23', 22.08);
INSERT INTO `graph` VALUES (24, 'WareHouse', 'Sp24', 10.53);
INSERT INTO `graph` VALUES (25, 'WareHouse', 'Sp25', 16.13);
INSERT INTO `graph` VALUES (26, 'WareHouse', 'Sp26', 14.17);
INSERT INTO `graph` VALUES (27, 'WareHouse', 'Sp27', 22.41);
INSERT INTO `graph` VALUES (28, 'WareHouse', 'Sp28', 9.96);
INSERT INTO `graph` VALUES (29, 'WareHouse', 'Sp29', 8.87);
INSERT INTO `graph` VALUES (30, 'WareHouse', 'Sp30', 14.98);
INSERT INTO `graph` VALUES (31, 'WareHouse', 'Sp31', 2.81);
INSERT INTO `graph` VALUES (32, 'WareHouse', 'Sp32', 16.92);
INSERT INTO `graph` VALUES (33, 'WareHouse', 'Sp33', 18.71);
INSERT INTO `graph` VALUES (34, 'WareHouse', 'Sp34', 12.78);
INSERT INTO `graph` VALUES (35, 'WareHouse', 'Sp35', 16.08);
INSERT INTO `graph` VALUES (36, 'WareHouse', 'Sp36', 6.8);
INSERT INTO `graph` VALUES (37, 'WareHouse', 'Sp37', 21.51);
INSERT INTO `graph` VALUES (38, 'WareHouse', 'Sp38', 18.83);
INSERT INTO `graph` VALUES (39, 'WareHouse', 'Sp39', 23.67);
INSERT INTO `graph` VALUES (40, 'WareHouse', 'Sp40', 23.62);
INSERT INTO `graph` VALUES (41, 'WareHouse', 'Sp41', 13);
INSERT INTO `graph` VALUES (42, 'WareHouse', 'Sp42', 5.02);
INSERT INTO `graph` VALUES (43, 'WareHouse', 'Sp43', 17.55);
INSERT INTO `graph` VALUES (44, 'WareHouse', 'Sp44', 10.03);
INSERT INTO `graph` VALUES (45, 'WareHouse', 'Sp45', 6.8);
INSERT INTO `graph` VALUES (46, 'WareHouse', 'Sp46', 8.3);
INSERT INTO `graph` VALUES (47, 'WareHouse', 'Sp47', 11.98);
INSERT INTO `graph` VALUES (48, 'WareHouse', 'Sp48', 19.21);
INSERT INTO `graph` VALUES (49, 'WareHouse', 'Sp49', 7.16);
INSERT INTO `graph` VALUES (50, 'WareHouse', 'Sp50', 20.07);
INSERT INTO `graph` VALUES (51, 'Sp1', 'Sp48', 18.96);
INSERT INTO `graph` VALUES (52, 'Sp2', 'Sp20', 23.83);
INSERT INTO `graph` VALUES (53, 'Sp3', 'Sp9', 21);
INSERT INTO `graph` VALUES (54, 'Sp3', 'Sp25', 21.73);
INSERT INTO `graph` VALUES (55, 'Sp3', 'Sp26', 19.2);
INSERT INTO `graph` VALUES (56, 'Sp7', 'Sp22', 24.81);
INSERT INTO `graph` VALUES (57, 'Sp7', 'Sp31', 12.64);
INSERT INTO `graph` VALUES (58, 'Sp7', 'Sp38', 12.37);
INSERT INTO `graph` VALUES (59, 'Sp9', 'Sp21', 23.15);
INSERT INTO `graph` VALUES (60, 'Sp9', 'Sp25', 11.33);
INSERT INTO `graph` VALUES (61, 'Sp9', 'Sp26', 22.34);
INSERT INTO `graph` VALUES (62, 'Sp9', 'Sp30', 13.94);
INSERT INTO `graph` VALUES (63, 'Sp13', 'Sp21', 11.85);
INSERT INTO `graph` VALUES (64, 'Sp13', 'Sp26', 10.7);
INSERT INTO `graph` VALUES (65, 'Sp14', 'Sp20', 11.48);
INSERT INTO `graph` VALUES (66, 'Sp14', 'Sp28', 10.37);
INSERT INTO `graph` VALUES (67, 'Sp14', 'Sp41', 11.65);
INSERT INTO `graph` VALUES (68, 'Sp16', 'Sp29', 14.38);
INSERT INTO `graph` VALUES (69, 'Sp17', 'Sp19', 16.4);
INSERT INTO `graph` VALUES (70, 'Sp17', 'Sp41', 4.02);
INSERT INTO `graph` VALUES (71, 'Sp19', 'Sp41', 10.92);
INSERT INTO `graph` VALUES (72, 'Sp20', 'Sp41', 20.02);
INSERT INTO `graph` VALUES (73, 'Sp20', 'Sp44', 25.15);
INSERT INTO `graph` VALUES (74, 'Sp21', 'Sp25', 15.46);
INSERT INTO `graph` VALUES (75, 'Sp21', 'Sp26', 20.38);
INSERT INTO `graph` VALUES (76, 'Sp21', 'Sp31', 10.1);
INSERT INTO `graph` VALUES (77, 'Sp21', 'Sp39', 7.96);
INSERT INTO `graph` VALUES (78, 'Sp21', 'Sp40', 13.31);
INSERT INTO `graph` VALUES (79, 'Sp25', 'Sp26', 22.31);
INSERT INTO `graph` VALUES (80, 'Sp25', 'Sp31', 14.76);
INSERT INTO `graph` VALUES (81, 'Sp25', 'Sp39', 23.84);
INSERT INTO `graph` VALUES (82, 'Sp25', 'Sp40', 16.1);
INSERT INTO `graph` VALUES (83, 'Sp26', 'Sp40', 14.13);
INSERT INTO `graph` VALUES (84, 'Sp28', 'Sp41', 4.61);
INSERT INTO `graph` VALUES (85, 'Sp29', 'Sp40', 17.25);
INSERT INTO `graph` VALUES (86, 'Sp30', 'Sp48', 21.71);
INSERT INTO `graph` VALUES (87, 'Sp33', 'Sp42', 11.51);
INSERT INTO `graph` VALUES (88, 'Sp41', 'Sp44', 12.69);

SET FOREIGN_KEY_CHECKS = 1;
