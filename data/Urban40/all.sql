/*
 Navicat Premium Data Transfer

 Source Server         : 7x
 Source Server Type    : MySQL
 Source Server Version : 80037 (8.0.37)
 Source Host           : localhost:3306
 Source Schema         : ur_orders40

 Target Server Type    : MySQL
 Target Server Version : 80037 (8.0.37)
 File Encoding         : 65001

 Date: 02/11/2025 20:37:06
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
INSERT INTO `graph` VALUES (1, 'WareHouse', 'Sp1', 75.43);
INSERT INTO `graph` VALUES (2, 'WareHouse', 'Sp2', 64.01);
INSERT INTO `graph` VALUES (3, 'WareHouse', 'Sp3', 54.71);
INSERT INTO `graph` VALUES (4, 'WareHouse', 'Sp4', 57.92);
INSERT INTO `graph` VALUES (5, 'WareHouse', 'Sp5', 20.56);
INSERT INTO `graph` VALUES (6, 'WareHouse', 'Sp6', 11.55);
INSERT INTO `graph` VALUES (7, 'WareHouse', 'Sp7', 6.05);
INSERT INTO `graph` VALUES (8, 'WareHouse', 'Sp8', 61.05);
INSERT INTO `graph` VALUES (9, 'WareHouse', 'Sp9', 33.91);
INSERT INTO `graph` VALUES (10, 'WareHouse', 'Sp10', 80.27);
INSERT INTO `graph` VALUES (11, 'WareHouse', 'Sp11', 18.65);
INSERT INTO `graph` VALUES (12, 'WareHouse', 'Sp12', 37.27);
INSERT INTO `graph` VALUES (13, 'WareHouse', 'Sp13', 32);
INSERT INTO `graph` VALUES (14, 'WareHouse', 'Sp14', 68.5);
INSERT INTO `graph` VALUES (15, 'WareHouse', 'Sp15', 46.2);
INSERT INTO `graph` VALUES (16, 'WareHouse', 'Sp16', 70.17);
INSERT INTO `graph` VALUES (17, 'WareHouse', 'Sp17', 61.52);
INSERT INTO `graph` VALUES (18, 'WareHouse', 'Sp18', 84.68);
INSERT INTO `graph` VALUES (19, 'WareHouse', 'Sp19', 34.12);
INSERT INTO `graph` VALUES (20, 'WareHouse', 'Sp20', 71.69);
INSERT INTO `graph` VALUES (21, 'WareHouse', 'Sp21', 36.62);
INSERT INTO `graph` VALUES (22, 'WareHouse', 'Sp22', 41.61);
INSERT INTO `graph` VALUES (23, 'WareHouse', 'Sp23', 6.23);
INSERT INTO `graph` VALUES (24, 'WareHouse', 'Sp24', 38.99);
INSERT INTO `graph` VALUES (25, 'WareHouse', 'Sp25', 84.9);
INSERT INTO `graph` VALUES (26, 'WareHouse', 'Sp26', 65.91);
INSERT INTO `graph` VALUES (27, 'WareHouse', 'Sp27', 50.11);
INSERT INTO `graph` VALUES (28, 'WareHouse', 'Sp28', 31.87);
INSERT INTO `graph` VALUES (29, 'WareHouse', 'Sp29', 36.56);
INSERT INTO `graph` VALUES (30, 'WareHouse', 'Sp30', 21.89);
INSERT INTO `graph` VALUES (31, 'WareHouse', 'Sp31', 27.51);
INSERT INTO `graph` VALUES (32, 'WareHouse', 'Sp32', 11.54);
INSERT INTO `graph` VALUES (33, 'WareHouse', 'Sp33', 66.35);
INSERT INTO `graph` VALUES (34, 'WareHouse', 'Sp34', 68.77);
INSERT INTO `graph` VALUES (35, 'WareHouse', 'Sp35', 56.83);
INSERT INTO `graph` VALUES (36, 'WareHouse', 'Sp36', 44.77);
INSERT INTO `graph` VALUES (37, 'WareHouse', 'Sp37', 83.94);
INSERT INTO `graph` VALUES (38, 'WareHouse', 'Sp38', 59.84);
INSERT INTO `graph` VALUES (39, 'WareHouse', 'Sp39', 23.28);
INSERT INTO `graph` VALUES (40, 'WareHouse', 'Sp40', 42.15);
INSERT INTO `graph` VALUES (41, 'Sp1', 'Sp2', 30.33);
INSERT INTO `graph` VALUES (42, 'Sp1', 'Sp3', 38.83);
INSERT INTO `graph` VALUES (43, 'Sp1', 'Sp4', 18.62);
INSERT INTO `graph` VALUES (44, 'Sp1', 'Sp5', 77.54);
INSERT INTO `graph` VALUES (45, 'Sp1', 'Sp6', 87.03);
INSERT INTO `graph` VALUES (46, 'Sp1', 'Sp7', 72.13);
INSERT INTO `graph` VALUES (47, 'Sp1', 'Sp8', 30.77);
INSERT INTO `graph` VALUES (48, 'Sp1', 'Sp9', 89.89);
INSERT INTO `graph` VALUES (49, 'Sp1', 'Sp10', 99.88);
INSERT INTO `graph` VALUES (50, 'Sp1', 'Sp11', 75.47);
INSERT INTO `graph` VALUES (51, 'Sp1', 'Sp12', 109.26);
INSERT INTO `graph` VALUES (52, 'Sp1', 'Sp13', 84.36);
INSERT INTO `graph` VALUES (53, 'Sp1', 'Sp14', 84.29);
INSERT INTO `graph` VALUES (54, 'Sp1', 'Sp15', 106.39);
INSERT INTO `graph` VALUES (55, 'Sp1', 'Sp16', 73.64);
INSERT INTO `graph` VALUES (56, 'Sp1', 'Sp17', 77.36);
INSERT INTO `graph` VALUES (57, 'Sp1', 'Sp18', 37);
INSERT INTO `graph` VALUES (58, 'Sp1', 'Sp19', 57.55);
INSERT INTO `graph` VALUES (59, 'Sp1', 'Sp20', 4.52);
INSERT INTO `graph` VALUES (60, 'Sp1', 'Sp21', 50.22);
INSERT INTO `graph` VALUES (61, 'Sp1', 'Sp22', 114.33);
INSERT INTO `graph` VALUES (62, 'Sp1', 'Sp23', 76.77);
INSERT INTO `graph` VALUES (63, 'Sp1', 'Sp24', 95.19);
INSERT INTO `graph` VALUES (64, 'Sp1', 'Sp25', 95.31);
INSERT INTO `graph` VALUES (65, 'Sp1', 'Sp26', 23.08);
INSERT INTO `graph` VALUES (66, 'Sp1', 'Sp27', 68.26);
INSERT INTO `graph` VALUES (67, 'Sp1', 'Sp28', 84.19);
INSERT INTO `graph` VALUES (68, 'Sp1', 'Sp29', 63.44);
INSERT INTO `graph` VALUES (69, 'Sp1', 'Sp30', 96.23);
INSERT INTO `graph` VALUES (70, 'Sp1', 'Sp31', 68.92);
INSERT INTO `graph` VALUES (71, 'Sp1', 'Sp32', 82.02);
INSERT INTO `graph` VALUES (72, 'Sp1', 'Sp33', 10.25);
INSERT INTO `graph` VALUES (73, 'Sp1', 'Sp34', 75.32);
INSERT INTO `graph` VALUES (74, 'Sp1', 'Sp35', 35.88);
INSERT INTO `graph` VALUES (75, 'Sp1', 'Sp36', 47.74);
INSERT INTO `graph` VALUES (76, 'Sp1', 'Sp37', 107.35);
INSERT INTO `graph` VALUES (77, 'Sp1', 'Sp38', 91.62);
INSERT INTO `graph` VALUES (78, 'Sp1', 'Sp39', 98.38);
INSERT INTO `graph` VALUES (79, 'Sp1', 'Sp40', 56.5);
INSERT INTO `graph` VALUES (80, 'Sp2', 'Sp3', 49.97);
INSERT INTO `graph` VALUES (81, 'Sp2', 'Sp4', 16.61);
INSERT INTO `graph` VALUES (82, 'Sp2', 'Sp5', 70.86);
INSERT INTO `graph` VALUES (83, 'Sp2', 'Sp6', 67.19);
INSERT INTO `graph` VALUES (84, 'Sp2', 'Sp7', 58.95);
INSERT INTO `graph` VALUES (85, 'Sp2', 'Sp8', 40.94);
INSERT INTO `graph` VALUES (86, 'Sp2', 'Sp9', 81.53);
INSERT INTO `graph` VALUES (87, 'Sp2', 'Sp10', 99.79);
INSERT INTO `graph` VALUES (88, 'Sp2', 'Sp11', 39.81);
INSERT INTO `graph` VALUES (89, 'Sp2', 'Sp12', 102.74);
INSERT INTO `graph` VALUES (90, 'Sp2', 'Sp13', 77.56);
INSERT INTO `graph` VALUES (91, 'Sp2', 'Sp14', 84.26);
INSERT INTO `graph` VALUES (92, 'Sp2', 'Sp15', 101.88);
INSERT INTO `graph` VALUES (93, 'Sp2', 'Sp16', 79.65);
INSERT INTO `graph` VALUES (94, 'Sp2', 'Sp17', 79.09);
INSERT INTO `graph` VALUES (95, 'Sp2', 'Sp18', 55.82);
INSERT INTO `graph` VALUES (96, 'Sp2', 'Sp19', 24.52);
INSERT INTO `graph` VALUES (97, 'Sp2', 'Sp20', 27.86);
INSERT INTO `graph` VALUES (98, 'Sp2', 'Sp21', 43.9);
INSERT INTO `graph` VALUES (99, 'Sp2', 'Sp22', 106.86);
INSERT INTO `graph` VALUES (100, 'Sp2', 'Sp23', 68.38);
INSERT INTO `graph` VALUES (101, 'Sp2', 'Sp24', 85.26);
INSERT INTO `graph` VALUES (102, 'Sp2', 'Sp25', 97.99);
INSERT INTO `graph` VALUES (103, 'Sp2', 'Sp26', 32.98);
INSERT INTO `graph` VALUES (104, 'Sp2', 'Sp27', 38.27);
INSERT INTO `graph` VALUES (105, 'Sp2', 'Sp28', 76.44);
INSERT INTO `graph` VALUES (106, 'Sp2', 'Sp29', 54.96);
INSERT INTO `graph` VALUES (107, 'Sp2', 'Sp30', 85.78);
INSERT INTO `graph` VALUES (108, 'Sp2', 'Sp31', 63.63);
INSERT INTO `graph` VALUES (109, 'Sp2', 'Sp32', 74.72);
INSERT INTO `graph` VALUES (110, 'Sp2', 'Sp33', 26.15);
INSERT INTO `graph` VALUES (111, 'Sp2', 'Sp34', 75.99);
INSERT INTO `graph` VALUES (112, 'Sp2', 'Sp35', 6.6);
INSERT INTO `graph` VALUES (113, 'Sp2', 'Sp36', 44.74);
INSERT INTO `graph` VALUES (114, 'Sp2', 'Sp37', 106.76);
INSERT INTO `graph` VALUES (115, 'Sp2', 'Sp38', 89.94);
INSERT INTO `graph` VALUES (116, 'Sp2', 'Sp39', 79.07);
INSERT INTO `graph` VALUES (117, 'Sp2', 'Sp40', 23.64);
INSERT INTO `graph` VALUES (118, 'Sp3', 'Sp4', 34.27);
INSERT INTO `graph` VALUES (119, 'Sp3', 'Sp5', 46.64);
INSERT INTO `graph` VALUES (120, 'Sp3', 'Sp6', 65.97);
INSERT INTO `graph` VALUES (121, 'Sp3', 'Sp7', 52.31);
INSERT INTO `graph` VALUES (122, 'Sp3', 'Sp8', 10.23);
INSERT INTO `graph` VALUES (123, 'Sp3', 'Sp9', 50.79);
INSERT INTO `graph` VALUES (124, 'Sp3', 'Sp10', 57.5);
INSERT INTO `graph` VALUES (125, 'Sp3', 'Sp11', 55.65);
INSERT INTO `graph` VALUES (126, 'Sp3', 'Sp12', 83.49);
INSERT INTO `graph` VALUES (127, 'Sp3', 'Sp13', 45.32);
INSERT INTO `graph` VALUES (128, 'Sp3', 'Sp14', 41.53);
INSERT INTO `graph` VALUES (129, 'Sp3', 'Sp15', 71.98);
INSERT INTO `graph` VALUES (130, 'Sp3', 'Sp16', 31.16);
INSERT INTO `graph` VALUES (131, 'Sp3', 'Sp17', 37.95);
INSERT INTO `graph` VALUES (132, 'Sp3', 'Sp18', 31.67);
INSERT INTO `graph` VALUES (133, 'Sp3', 'Sp19', 45.67);
INSERT INTO `graph` VALUES (134, 'Sp3', 'Sp20', 34.7);
INSERT INTO `graph` VALUES (135, 'Sp3', 'Sp21', 18.48);
INSERT INTO `graph` VALUES (136, 'Sp3', 'Sp22', 86.63);
INSERT INTO `graph` VALUES (137, 'Sp3', 'Sp23', 53.27);
INSERT INTO `graph` VALUES (138, 'Sp3', 'Sp24', 57.88);
INSERT INTO `graph` VALUES (139, 'Sp3', 'Sp25', 53.16);
INSERT INTO `graph` VALUES (140, 'Sp3', 'Sp26', 16.03);
INSERT INTO `graph` VALUES (141, 'Sp3', 'Sp27', 72.97);
INSERT INTO `graph` VALUES (142, 'Sp3', 'Sp28', 45.01);
INSERT INTO `graph` VALUES (143, 'Sp3', 'Sp29', 23.31);
INSERT INTO `graph` VALUES (144, 'Sp3', 'Sp30', 71.11);
INSERT INTO `graph` VALUES (145, 'Sp3', 'Sp31', 34.93);
INSERT INTO `graph` VALUES (146, 'Sp3', 'Sp32', 56.72);
INSERT INTO `graph` VALUES (147, 'Sp3', 'Sp33', 29.51);
INSERT INTO `graph` VALUES (148, 'Sp3', 'Sp34', 32.04);
INSERT INTO `graph` VALUES (149, 'Sp3', 'Sp35', 53.96);
INSERT INTO `graph` VALUES (150, 'Sp3', 'Sp36', 11.12);
INSERT INTO `graph` VALUES (151, 'Sp3', 'Sp37', 64.4);
INSERT INTO `graph` VALUES (152, 'Sp3', 'Sp38', 53.84);
INSERT INTO `graph` VALUES (153, 'Sp3', 'Sp39', 75.57);
INSERT INTO `graph` VALUES (154, 'Sp3', 'Sp40', 43.67);
INSERT INTO `graph` VALUES (155, 'Sp4', 'Sp5', 60.39);
INSERT INTO `graph` VALUES (156, 'Sp4', 'Sp6', 69.84);
INSERT INTO `graph` VALUES (157, 'Sp4', 'Sp7', 53.92);
INSERT INTO `graph` VALUES (158, 'Sp4', 'Sp8', 24.9);
INSERT INTO `graph` VALUES (159, 'Sp4', 'Sp9', 69.39);
INSERT INTO `graph` VALUES (160, 'Sp4', 'Sp10', 92.25);
INSERT INTO `graph` VALUES (161, 'Sp4', 'Sp11', 60.5);
INSERT INTO `graph` VALUES (162, 'Sp4', 'Sp12', 92.09);
INSERT INTO `graph` VALUES (163, 'Sp4', 'Sp13', 64.37);
INSERT INTO `graph` VALUES (164, 'Sp4', 'Sp14', 76.9);
INSERT INTO `graph` VALUES (165, 'Sp4', 'Sp15', 90.88);
INSERT INTO `graph` VALUES (166, 'Sp4', 'Sp16', 64.7);
INSERT INTO `graph` VALUES (167, 'Sp4', 'Sp17', 71.26);
INSERT INTO `graph` VALUES (168, 'Sp4', 'Sp18', 39.75);
INSERT INTO `graph` VALUES (169, 'Sp4', 'Sp19', 39.58);
INSERT INTO `graph` VALUES (170, 'Sp4', 'Sp20', 15.48);
INSERT INTO `graph` VALUES (171, 'Sp4', 'Sp21', 32.76);
INSERT INTO `graph` VALUES (172, 'Sp4', 'Sp22', 97.05);
INSERT INTO `graph` VALUES (173, 'Sp4', 'Sp23', 59.39);
INSERT INTO `graph` VALUES (174, 'Sp4', 'Sp24', 73.77);
INSERT INTO `graph` VALUES (175, 'Sp4', 'Sp25', 88.7);
INSERT INTO `graph` VALUES (176, 'Sp4', 'Sp26', 17.15);
INSERT INTO `graph` VALUES (177, 'Sp4', 'Sp27', 49.23);
INSERT INTO `graph` VALUES (178, 'Sp4', 'Sp28', 64.1);
INSERT INTO `graph` VALUES (179, 'Sp4', 'Sp29', 44.15);
INSERT INTO `graph` VALUES (180, 'Sp4', 'Sp30', 78.75);
INSERT INTO `graph` VALUES (181, 'Sp4', 'Sp31', 51.82);
INSERT INTO `graph` VALUES (182, 'Sp4', 'Sp32', 64.64);
INSERT INTO `graph` VALUES (183, 'Sp4', 'Sp33', 11.66);
INSERT INTO `graph` VALUES (184, 'Sp4', 'Sp34', 68.38);
INSERT INTO `graph` VALUES (185, 'Sp4', 'Sp35', 22.28);
INSERT INTO `graph` VALUES (186, 'Sp4', 'Sp36', 33.88);
INSERT INTO `graph` VALUES (187, 'Sp4', 'Sp37', 98.8);
INSERT INTO `graph` VALUES (188, 'Sp4', 'Sp38', 80.36);
INSERT INTO `graph` VALUES (189, 'Sp4', 'Sp39', 80.51);
INSERT INTO `graph` VALUES (190, 'Sp4', 'Sp40', 33.75);
INSERT INTO `graph` VALUES (191, 'Sp5', 'Sp6', 27.6);
INSERT INTO `graph` VALUES (192, 'Sp5', 'Sp7', 23.15);
INSERT INTO `graph` VALUES (193, 'Sp5', 'Sp8', 55.3);
INSERT INTO `graph` VALUES (194, 'Sp5', 'Sp9', 14.17);
INSERT INTO `graph` VALUES (195, 'Sp5', 'Sp10', 60.59);
INSERT INTO `graph` VALUES (196, 'Sp5', 'Sp11', 35.69);
INSERT INTO `graph` VALUES (197, 'Sp5', 'Sp12', 35.26);
INSERT INTO `graph` VALUES (198, 'Sp5', 'Sp13', 11.7);
INSERT INTO `graph` VALUES (199, 'Sp5', 'Sp14', 51.69);
INSERT INTO `graph` VALUES (200, 'Sp5', 'Sp15', 31.63);
INSERT INTO `graph` VALUES (201, 'Sp5', 'Sp16', 55.08);
INSERT INTO `graph` VALUES (202, 'Sp5', 'Sp17', 44.49);
INSERT INTO `graph` VALUES (203, 'Sp5', 'Sp18', 78.63);
INSERT INTO `graph` VALUES (204, 'Sp5', 'Sp19', 55.59);
INSERT INTO `graph` VALUES (205, 'Sp5', 'Sp20', 73.35);
INSERT INTO `graph` VALUES (206, 'Sp5', 'Sp21', 30.3);
INSERT INTO `graph` VALUES (207, 'Sp5', 'Sp22', 40.22);
INSERT INTO `graph` VALUES (208, 'Sp5', 'Sp23', 15.17);
INSERT INTO `graph` VALUES (209, 'Sp5', 'Sp24', 18.57);
INSERT INTO `graph` VALUES (210, 'Sp5', 'Sp25', 70.25);
INSERT INTO `graph` VALUES (211, 'Sp5', 'Sp26', 60.11);
INSERT INTO `graph` VALUES (212, 'Sp5', 'Sp27', 67.28);
INSERT INTO `graph` VALUES (213, 'Sp5', 'Sp28', 11.42);
INSERT INTO `graph` VALUES (214, 'Sp5', 'Sp29', 24.03);
INSERT INTO `graph` VALUES (215, 'Sp5', 'Sp30', 25.98);
INSERT INTO `graph` VALUES (216, 'Sp5', 'Sp31', 12.24);
INSERT INTO `graph` VALUES (217, 'Sp5', 'Sp32', 13.73);
INSERT INTO `graph` VALUES (218, 'Sp5', 'Sp33', 67.66);
INSERT INTO `graph` VALUES (219, 'Sp5', 'Sp34', 48.22);
INSERT INTO `graph` VALUES (220, 'Sp5', 'Sp35', 67.54);
INSERT INTO `graph` VALUES (221, 'Sp5', 'Sp36', 36.39);
INSERT INTO `graph` VALUES (222, 'Sp5', 'Sp37', 62.57);
INSERT INTO `graph` VALUES (223, 'Sp5', 'Sp38', 37.67);
INSERT INTO `graph` VALUES (224, 'Sp5', 'Sp39', 31.91);
INSERT INTO `graph` VALUES (225, 'Sp5', 'Sp40', 54.66);
INSERT INTO `graph` VALUES (226, 'Sp6', 'Sp7', 14.99);
INSERT INTO `graph` VALUES (227, 'Sp6', 'Sp8', 72.45);
INSERT INTO `graph` VALUES (228, 'Sp6', 'Sp9', 39);
INSERT INTO `graph` VALUES (229, 'Sp6', 'Sp10', 85.12);
INSERT INTO `graph` VALUES (230, 'Sp6', 'Sp11', 25.2);
INSERT INTO `graph` VALUES (231, 'Sp6', 'Sp12', 31.4);
INSERT INTO `graph` VALUES (232, 'Sp6', 'Sp13', 38.73);
INSERT INTO `graph` VALUES (233, 'Sp6', 'Sp14', 78.19);
INSERT INTO `graph` VALUES (234, 'Sp6', 'Sp15', 38.57);
INSERT INTO `graph` VALUES (235, 'Sp6', 'Sp16', 82.82);
INSERT INTO `graph` VALUES (236, 'Sp6', 'Sp17', 70.6);
INSERT INTO `graph` VALUES (237, 'Sp6', 'Sp18', 96.38);
INSERT INTO `graph` VALUES (238, 'Sp6', 'Sp19', 41.58);
INSERT INTO `graph` VALUES (239, 'Sp6', 'Sp20', 82.88);
INSERT INTO `graph` VALUES (240, 'Sp6', 'Sp21', 47.67);
INSERT INTO `graph` VALUES (241, 'Sp6', 'Sp22', 34.26);
INSERT INTO `graph` VALUES (242, 'Sp6', 'Sp23', 14.03);
INSERT INTO `graph` VALUES (243, 'Sp6', 'Sp24', 44.52);
INSERT INTO `graph` VALUES (244, 'Sp6', 'Sp25', 96.97);
INSERT INTO `graph` VALUES (245, 'Sp6', 'Sp26', 76.58);
INSERT INTO `graph` VALUES (246, 'Sp6', 'Sp27', 53.72);
INSERT INTO `graph` VALUES (247, 'Sp6', 'Sp28', 38.6);
INSERT INTO `graph` VALUES (248, 'Sp6', 'Sp29', 47.09);
INSERT INTO `graph` VALUES (249, 'Sp6', 'Sp30', 15.95);
INSERT INTO `graph` VALUES (250, 'Sp6', 'Sp31', 37.01);
INSERT INTO `graph` VALUES (251, 'Sp6', 'Sp32', 14.4);
INSERT INTO `graph` VALUES (252, 'Sp6', 'Sp33', 77.3);
INSERT INTO `graph` VALUES (253, 'Sp6', 'Sp34', 77.15);
INSERT INTO `graph` VALUES (254, 'Sp6', 'Sp35', 62.15);
INSERT INTO `graph` VALUES (255, 'Sp6', 'Sp36', 55.8);
INSERT INTO `graph` VALUES (256, 'Sp6', 'Sp37', 87.72);
INSERT INTO `graph` VALUES (257, 'Sp6', 'Sp38', 64.14);
INSERT INTO `graph` VALUES (258, 'Sp6', 'Sp39', 13.54);
INSERT INTO `graph` VALUES (259, 'Sp6', 'Sp40', 49.12);
INSERT INTO `graph` VALUES (260, 'Sp7', 'Sp8', 58.09);
INSERT INTO `graph` VALUES (261, 'Sp7', 'Sp9', 36.49);
INSERT INTO `graph` VALUES (262, 'Sp7', 'Sp10', 80.01);
INSERT INTO `graph` VALUES (263, 'Sp7', 'Sp11', 14.72);
INSERT INTO `graph` VALUES (264, 'Sp7', 'Sp12', 41.92);
INSERT INTO `graph` VALUES (265, 'Sp7', 'Sp13', 34.35);
INSERT INTO `graph` VALUES (266, 'Sp7', 'Sp14', 68.42);
INSERT INTO `graph` VALUES (267, 'Sp7', 'Sp15', 50.5);
INSERT INTO `graph` VALUES (268, 'Sp7', 'Sp16', 69.18);
INSERT INTO `graph` VALUES (269, 'Sp7', 'Sp17', 62.46);
INSERT INTO `graph` VALUES (270, 'Sp7', 'Sp18', 82.34);
INSERT INTO `graph` VALUES (271, 'Sp7', 'Sp19', 31.91);
INSERT INTO `graph` VALUES (272, 'Sp7', 'Sp20', 67.62);
INSERT INTO `graph` VALUES (273, 'Sp7', 'Sp21', 34.07);
INSERT INTO `graph` VALUES (274, 'Sp7', 'Sp22', 46.02);
INSERT INTO `graph` VALUES (275, 'Sp7', 'Sp23', 10.61);
INSERT INTO `graph` VALUES (276, 'Sp7', 'Sp24', 41.5);
INSERT INTO `graph` VALUES (277, 'Sp7', 'Sp25', 84.21);
INSERT INTO `graph` VALUES (278, 'Sp7', 'Sp26', 62.22);
INSERT INTO `graph` VALUES (279, 'Sp7', 'Sp27', 46.15);
INSERT INTO `graph` VALUES (280, 'Sp7', 'Sp28', 34.09);
INSERT INTO `graph` VALUES (281, 'Sp7', 'Sp29', 35.76);
INSERT INTO `graph` VALUES (282, 'Sp7', 'Sp30', 27.11);
INSERT INTO `graph` VALUES (283, 'Sp7', 'Sp31', 28.11);
INSERT INTO `graph` VALUES (284, 'Sp7', 'Sp32', 15.71);
INSERT INTO `graph` VALUES (285, 'Sp7', 'Sp33', 62.22);
INSERT INTO `graph` VALUES (286, 'Sp7', 'Sp34', 66.91);
INSERT INTO `graph` VALUES (287, 'Sp7', 'Sp35', 53.16);
INSERT INTO `graph` VALUES (288, 'Sp7', 'Sp36', 42.38);
INSERT INTO `graph` VALUES (289, 'Sp7', 'Sp37', 86.44);
INSERT INTO `graph` VALUES (290, 'Sp7', 'Sp38', 62.69);
INSERT INTO `graph` VALUES (291, 'Sp7', 'Sp39', 27.53);
INSERT INTO `graph` VALUES (292, 'Sp7', 'Sp40', 31.57);
INSERT INTO `graph` VALUES (293, 'Sp8', 'Sp9', 60.18);
INSERT INTO `graph` VALUES (294, 'Sp8', 'Sp10', 66.42);
INSERT INTO `graph` VALUES (295, 'Sp8', 'Sp11', 63.92);
INSERT INTO `graph` VALUES (296, 'Sp8', 'Sp12', 90.73);
INSERT INTO `graph` VALUES (297, 'Sp8', 'Sp13', 54.87);
INSERT INTO `graph` VALUES (298, 'Sp8', 'Sp14', 50.31);
INSERT INTO `graph` VALUES (299, 'Sp8', 'Sp15', 81.64);
INSERT INTO `graph` VALUES (300, 'Sp8', 'Sp16', 38.28);
INSERT INTO `graph` VALUES (301, 'Sp8', 'Sp17', 47.23);
INSERT INTO `graph` VALUES (302, 'Sp8', 'Sp18', 23.7);
INSERT INTO `graph` VALUES (303, 'Sp8', 'Sp19', 52.25);
INSERT INTO `graph` VALUES (304, 'Sp8', 'Sp20', 26.81);
INSERT INTO `graph` VALUES (305, 'Sp8', 'Sp21', 25.49);
INSERT INTO `graph` VALUES (306, 'Sp8', 'Sp22', 95.67);
INSERT INTO `graph` VALUES (307, 'Sp8', 'Sp23', 60.33);
INSERT INTO `graph` VALUES (308, 'Sp8', 'Sp24', 64.72);
INSERT INTO `graph` VALUES (309, 'Sp8', 'Sp25', 60.85);
INSERT INTO `graph` VALUES (310, 'Sp8', 'Sp26', 8.03);
INSERT INTO `graph` VALUES (311, 'Sp8', 'Sp27', 81.61);
INSERT INTO `graph` VALUES (312, 'Sp8', 'Sp28', 54.52);
INSERT INTO `graph` VALUES (313, 'Sp8', 'Sp29', 32.62);
INSERT INTO `graph` VALUES (314, 'Sp8', 'Sp30', 78.9);
INSERT INTO `graph` VALUES (315, 'Sp8', 'Sp31', 43.87);
INSERT INTO `graph` VALUES (316, 'Sp8', 'Sp32', 64.32);
INSERT INTO `graph` VALUES (317, 'Sp8', 'Sp33', 21.01);
INSERT INTO `graph` VALUES (318, 'Sp8', 'Sp34', 40.38);
INSERT INTO `graph` VALUES (319, 'Sp8', 'Sp35', 46.82);
INSERT INTO `graph` VALUES (320, 'Sp8', 'Sp36', 19.5);
INSERT INTO `graph` VALUES (321, 'Sp8', 'Sp37', 73.5);
INSERT INTO `graph` VALUES (322, 'Sp8', 'Sp38', 63.37);
INSERT INTO `graph` VALUES (323, 'Sp8', 'Sp39', 82.77);
INSERT INTO `graph` VALUES (324, 'Sp8', 'Sp40', 51.2);
INSERT INTO `graph` VALUES (325, 'Sp9', 'Sp10', 44.02);
INSERT INTO `graph` VALUES (326, 'Sp9', 'Sp11', 49.51);
INSERT INTO `graph` VALUES (327, 'Sp9', 'Sp12', 44.78);
INSERT INTO `graph` VALUES (328, 'Sp9', 'Sp13', 7.06);
INSERT INTO `graph` VALUES (329, 'Sp9', 'Sp14', 41.79);
INSERT INTO `graph` VALUES (330, 'Sp9', 'Sp15', 21.61);
INSERT INTO `graph` VALUES (331, 'Sp9', 'Sp16', 55.21);
INSERT INTO `graph` VALUES (332, 'Sp9', 'Sp17', 41.74);
INSERT INTO `graph` VALUES (333, 'Sp9', 'Sp18', 84.79);
INSERT INTO `graph` VALUES (334, 'Sp9', 'Sp19', 67.12);
INSERT INTO `graph` VALUES (335, 'Sp9', 'Sp20', 84.49);
INSERT INTO `graph` VALUES (336, 'Sp9', 'Sp21', 37.35);
INSERT INTO `graph` VALUES (337, 'Sp9', 'Sp22', 43.3);
INSERT INTO `graph` VALUES (338, 'Sp9', 'Sp23', 28.33);
INSERT INTO `graph` VALUES (339, 'Sp9', 'Sp24', 7.39);
INSERT INTO `graph` VALUES (340, 'Sp9', 'Sp25', 54.05);
INSERT INTO `graph` VALUES (341, 'Sp9', 'Sp26', 65.38);
INSERT INTO `graph` VALUES (342, 'Sp9', 'Sp27', 80.96);
INSERT INTO `graph` VALUES (343, 'Sp9', 'Sp28', 6.66);
INSERT INTO `graph` VALUES (344, 'Sp9', 'Sp29', 28.02);
INSERT INTO `graph` VALUES (345, 'Sp9', 'Sp30', 33.49);
INSERT INTO `graph` VALUES (346, 'Sp9', 'Sp31', 18.15);
INSERT INTO `graph` VALUES (347, 'Sp9', 'Sp32', 24.87);
INSERT INTO `graph` VALUES (348, 'Sp9', 'Sp33', 78.14);
INSERT INTO `graph` VALUES (349, 'Sp9', 'Sp34', 49.87);
INSERT INTO `graph` VALUES (350, 'Sp9', 'Sp35', 79.09);
INSERT INTO `graph` VALUES (351, 'Sp9', 'Sp36', 41.09);
INSERT INTO `graph` VALUES (352, 'Sp9', 'Sp37', 50.39);
INSERT INTO `graph` VALUES (353, 'Sp9', 'Sp38', 23.16);
INSERT INTO `graph` VALUES (354, 'Sp9', 'Sp39', 39.98);
INSERT INTO `graph` VALUES (355, 'Sp9', 'Sp40', 61.26);
INSERT INTO `graph` VALUES (356, 'Sp10', 'Sp11', 91.37);
INSERT INTO `graph` VALUES (357, 'Sp10', 'Sp12', 76.6);
INSERT INTO `graph` VALUES (358, 'Sp10', 'Sp13', 48.38);
INSERT INTO `graph` VALUES (359, 'Sp10', 'Sp14', 16.14);
INSERT INTO `graph` VALUES (360, 'Sp10', 'Sp15', 61.8);
INSERT INTO `graph` VALUES (361, 'Sp10', 'Sp16', 30.58);
INSERT INTO `graph` VALUES (362, 'Sp10', 'Sp17', 20.34);
INSERT INTO `graph` VALUES (363, 'Sp10', 'Sp18', 78.04);
INSERT INTO `graph` VALUES (364, 'Sp10', 'Sp19', 93.78);
INSERT INTO `graph` VALUES (365, 'Sp10', 'Sp20', 92.92);
INSERT INTO `graph` VALUES (366, 'Sp10', 'Sp21', 58.55);
INSERT INTO `graph` VALUES (367, 'Sp10', 'Sp22', 81.31);
INSERT INTO `graph` VALUES (368, 'Sp10', 'Sp23', 75.75);
INSERT INTO `graph` VALUES (369, 'Sp10', 'Sp24', 38.97);
INSERT INTO `graph` VALUES (370, 'Sp10', 'Sp25', 15.22);
INSERT INTO `graph` VALUES (371, 'Sp10', 'Sp26', 73.44);
INSERT INTO `graph` VALUES (372, 'Sp10', 'Sp27', 133.41);
INSERT INTO `graph` VALUES (373, 'Sp10', 'Sp28', 48.12);
INSERT INTO `graph` VALUES (374, 'Sp10', 'Sp29', 51.83);
INSERT INTO `graph` VALUES (375, 'Sp10', 'Sp30', 80.6);
INSERT INTO `graph` VALUES (376, 'Sp10', 'Sp31', 53.58);
INSERT INTO `graph` VALUES (377, 'Sp10', 'Sp32', 69.75);
INSERT INTO `graph` VALUES (378, 'Sp10', 'Sp33', 86.45);
INSERT INTO `graph` VALUES (379, 'Sp10', 'Sp34', 26.7);
INSERT INTO `graph` VALUES (380, 'Sp10', 'Sp35', 106.88);
INSERT INTO `graph` VALUES (381, 'Sp10', 'Sp36', 54.88);
INSERT INTO `graph` VALUES (382, 'Sp10', 'Sp37', 8.58);
INSERT INTO `graph` VALUES (383, 'Sp10', 'Sp38', 21.24);
INSERT INTO `graph` VALUES (384, 'Sp10', 'Sp39', 84.2);
INSERT INTO `graph` VALUES (385, 'Sp10', 'Sp40', 91.35);
INSERT INTO `graph` VALUES (386, 'Sp11', 'Sp12', 55.31);
INSERT INTO `graph` VALUES (387, 'Sp11', 'Sp13', 46.33);
INSERT INTO `graph` VALUES (388, 'Sp11', 'Sp14', 80.11);
INSERT INTO `graph` VALUES (389, 'Sp11', 'Sp15', 60.46);
INSERT INTO `graph` VALUES (390, 'Sp11', 'Sp16', 75.59);
INSERT INTO `graph` VALUES (391, 'Sp11', 'Sp17', 73.3);
INSERT INTO `graph` VALUES (392, 'Sp11', 'Sp18', 97.13);
INSERT INTO `graph` VALUES (393, 'Sp11', 'Sp19', 16.37);
INSERT INTO `graph` VALUES (394, 'Sp11', 'Sp20', 69.6);
INSERT INTO `graph` VALUES (395, 'Sp11', 'Sp21', 36.95);
INSERT INTO `graph` VALUES (396, 'Sp11', 'Sp22', 58.82);
INSERT INTO `graph` VALUES (397, 'Sp11', 'Sp23', 23.82);
INSERT INTO `graph` VALUES (398, 'Sp11', 'Sp24', 53.83);
INSERT INTO `graph` VALUES (399, 'Sp11', 'Sp25', 95.17);
INSERT INTO `graph` VALUES (400, 'Sp11', 'Sp26', 64.77);
INSERT INTO `graph` VALUES (401, 'Sp11', 'Sp27', 31.88);
INSERT INTO `graph` VALUES (402, 'Sp11', 'Sp28', 46.1);
INSERT INTO `graph` VALUES (403, 'Sp11', 'Sp29', 41.96);
INSERT INTO `graph` VALUES (404, 'Sp11', 'Sp30', 39.41);
INSERT INTO `graph` VALUES (405, 'Sp11', 'Sp31', 37.66);
INSERT INTO `graph` VALUES (406, 'Sp11', 'Sp32', 29.8);
INSERT INTO `graph` VALUES (407, 'Sp11', 'Sp33', 63.78);
INSERT INTO `graph` VALUES (408, 'Sp11', 'Sp34', 72.16);
INSERT INTO `graph` VALUES (409, 'Sp11', 'Sp35', 37.24);
INSERT INTO `graph` VALUES (410, 'Sp11', 'Sp36', 45.92);
INSERT INTO `graph` VALUES (411, 'Sp11', 'Sp37', 93.29);
INSERT INTO `graph` VALUES (412, 'Sp11', 'Sp38', 68.62);
INSERT INTO `graph` VALUES (413, 'Sp11', 'Sp39', 38.68);
INSERT INTO `graph` VALUES (414, 'Sp11', 'Sp40', 18.32);
INSERT INTO `graph` VALUES (415, 'Sp12', 'Sp13', 50.82);
INSERT INTO `graph` VALUES (416, 'Sp12', 'Sp14', 76.7);
INSERT INTO `graph` VALUES (417, 'Sp12', 'Sp15', 16.53);
INSERT INTO `graph` VALUES (418, 'Sp12', 'Sp16', 93.92);
INSERT INTO `graph` VALUES (419, 'Sp12', 'Sp17', 74.43);
INSERT INTO `graph` VALUES (420, 'Sp12', 'Sp18', 114.5);
INSERT INTO `graph` VALUES (421, 'Sp12', 'Sp19', 71.82);
INSERT INTO `graph` VALUES (422, 'Sp12', 'Sp20', 105.35);
INSERT INTO `graph` VALUES (423, 'Sp12', 'Sp21', 64.56);
INSERT INTO `graph` VALUES (424, 'Sp12', 'Sp22', 7.08);
INSERT INTO `graph` VALUES (425, 'Sp12', 'Sp23', 33.91);
INSERT INTO `graph` VALUES (426, 'Sp12', 'Sp24', 41.14);
INSERT INTO `graph` VALUES (427, 'Sp12', 'Sp25', 88.59);
INSERT INTO `graph` VALUES (428, 'Sp12', 'Sp26', 95.75);
INSERT INTO `graph` VALUES (429, 'Sp12', 'Sp27', 85.07);
INSERT INTO `graph` VALUES (430, 'Sp12', 'Sp28', 49.96);
INSERT INTO `graph` VALUES (431, 'Sp12', 'Sp29', 61.07);
INSERT INTO `graph` VALUES (432, 'Sp12', 'Sp30', 16.85);
INSERT INTO `graph` VALUES (433, 'Sp12', 'Sp31', 48.79);
INSERT INTO `graph` VALUES (434, 'Sp12', 'Sp32', 27.93);
INSERT INTO `graph` VALUES (435, 'Sp12', 'Sp33', 99.64);
INSERT INTO `graph` VALUES (436, 'Sp12', 'Sp34', 84.13);
INSERT INTO `graph` VALUES (437, 'Sp12', 'Sp35', 95.36);
INSERT INTO `graph` VALUES (438, 'Sp12', 'Sp36', 72.69);
INSERT INTO `graph` VALUES (439, 'Sp12', 'Sp37', 74.62);
INSERT INTO `graph` VALUES (440, 'Sp12', 'Sp38', 58.92);
INSERT INTO `graph` VALUES (441, 'Sp12', 'Sp39', 20.15);
INSERT INTO `graph` VALUES (442, 'Sp12', 'Sp40', 75.52);
INSERT INTO `graph` VALUES (443, 'Sp13', 'Sp14', 55.94);
INSERT INTO `graph` VALUES (444, 'Sp13', 'Sp15', 26.34);
INSERT INTO `graph` VALUES (445, 'Sp13', 'Sp16', 48.36);
INSERT INTO `graph` VALUES (446, 'Sp13', 'Sp17', 48.32);
INSERT INTO `graph` VALUES (447, 'Sp13', 'Sp18', 79.2);
INSERT INTO `graph` VALUES (448, 'Sp13', 'Sp19', 63.19);
INSERT INTO `graph` VALUES (449, 'Sp13', 'Sp20', 79.08);
INSERT INTO `graph` VALUES (450, 'Sp13', 'Sp21', 32.04);
INSERT INTO `graph` VALUES (451, 'Sp13', 'Sp22', 54.84);
INSERT INTO `graph` VALUES (452, 'Sp13', 'Sp23', 26.62);
INSERT INTO `graph` VALUES (453, 'Sp13', 'Sp24', 9.27);
INSERT INTO `graph` VALUES (454, 'Sp13', 'Sp25', 59.21);
INSERT INTO `graph` VALUES (455, 'Sp13', 'Sp26', 59.48);
INSERT INTO `graph` VALUES (456, 'Sp13', 'Sp27', 78.3);
INSERT INTO `graph` VALUES (457, 'Sp13', 'Sp28', 3.39);
INSERT INTO `graph` VALUES (458, 'Sp13', 'Sp29', 22.28);
INSERT INTO `graph` VALUES (459, 'Sp13', 'Sp30', 34.23);
INSERT INTO `graph` VALUES (460, 'Sp13', 'Sp31', 12.7);
INSERT INTO `graph` VALUES (461, 'Sp13', 'Sp32', 24.53);
INSERT INTO `graph` VALUES (462, 'Sp13', 'Sp33', 73.01);
INSERT INTO `graph` VALUES (463, 'Sp13', 'Sp34', 42.55);
INSERT INTO `graph` VALUES (464, 'Sp13', 'Sp35', 74.87);
INSERT INTO `graph` VALUES (465, 'Sp13', 'Sp36', 35.92);
INSERT INTO `graph` VALUES (466, 'Sp13', 'Sp37', 52.91);
INSERT INTO `graph` VALUES (467, 'Sp13', 'Sp38', 27.2);
INSERT INTO `graph` VALUES (468, 'Sp13', 'Sp39', 41.07);
INSERT INTO `graph` VALUES (469, 'Sp13', 'Sp40', 58.54);
INSERT INTO `graph` VALUES (470, 'Sp14', 'Sp15', 61.67);
INSERT INTO `graph` VALUES (471, 'Sp14', 'Sp16', 15.6);
INSERT INTO `graph` VALUES (472, 'Sp14', 'Sp17', 7.04);
INSERT INTO `graph` VALUES (473, 'Sp14', 'Sp18', 63.02);
INSERT INTO `graph` VALUES (474, 'Sp14', 'Sp19', 78.47);
INSERT INTO `graph` VALUES (475, 'Sp14', 'Sp20', 76.27);
INSERT INTO `graph` VALUES (476, 'Sp14', 'Sp21', 44.37);
INSERT INTO `graph` VALUES (477, 'Sp14', 'Sp22', 81.8);
INSERT INTO `graph` VALUES (478, 'Sp14', 'Sp23', 64.37);
INSERT INTO `graph` VALUES (479, 'Sp14', 'Sp24', 35.88);
INSERT INTO `graph` VALUES (480, 'Sp14', 'Sp25', 15.92);
INSERT INTO `graph` VALUES (481, 'Sp14', 'Sp26', 57.36);
INSERT INTO `graph` VALUES (482, 'Sp14', 'Sp27', 109.65);
INSERT INTO `graph` VALUES (483, 'Sp14', 'Sp28', 52.13);
INSERT INTO `graph` VALUES (484, 'Sp14', 'Sp29', 35.72);
INSERT INTO `graph` VALUES (485, 'Sp14', 'Sp30', 80.89);
INSERT INTO `graph` VALUES (486, 'Sp14', 'Sp31', 40.67);
INSERT INTO `graph` VALUES (487, 'Sp14', 'Sp32', 65.65);
INSERT INTO `graph` VALUES (488, 'Sp14', 'Sp33', 70.44);
INSERT INTO `graph` VALUES (489, 'Sp14', 'Sp34', 11.17);
INSERT INTO `graph` VALUES (490, 'Sp14', 'Sp35', 88.9);
INSERT INTO `graph` VALUES (491, 'Sp14', 'Sp36', 39.72);
INSERT INTO `graph` VALUES (492, 'Sp14', 'Sp37', 23.61);
INSERT INTO `graph` VALUES (493, 'Sp14', 'Sp38', 18.55);
INSERT INTO `graph` VALUES (494, 'Sp14', 'Sp39', 88.6);
INSERT INTO `graph` VALUES (495, 'Sp14', 'Sp40', 75.98);
INSERT INTO `graph` VALUES (496, 'Sp15', 'Sp16', 72.52);
INSERT INTO `graph` VALUES (497, 'Sp15', 'Sp17', 57.9);
INSERT INTO `graph` VALUES (498, 'Sp15', 'Sp18', 104.91);
INSERT INTO `graph` VALUES (499, 'Sp15', 'Sp19', 79.68);
INSERT INTO `graph` VALUES (500, 'Sp15', 'Sp20', 102.89);
INSERT INTO `graph` VALUES (501, 'Sp15', 'Sp21', 58.59);
INSERT INTO `graph` VALUES (502, 'Sp15', 'Sp22', 21.13);
INSERT INTO `graph` VALUES (503, 'Sp15', 'Sp23', 39.05);
INSERT INTO `graph` VALUES (504, 'Sp15', 'Sp24', 24.38);
INSERT INTO `graph` VALUES (505, 'Sp15', 'Sp25', 72.48);
INSERT INTO `graph` VALUES (506, 'Sp15', 'Sp26', 88.26);
INSERT INTO `graph` VALUES (507, 'Sp15', 'Sp27', 91.52);
INSERT INTO `graph` VALUES (508, 'Sp15', 'Sp28', 26.28);
INSERT INTO `graph` VALUES (509, 'Sp15', 'Sp29', 48.47);
INSERT INTO `graph` VALUES (510, 'Sp15', 'Sp30', 22.91);
INSERT INTO `graph` VALUES (511, 'Sp15', 'Sp31', 42.62);
INSERT INTO `graph` VALUES (512, 'Sp15', 'Sp32', 30.35);
INSERT INTO `graph` VALUES (513, 'Sp15', 'Sp33', 98);
INSERT INTO `graph` VALUES (514, 'Sp15', 'Sp34', 67.25);
INSERT INTO `graph` VALUES (515, 'Sp15', 'Sp35', 102.07);
INSERT INTO `graph` VALUES (516, 'Sp15', 'Sp36', 62.53);
INSERT INTO `graph` VALUES (517, 'Sp15', 'Sp37', 59.02);
INSERT INTO `graph` VALUES (518, 'Sp15', 'Sp38', 42.96);
INSERT INTO `graph` VALUES (519, 'Sp15', 'Sp39', 29.85);
INSERT INTO `graph` VALUES (520, 'Sp15', 'Sp40', 82.74);
INSERT INTO `graph` VALUES (521, 'Sp16', 'Sp17', 17.08);
INSERT INTO `graph` VALUES (522, 'Sp16', 'Sp18', 46.89);
INSERT INTO `graph` VALUES (523, 'Sp16', 'Sp19', 73.26);
INSERT INTO `graph` VALUES (524, 'Sp16', 'Sp20', 66.38);
INSERT INTO `graph` VALUES (525, 'Sp16', 'Sp21', 39.95);
INSERT INTO `graph` VALUES (526, 'Sp16', 'Sp22', 98.14);
INSERT INTO `graph` VALUES (527, 'Sp16', 'Sp23', 67.89);
INSERT INTO `graph` VALUES (528, 'Sp16', 'Sp24', 47.86);
INSERT INTO `graph` VALUES (529, 'Sp16', 'Sp25', 23);
INSERT INTO `graph` VALUES (530, 'Sp16', 'Sp26', 45.89);
INSERT INTO `graph` VALUES (531, 'Sp16', 'Sp27', 101.22);
INSERT INTO `graph` VALUES (532, 'Sp16', 'Sp28', 48.14);
INSERT INTO `graph` VALUES (533, 'Sp16', 'Sp29', 34.04);
INSERT INTO `graph` VALUES (534, 'Sp16', 'Sp30', 79.08);
INSERT INTO `graph` VALUES (535, 'Sp16', 'Sp31', 45.6);
INSERT INTO `graph` VALUES (536, 'Sp16', 'Sp32', 69.21);
INSERT INTO `graph` VALUES (537, 'Sp16', 'Sp33', 59.31);
INSERT INTO `graph` VALUES (538, 'Sp16', 'Sp34', 7.56);
INSERT INTO `graph` VALUES (539, 'Sp16', 'Sp35', 82.3);
INSERT INTO `graph` VALUES (540, 'Sp16', 'Sp36', 33.06);
INSERT INTO `graph` VALUES (541, 'Sp16', 'Sp37', 37.9);
INSERT INTO `graph` VALUES (542, 'Sp16', 'Sp38', 31.84);
INSERT INTO `graph` VALUES (543, 'Sp16', 'Sp39', 86.07);
INSERT INTO `graph` VALUES (544, 'Sp16', 'Sp40', 71.05);
INSERT INTO `graph` VALUES (545, 'Sp17', 'Sp18', 63.62);
INSERT INTO `graph` VALUES (546, 'Sp17', 'Sp19', 73.15);
INSERT INTO `graph` VALUES (547, 'Sp17', 'Sp20', 72.59);
INSERT INTO `graph` VALUES (548, 'Sp17', 'Sp21', 38.78);
INSERT INTO `graph` VALUES (549, 'Sp17', 'Sp22', 78.72);
INSERT INTO `graph` VALUES (550, 'Sp17', 'Sp23', 57.26);
INSERT INTO `graph` VALUES (551, 'Sp17', 'Sp24', 35.5);
INSERT INTO `graph` VALUES (552, 'Sp17', 'Sp25', 22.43);
INSERT INTO `graph` VALUES (553, 'Sp17', 'Sp26', 54);
INSERT INTO `graph` VALUES (554, 'Sp17', 'Sp27', 107.99);
INSERT INTO `graph` VALUES (555, 'Sp17', 'Sp28', 46.92);
INSERT INTO `graph` VALUES (556, 'Sp17', 'Sp29', 29.78);
INSERT INTO `graph` VALUES (557, 'Sp17', 'Sp30', 75.76);
INSERT INTO `graph` VALUES (558, 'Sp17', 'Sp31', 33.9);
INSERT INTO `graph` VALUES (559, 'Sp17', 'Sp32', 58.28);
INSERT INTO `graph` VALUES (560, 'Sp17', 'Sp33', 67.11);
INSERT INTO `graph` VALUES (561, 'Sp17', 'Sp34', 11.6);
INSERT INTO `graph` VALUES (562, 'Sp17', 'Sp35', 86.99);
INSERT INTO `graph` VALUES (563, 'Sp17', 'Sp36', 34.7);
INSERT INTO `graph` VALUES (564, 'Sp17', 'Sp37', 27.52);
INSERT INTO `graph` VALUES (565, 'Sp17', 'Sp38', 14.78);
INSERT INTO `graph` VALUES (566, 'Sp17', 'Sp39', 78.17);
INSERT INTO `graph` VALUES (567, 'Sp17', 'Sp40', 70.16);
INSERT INTO `graph` VALUES (568, 'Sp18', 'Sp19', 71.96);
INSERT INTO `graph` VALUES (569, 'Sp18', 'Sp20', 40.76);
INSERT INTO `graph` VALUES (570, 'Sp18', 'Sp21', 48.86);
INSERT INTO `graph` VALUES (571, 'Sp18', 'Sp22', 119.81);
INSERT INTO `graph` VALUES (572, 'Sp18', 'Sp23', 83.88);
INSERT INTO `graph` VALUES (573, 'Sp18', 'Sp24', 91.87);
INSERT INTO `graph` VALUES (574, 'Sp18', 'Sp25', 66.93);
INSERT INTO `graph` VALUES (575, 'Sp18', 'Sp26', 32.95);
INSERT INTO `graph` VALUES (576, 'Sp18', 'Sp27', 88.87);
INSERT INTO `graph` VALUES (577, 'Sp18', 'Sp28', 79.08);
INSERT INTO `graph` VALUES (578, 'Sp18', 'Sp29', 55.89);
INSERT INTO `graph` VALUES (579, 'Sp18', 'Sp30', 102.36);
INSERT INTO `graph` VALUES (580, 'Sp18', 'Sp31', 67.19);
INSERT INTO `graph` VALUES (581, 'Sp18', 'Sp32', 87.68);
INSERT INTO `graph` VALUES (582, 'Sp18', 'Sp33', 30.49);
INSERT INTO `graph` VALUES (583, 'Sp18', 'Sp34', 52.56);
INSERT INTO `graph` VALUES (584, 'Sp18', 'Sp35', 61.62);
INSERT INTO `graph` VALUES (585, 'Sp18', 'Sp36', 41.95);
INSERT INTO `graph` VALUES (586, 'Sp18', 'Sp37', 84.48);
INSERT INTO `graph` VALUES (587, 'Sp18', 'Sp38', 81.95);
INSERT INTO `graph` VALUES (588, 'Sp18', 'Sp39', 106.3);
INSERT INTO `graph` VALUES (589, 'Sp18', 'Sp40', 70.67);
INSERT INTO `graph` VALUES (590, 'Sp19', 'Sp20', 54.37);
INSERT INTO `graph` VALUES (591, 'Sp19', 'Sp21', 33.46);
INSERT INTO `graph` VALUES (592, 'Sp19', 'Sp22', 75.82);
INSERT INTO `graph` VALUES (593, 'Sp19', 'Sp23', 45.37);
INSERT INTO `graph` VALUES (594, 'Sp19', 'Sp24', 67.67);
INSERT INTO `graph` VALUES (595, 'Sp19', 'Sp25', 93.13);
INSERT INTO `graph` VALUES (596, 'Sp19', 'Sp26', 43.51);
INSERT INTO `graph` VALUES (597, 'Sp19', 'Sp27', 33.51);
INSERT INTO `graph` VALUES (598, 'Sp19', 'Sp28', 63.48);
INSERT INTO `graph` VALUES (599, 'Sp19', 'Sp29', 43.39);
INSERT INTO `graph` VALUES (600, 'Sp19', 'Sp30', 56.2);
INSERT INTO `graph` VALUES (601, 'Sp19', 'Sp31', 50.34);
INSERT INTO `graph` VALUES (602, 'Sp19', 'Sp32', 45);
INSERT INTO `graph` VALUES (603, 'Sp19', 'Sp33', 46.67);
INSERT INTO `graph` VALUES (604, 'Sp19', 'Sp34', 71.65);
INSERT INTO `graph` VALUES (605, 'Sp19', 'Sp35', 22.08);
INSERT INTO `graph` VALUES (606, 'Sp19', 'Sp36', 40.46);
INSERT INTO `graph` VALUES (607, 'Sp19', 'Sp37', 104.52);
INSERT INTO `graph` VALUES (608, 'Sp19', 'Sp38', 75.87);
INSERT INTO `graph` VALUES (609, 'Sp19', 'Sp39', 55.41);
INSERT INTO `graph` VALUES (610, 'Sp19', 'Sp40', 2.83);
INSERT INTO `graph` VALUES (611, 'Sp20', 'Sp21', 45.4);
INSERT INTO `graph` VALUES (612, 'Sp20', 'Sp22', 110.42);
INSERT INTO `graph` VALUES (613, 'Sp20', 'Sp23', 72.88);
INSERT INTO `graph` VALUES (614, 'Sp20', 'Sp24', 90.66);
INSERT INTO `graph` VALUES (615, 'Sp20', 'Sp25', 91);
INSERT INTO `graph` VALUES (616, 'Sp20', 'Sp26', 18.89);
INSERT INTO `graph` VALUES (617, 'Sp20', 'Sp27', 64.61);
INSERT INTO `graph` VALUES (618, 'Sp20', 'Sp28', 79.1);
INSERT INTO `graph` VALUES (619, 'Sp20', 'Sp29', 59.24);
INSERT INTO `graph` VALUES (620, 'Sp20', 'Sp30', 92.34);
INSERT INTO `graph` VALUES (621, 'Sp20', 'Sp31', 65.67);
INSERT INTO `graph` VALUES (622, 'Sp20', 'Sp32', 78.16);
INSERT INTO `graph` VALUES (623, 'Sp20', 'Sp33', 8.63);
INSERT INTO `graph` VALUES (624, 'Sp20', 'Sp34', 67.78);
INSERT INTO `graph` VALUES (625, 'Sp20', 'Sp35', 33.62);
INSERT INTO `graph` VALUES (626, 'Sp20', 'Sp36', 44.52);
INSERT INTO `graph` VALUES (627, 'Sp20', 'Sp37', 99.96);
INSERT INTO `graph` VALUES (628, 'Sp20', 'Sp38', 87.66);
INSERT INTO `graph` VALUES (629, 'Sp20', 'Sp39', 94.59);
INSERT INTO `graph` VALUES (630, 'Sp20', 'Sp40', 51.21);
INSERT INTO `graph` VALUES (631, 'Sp21', 'Sp22', 69.68);
INSERT INTO `graph` VALUES (632, 'Sp21', 'Sp23', 35.17);
INSERT INTO `graph` VALUES (633, 'Sp21', 'Sp24', 44.13);
INSERT INTO `graph` VALUES (634, 'Sp21', 'Sp25', 58.91);
INSERT INTO `graph` VALUES (635, 'Sp21', 'Sp26', 32.31);
INSERT INTO `graph` VALUES (636, 'Sp21', 'Sp27', 62.46);
INSERT INTO `graph` VALUES (637, 'Sp21', 'Sp28', 31.77);
INSERT INTO `graph` VALUES (638, 'Sp21', 'Sp29', 11.72);
INSERT INTO `graph` VALUES (639, 'Sp21', 'Sp30', 53.49);
INSERT INTO `graph` VALUES (640, 'Sp21', 'Sp31', 19.83);
INSERT INTO `graph` VALUES (641, 'Sp21', 'Sp32', 38.89);
INSERT INTO `graph` VALUES (642, 'Sp21', 'Sp33', 39.95);
INSERT INTO `graph` VALUES (643, 'Sp21', 'Sp34', 37.9);
INSERT INTO `graph` VALUES (644, 'Sp21', 'Sp35', 53.13);
INSERT INTO `graph` VALUES (645, 'Sp21', 'Sp36', 8.82);
INSERT INTO `graph` VALUES (646, 'Sp21', 'Sp37', 65.23);
INSERT INTO `graph` VALUES (647, 'Sp21', 'Sp38', 48.36);
INSERT INTO `graph` VALUES (648, 'Sp21', 'Sp39', 57.52);
INSERT INTO `graph` VALUES (649, 'Sp21', 'Sp40', 31.57);
INSERT INTO `graph` VALUES (650, 'Sp22', 'Sp23', 38.26);
INSERT INTO `graph` VALUES (651, 'Sp22', 'Sp24', 44.97);
INSERT INTO `graph` VALUES (652, 'Sp22', 'Sp25', 93.08);
INSERT INTO `graph` VALUES (653, 'Sp22', 'Sp26', 100.96);
INSERT INTO `graph` VALUES (654, 'Sp22', 'Sp27', 87.79);
INSERT INTO `graph` VALUES (655, 'Sp22', 'Sp28', 51.55);
INSERT INTO `graph` VALUES (656, 'Sp22', 'Sp29', 65.72);
INSERT INTO `graph` VALUES (657, 'Sp22', 'Sp30', 19.8);
INSERT INTO `graph` VALUES (658, 'Sp22', 'Sp31', 52.87);
INSERT INTO `graph` VALUES (659, 'Sp22', 'Sp32', 32.45);
INSERT INTO `graph` VALUES (660, 'Sp22', 'Sp33', 104.75);
INSERT INTO `graph` VALUES (661, 'Sp22', 'Sp34', 89.66);
INSERT INTO `graph` VALUES (662, 'Sp22', 'Sp35', 97.85);
INSERT INTO `graph` VALUES (663, 'Sp22', 'Sp36', 77.3);
INSERT INTO `graph` VALUES (664, 'Sp22', 'Sp37', 79.19);
INSERT INTO `graph` VALUES (665, 'Sp22', 'Sp38', 63.45);
INSERT INTO `graph` VALUES (666, 'Sp22', 'Sp39', 21.89);
INSERT INTO `graph` VALUES (667, 'Sp22', 'Sp40', 78.49);
INSERT INTO `graph` VALUES (668, 'Sp23', 'Sp24', 33.15);
INSERT INTO `graph` VALUES (669, 'Sp23', 'Sp25', 81.22);
INSERT INTO `graph` VALUES (670, 'Sp23', 'Sp26', 66.5);
INSERT INTO `graph` VALUES (671, 'Sp23', 'Sp27', 55.58);
INSERT INTO `graph` VALUES (672, 'Sp23', 'Sp28', 26.56);
INSERT INTO `graph` VALUES (673, 'Sp23', 'Sp29', 33.41);
INSERT INTO `graph` VALUES (674, 'Sp23', 'Sp30', 19.49);
INSERT INTO `graph` VALUES (675, 'Sp23', 'Sp31', 23.38);
INSERT INTO `graph` VALUES (676, 'Sp23', 'Sp32', 6.94);
INSERT INTO `graph` VALUES (677, 'Sp23', 'Sp33', 67.53);
INSERT INTO `graph` VALUES (678, 'Sp23', 'Sp34', 64.28);
INSERT INTO `graph` VALUES (679, 'Sp23', 'Sp35', 64.52);
INSERT INTO `graph` VALUES (680, 'Sp23', 'Sp36', 43.11);
INSERT INTO `graph` VALUES (681, 'Sp23', 'Sp37', 76.63);
INSERT INTO `graph` VALUES (682, 'Sp23', 'Sp38', 55.18);
INSERT INTO `graph` VALUES (683, 'Sp23', 'Sp39', 22.89);
INSERT INTO `graph` VALUES (684, 'Sp23', 'Sp40', 46.62);
INSERT INTO `graph` VALUES (685, 'Sp24', 'Sp25', 48.5);
INSERT INTO `graph` VALUES (686, 'Sp24', 'Sp26', 70.11);
INSERT INTO `graph` VALUES (687, 'Sp24', 'Sp27', 85.22);
INSERT INTO `graph` VALUES (688, 'Sp24', 'Sp28', 8.36);
INSERT INTO `graph` VALUES (689, 'Sp24', 'Sp29', 34.04);
INSERT INTO `graph` VALUES (690, 'Sp24', 'Sp30', 38.99);
INSERT INTO `graph` VALUES (691, 'Sp24', 'Sp31', 20.94);
INSERT INTO `graph` VALUES (692, 'Sp24', 'Sp32', 30.34);
INSERT INTO `graph` VALUES (693, 'Sp24', 'Sp33', 84.84);
INSERT INTO `graph` VALUES (694, 'Sp24', 'Sp34', 45.5);
INSERT INTO `graph` VALUES (695, 'Sp24', 'Sp35', 84.42);
INSERT INTO `graph` VALUES (696, 'Sp24', 'Sp36', 47.96);
INSERT INTO `graph` VALUES (697, 'Sp24', 'Sp37', 42.87);
INSERT INTO `graph` VALUES (698, 'Sp24', 'Sp38', 18.35);
INSERT INTO `graph` VALUES (699, 'Sp24', 'Sp39', 45.49);
INSERT INTO `graph` VALUES (700, 'Sp24', 'Sp40', 65.06);
INSERT INTO `graph` VALUES (701, 'Sp25', 'Sp26', 68.35);
INSERT INTO `graph` VALUES (702, 'Sp25', 'Sp27', 121.35);
INSERT INTO `graph` VALUES (703, 'Sp25', 'Sp28', 59.09);
INSERT INTO `graph` VALUES (704, 'Sp25', 'Sp29', 50.45);
INSERT INTO `graph` VALUES (705, 'Sp25', 'Sp30', 88.91);
INSERT INTO `graph` VALUES (706, 'Sp25', 'Sp31', 56.03);
INSERT INTO `graph` VALUES (707, 'Sp25', 'Sp32', 86.12);
INSERT INTO `graph` VALUES (708, 'Sp25', 'Sp33', 82.24);
INSERT INTO `graph` VALUES (709, 'Sp25', 'Sp34', 21.7);
INSERT INTO `graph` VALUES (710, 'Sp25', 'Sp35', 103.79);
INSERT INTO `graph` VALUES (711, 'Sp25', 'Sp36', 53.53);
INSERT INTO `graph` VALUES (712, 'Sp25', 'Sp37', 19.93);
INSERT INTO `graph` VALUES (713, 'Sp25', 'Sp38', 31.17);
INSERT INTO `graph` VALUES (714, 'Sp25', 'Sp39', 96.57);
INSERT INTO `graph` VALUES (715, 'Sp25', 'Sp40', 90.7);
INSERT INTO `graph` VALUES (716, 'Sp26', 'Sp27', 66.58);
INSERT INTO `graph` VALUES (717, 'Sp26', 'Sp28', 59.73);
INSERT INTO `graph` VALUES (718, 'Sp26', 'Sp29', 37.51);
INSERT INTO `graph` VALUES (719, 'Sp26', 'Sp30', 84.51);
INSERT INTO `graph` VALUES (720, 'Sp26', 'Sp31', 47.98);
INSERT INTO `graph` VALUES (721, 'Sp26', 'Sp32', 69.97);
INSERT INTO `graph` VALUES (722, 'Sp26', 'Sp33', 13.84);
INSERT INTO `graph` VALUES (723, 'Sp26', 'Sp34', 47.58);
INSERT INTO `graph` VALUES (724, 'Sp26', 'Sp35', 38.32);
INSERT INTO `graph` VALUES (725, 'Sp26', 'Sp36', 24.69);
INSERT INTO `graph` VALUES (726, 'Sp26', 'Sp37', 80.39);
INSERT INTO `graph` VALUES (727, 'Sp26', 'Sp38', 68.64);
INSERT INTO `graph` VALUES (728, 'Sp26', 'Sp39', 88.07);
INSERT INTO `graph` VALUES (729, 'Sp26', 'Sp40', 41.52);
INSERT INTO `graph` VALUES (730, 'Sp27', 'Sp28', 77.93);
INSERT INTO `graph` VALUES (731, 'Sp27', 'Sp29', 77.29);
INSERT INTO `graph` VALUES (732, 'Sp27', 'Sp30', 68.95);
INSERT INTO `graph` VALUES (733, 'Sp27', 'Sp31', 72.58);
INSERT INTO `graph` VALUES (734, 'Sp27', 'Sp32', 61.36);
INSERT INTO `graph` VALUES (735, 'Sp27', 'Sp33', 60.51);
INSERT INTO `graph` VALUES (736, 'Sp27', 'Sp34', 101.11);
INSERT INTO `graph` VALUES (737, 'Sp27', 'Sp35', 36.59);
INSERT INTO `graph` VALUES (738, 'Sp27', 'Sp36', 67.4);
INSERT INTO `graph` VALUES (739, 'Sp27', 'Sp37', 129.53);
INSERT INTO `graph` VALUES (740, 'Sp27', 'Sp38', 105.86);
INSERT INTO `graph` VALUES (741, 'Sp27', 'Sp39', 66.35);
INSERT INTO `graph` VALUES (742, 'Sp27', 'Sp40', 31.94);
INSERT INTO `graph` VALUES (743, 'Sp28', 'Sp29', 22.02);
INSERT INTO `graph` VALUES (744, 'Sp28', 'Sp30', 34.25);
INSERT INTO `graph` VALUES (745, 'Sp28', 'Sp31', 12.39);
INSERT INTO `graph` VALUES (746, 'Sp28', 'Sp32', 24.37);
INSERT INTO `graph` VALUES (747, 'Sp28', 'Sp33', 73.67);
INSERT INTO `graph` VALUES (748, 'Sp28', 'Sp34', 42.63);
INSERT INTO `graph` VALUES (749, 'Sp28', 'Sp35', 75.03);
INSERT INTO `graph` VALUES (750, 'Sp28', 'Sp36', 35.57);
INSERT INTO `graph` VALUES (751, 'Sp28', 'Sp37', 51.03);
INSERT INTO `graph` VALUES (752, 'Sp28', 'Sp38', 30.9);
INSERT INTO `graph` VALUES (753, 'Sp28', 'Sp39', 41.04);
INSERT INTO `graph` VALUES (754, 'Sp28', 'Sp40', 55.78);
INSERT INTO `graph` VALUES (755, 'Sp29', 'Sp30', 49.39);
INSERT INTO `graph` VALUES (756, 'Sp29', 'Sp31', 12.21);
INSERT INTO `graph` VALUES (757, 'Sp29', 'Sp32', 35.56);
INSERT INTO `graph` VALUES (758, 'Sp29', 'Sp33', 54.94);
INSERT INTO `graph` VALUES (759, 'Sp29', 'Sp34', 30.3);
INSERT INTO `graph` VALUES (760, 'Sp29', 'Sp35', 62.63);
INSERT INTO `graph` VALUES (761, 'Sp29', 'Sp36', 14.03);
INSERT INTO `graph` VALUES (762, 'Sp29', 'Sp37', 60.2);
INSERT INTO `graph` VALUES (763, 'Sp29', 'Sp38', 33.96);
INSERT INTO `graph` VALUES (764, 'Sp29', 'Sp39', 54.66);
INSERT INTO `graph` VALUES (765, 'Sp29', 'Sp40', 41.39);
INSERT INTO `graph` VALUES (766, 'Sp30', 'Sp31', 37.78);
INSERT INTO `graph` VALUES (767, 'Sp30', 'Sp32', 15.1);
INSERT INTO `graph` VALUES (768, 'Sp30', 'Sp33', 86.95);
INSERT INTO `graph` VALUES (769, 'Sp30', 'Sp34', 74.05);
INSERT INTO `graph` VALUES (770, 'Sp30', 'Sp35', 78.63);
INSERT INTO `graph` VALUES (771, 'Sp30', 'Sp36', 60.86);
INSERT INTO `graph` VALUES (772, 'Sp30', 'Sp37', 89.22);
INSERT INTO `graph` VALUES (773, 'Sp30', 'Sp38', 57.57);
INSERT INTO `graph` VALUES (774, 'Sp30', 'Sp39', 9.01);
INSERT INTO `graph` VALUES (775, 'Sp30', 'Sp40', 60.69);
INSERT INTO `graph` VALUES (776, 'Sp31', 'Sp32', 24.45);
INSERT INTO `graph` VALUES (777, 'Sp31', 'Sp33', 59.35);
INSERT INTO `graph` VALUES (778, 'Sp31', 'Sp34', 41.53);
INSERT INTO `graph` VALUES (779, 'Sp31', 'Sp35', 65.97);
INSERT INTO `graph` VALUES (780, 'Sp31', 'Sp36', 24.89);
INSERT INTO `graph` VALUES (781, 'Sp31', 'Sp37', 55.58);
INSERT INTO `graph` VALUES (782, 'Sp31', 'Sp38', 30.51);
INSERT INTO `graph` VALUES (783, 'Sp31', 'Sp39', 43.35);
INSERT INTO `graph` VALUES (784, 'Sp31', 'Sp40', 43.35);
INSERT INTO `graph` VALUES (785, 'Sp32', 'Sp33', 72.53);
INSERT INTO `graph` VALUES (786, 'Sp32', 'Sp34', 62.32);
INSERT INTO `graph` VALUES (787, 'Sp32', 'Sp35', 70.11);
INSERT INTO `graph` VALUES (788, 'Sp32', 'Sp36', 46.24);
INSERT INTO `graph` VALUES (789, 'Sp32', 'Sp37', 74.08);
INSERT INTO `graph` VALUES (790, 'Sp32', 'Sp38', 49.12);
INSERT INTO `graph` VALUES (791, 'Sp32', 'Sp39', 19.14);
INSERT INTO `graph` VALUES (792, 'Sp32', 'Sp40', 54.05);
INSERT INTO `graph` VALUES (793, 'Sp33', 'Sp34', 60.85);
INSERT INTO `graph` VALUES (794, 'Sp33', 'Sp35', 31.99);
INSERT INTO `graph` VALUES (795, 'Sp33', 'Sp36', 40.98);
INSERT INTO `graph` VALUES (796, 'Sp33', 'Sp37', 93.59);
INSERT INTO `graph` VALUES (797, 'Sp33', 'Sp38', 83.53);
INSERT INTO `graph` VALUES (798, 'Sp33', 'Sp39', 89.19);
INSERT INTO `graph` VALUES (799, 'Sp33', 'Sp40', 44.76);
INSERT INTO `graph` VALUES (800, 'Sp34', 'Sp35', 82.26);
INSERT INTO `graph` VALUES (801, 'Sp34', 'Sp36', 32.23);
INSERT INTO `graph` VALUES (802, 'Sp34', 'Sp37', 33.53);
INSERT INTO `graph` VALUES (803, 'Sp34', 'Sp38', 25.71);
INSERT INTO `graph` VALUES (804, 'Sp34', 'Sp39', 79.73);
INSERT INTO `graph` VALUES (805, 'Sp34', 'Sp40', 69.58);
INSERT INTO `graph` VALUES (806, 'Sp35', 'Sp36', 49.28);
INSERT INTO `graph` VALUES (807, 'Sp35', 'Sp37', 114.67);
INSERT INTO `graph` VALUES (808, 'Sp35', 'Sp38', 96.08);
INSERT INTO `graph` VALUES (809, 'Sp35', 'Sp39', 75.7);
INSERT INTO `graph` VALUES (810, 'Sp35', 'Sp40', 21.25);
INSERT INTO `graph` VALUES (811, 'Sp36', 'Sp37', 61.63);
INSERT INTO `graph` VALUES (812, 'Sp36', 'Sp38', 47.34);
INSERT INTO `graph` VALUES (813, 'Sp36', 'Sp39', 65.07);
INSERT INTO `graph` VALUES (814, 'Sp36', 'Sp40', 38.07);
INSERT INTO `graph` VALUES (815, 'Sp37', 'Sp38', 25.46);
INSERT INTO `graph` VALUES (816, 'Sp37', 'Sp39', 94.26);
INSERT INTO `graph` VALUES (817, 'Sp37', 'Sp40', 104.4);
INSERT INTO `graph` VALUES (818, 'Sp38', 'Sp39', 63.48);
INSERT INTO `graph` VALUES (819, 'Sp38', 'Sp40', 73.1);
INSERT INTO `graph` VALUES (820, 'Sp39', 'Sp40', 57.64);

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '订单主键，唯一属性',
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '订单商家地址，同时也是商店名',
  `timestage` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '期望时间段（单位是分钟）',
  `dtime` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '最晚时间（单位同上）',
  `nback` json NULL COMMENT '退还多少（只计量没有分类型）',
  `buyitem` json NULL COMMENT '买的东西（“商品名”:\"数量\"）',
  `early_time` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `remain_time` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 183 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (1, 'Sp1', '192.0-491.99999999999994', '636', '{\"frozen\": 0.029, \"normal\": 0.028, \"refrigeration\": 0.024}', '{\"frozen\": 0.061, \"normal\": 0.036, \"refrigeration\": 0.056}', '24', '9');
INSERT INTO `orders` VALUES (2, 'Sp2', '480.0-606.0', '756', '{\"frozen\": 0.012, \"normal\": 0.02, \"refrigeration\": 0.026}', '{\"frozen\": 0.082, \"normal\": 0.04, \"refrigeration\": 0.02}', '336', '2');
INSERT INTO `orders` VALUES (3, 'Sp3', '348.0-491.99999999999994', '558', '{\"frozen\": 0.006, \"normal\": 0.02, \"refrigeration\": 0.018}', '{\"frozen\": 0.032, \"normal\": 0.016, \"refrigeration\": 0.071}', '276', '4');
INSERT INTO `orders` VALUES (4, 'Sp4', '414.0-660.0', '744', '{\"frozen\": 0.008, \"normal\": 0.004, \"refrigeration\": 0.024}', '{\"frozen\": 0.042, \"normal\": 0.016, \"refrigeration\": 0.028}', '348', '2');
INSERT INTO `orders` VALUES (5, 'Sp5', '245.99999999999997-438.0', '540', '{\"frozen\": 0.026, \"normal\": 0.015, \"refrigeration\": 0.022}', '{\"frozen\": 0.018, \"normal\": 0.069, \"refrigeration\": 0.044}', '108', '7');
INSERT INTO `orders` VALUES (6, 'Sp6', '354.0-540.0', '714', '{\"frozen\": 0.018, \"normal\": 0.005, \"refrigeration\": 0.026}', '{\"frozen\": 0.087, \"normal\": 0.054, \"refrigeration\": 0.066}', '270', '7');
INSERT INTO `orders` VALUES (7, 'Sp7', '282.0-384.0', '510', '{\"frozen\": 0.002, \"normal\": 0.019, \"refrigeration\": 0.01}', '{\"frozen\": 0.042, \"normal\": 0.091, \"refrigeration\": 0.052}', '192', '2');
INSERT INTO `orders` VALUES (8, 'Sp8', '491.99999999999994-768.0', '870', '{\"frozen\": 0.026, \"normal\": 0.023, \"refrigeration\": 0.024}', '{\"frozen\": 0.067, \"normal\": 0.087, \"refrigeration\": 0.099}', '342', '9');
INSERT INTO `orders` VALUES (9, 'Sp9', '540.0-822.0', '888', '{\"frozen\": 0.027, \"normal\": 0.023, \"refrigeration\": 0.013}', '{\"frozen\": 0.074, \"normal\": 0.028, \"refrigeration\": 0.017}', '450', '7');
INSERT INTO `orders` VALUES (10, 'Sp10', '491.99999999999994-822.0', '996.0000000000001', '{\"frozen\": 0.025, \"normal\": 0.017, \"refrigeration\": 0.024}', '{\"frozen\": 0.099, \"normal\": 0.075, \"refrigeration\": 0.084}', '312', '2');
INSERT INTO `orders` VALUES (11, 'Sp11', '312.0-486.0', '588', '{\"frozen\": 0.026, \"refrigeration\": 0.002}', '{\"frozen\": 0.076, \"normal\": 0.033, \"refrigeration\": 0.017}', '245.99999999999997', '4');
INSERT INTO `orders` VALUES (12, 'Sp12', '354.0-654.0', '732', '{\"frozen\": 0.019, \"normal\": 0.028, \"refrigeration\": 0.03}', '{\"frozen\": 0.044, \"normal\": 0.05, \"refrigeration\": 0.034}', '240', '10');
INSERT INTO `orders` VALUES (13, 'Sp13', '276.0-462.0', '570', '{\"frozen\": 0.01, \"normal\": 0.011, \"refrigeration\": 0.02}', '{\"frozen\": 0.077, \"normal\": 0.092, \"refrigeration\": 0.081}', '126', '3');
INSERT INTO `orders` VALUES (14, 'Sp14', '570.0-912.0', '1038', '{\"frozen\": 0.022, \"normal\": 0.015, \"refrigeration\": 0.024}', '{\"frozen\": 0.047, \"normal\": 0.084, \"refrigeration\": 0.028}', '402', '2');
INSERT INTO `orders` VALUES (15, 'Sp15', '372.0-708.0', '780', '{\"frozen\": 0.026, \"normal\": 0.003, \"refrigeration\": 0.005}', '{\"frozen\": 0.085, \"normal\": 0.061, \"refrigeration\": 0.053}', '288', '2');
INSERT INTO `orders` VALUES (16, 'Sp16', '462.0-600.0', '684', '{\"frozen\": 0.02, \"normal\": 0.026, \"refrigeration\": 0.028}', '{\"frozen\": 0.061, \"normal\": 0.031, \"refrigeration\": 0.064}', '396', '2');
INSERT INTO `orders` VALUES (17, 'Sp17', '348.0-462.0', '546', '{\"frozen\": 0.03, \"normal\": 0.014, \"refrigeration\": 0.027}', '{\"frozen\": 0.045, \"normal\": 0.018, \"refrigeration\": 0.047}', '258', '10');
INSERT INTO `orders` VALUES (18, 'Sp18', '228.0-360.0', '516', '{\"frozen\": 0.004, \"normal\": 0.016, \"refrigeration\": 0.019}', '{\"frozen\": 0.047, \"normal\": 0.094, \"refrigeration\": 0.044}', '150', '2');
INSERT INTO `orders` VALUES (19, 'Sp19', '174.0-498.00000000000006', '558', '{\"frozen\": 0.015, \"normal\": 0.015, \"refrigeration\": 0.023}', '{\"frozen\": 0.047, \"normal\": 0.049, \"refrigeration\": 0.058}', '48', '8');
INSERT INTO `orders` VALUES (20, 'Sp20', '438.0-714.0', '852', '{\"frozen\": 0.026, \"normal\": 0.025, \"refrigeration\": 0.016}', '{\"frozen\": 0.073, \"normal\": 0.052, \"refrigeration\": 0.078}', '288', '3');
INSERT INTO `orders` VALUES (21, 'Sp21', '498.00000000000006-768.0', '906', '{\"normal\": 0.019, \"refrigeration\": 0.008}', '{\"frozen\": 0.035, \"normal\": 0.081, \"refrigeration\": 0.081}', '426', '9');
INSERT INTO `orders` VALUES (22, 'Sp22', '288.0-396.0', '504', '{\"frozen\": 0.004, \"normal\": 0.018, \"refrigeration\": 0.024}', '{\"frozen\": 0.031, \"normal\": 0.059, \"refrigeration\": 0.057}', '168', '7');
INSERT INTO `orders` VALUES (23, 'Sp23', '288.0-384.0', '480', '{\"frozen\": 0.005, \"normal\": 0.029, \"refrigeration\": 0.022}', '{\"frozen\": 0.097, \"normal\": 0.089, \"refrigeration\": 0.096}', '144', '6');
INSERT INTO `orders` VALUES (24, 'Sp24', '396.0-576.0', '726', '{\"frozen\": 0.019, \"normal\": 0.004, \"refrigeration\": 0.014}', '{\"frozen\": 0.075, \"normal\": 0.036, \"refrigeration\": 0.093}', '306', '8');
INSERT INTO `orders` VALUES (25, 'Sp25', '402.0-600.0', '678', '{\"frozen\": 0.025, \"normal\": 0.016, \"refrigeration\": 0.027}', '{\"frozen\": 0.064, \"normal\": 0.081, \"refrigeration\": 0.074}', '264', '7');
INSERT INTO `orders` VALUES (26, 'Sp26', '690.0-930.0', '1000', '{\"frozen\": 0.018, \"normal\": 0.011, \"refrigeration\": 0.023}', '{\"frozen\": 0.053, \"normal\": 0.082, \"refrigeration\": 0.05}', '560', '6');
INSERT INTO `orders` VALUES (27, 'Sp27', '396.0-618.0', '714', '{\"frozen\": 0.009, \"normal\": 0.001, \"refrigeration\": 0.013}', '{\"frozen\": 0.025, \"normal\": 0.07, \"refrigeration\": 0.052}', '288', '10');
INSERT INTO `orders` VALUES (28, 'Sp28', '510.0-612.0', '768', '{\"frozen\": 0.008, \"normal\": 0.018, \"refrigeration\": 0.002}', '{\"frozen\": 0.093, \"normal\": 0.055, \"refrigeration\": 0.067}', '372', '3');
INSERT INTO `orders` VALUES (29, 'Sp29', '168.0-372.0', '432', '{\"frozen\": 0.011, \"normal\": 0.007, \"refrigeration\": 0.005}', '{\"frozen\": 0.096, \"normal\": 0.03, \"refrigeration\": 0.074}', '60', '4');
INSERT INTO `orders` VALUES (30, 'Sp30', '174.0-534.0', '606', '{\"frozen\": 0.023, \"normal\": 0.014, \"refrigeration\": 0.004}', '{\"frozen\": 0.035, \"normal\": 0.051, \"refrigeration\": 0.041}', '90', '8');
INSERT INTO `orders` VALUES (31, 'Sp31', '420-810.0', '840', '{\"frozen\": 0.008, \"refrigeration\": 0.016}', '{\"frozen\": 0.099, \"normal\": 0.088, \"refrigeration\": 0.056}', '330', '6');
INSERT INTO `orders` VALUES (32, 'Sp32', '420-570.0', '690', '{\"frozen\": 0.012, \"normal\": 0.002, \"refrigeration\": 0.005}', '{\"frozen\": 0.045, \"normal\": 0.033, \"refrigeration\": 0.072}', '300', '8');
INSERT INTO `orders` VALUES (33, 'Sp33', '690.0-930.0', '1020', '{\"frozen\": 0.028, \"refrigeration\": 0.016}', '{\"frozen\": 0.039, \"normal\": 0.095, \"refrigeration\": 0.068}', '540', '4.5');
INSERT INTO `orders` VALUES (34, 'Sp34', '550.0-640', '730', '{\"frozen\": 0.02, \"normal\": 0.055, \"refrigeration\": 0.04}', '{\"frozen\": 0.028, \"normal\": 0.082, \"refrigeration\": 0.06}', '490', '5');
INSERT INTO `orders` VALUES (35, 'Sp35', '720-840', '1020', '{\"refrigeration\": 0.01}', '{\"frozen\": 0.011, \"normal\": 0.044, \"refrigeration\": 0.054}', '588', '3');
INSERT INTO `orders` VALUES (36, 'Sp36', '540-720', '840', '{\"frozen\": 0.014, \"normal\": 0.003, \"refrigeration\": 0.022}', '{\"frozen\": 0.089, \"normal\": 0.018, \"refrigeration\": 0.035}', '360', '9');
INSERT INTO `orders` VALUES (37, 'Sp37', '540-900', '990', '{\"frozen\": 0.042, \"refrigeration\": 0.026}', '{\"frozen\": 0.067, \"normal\": 0.031, \"refrigeration\": 0.1}', '480', '2.5');
INSERT INTO `orders` VALUES (38, 'Sp38', '840-960', '1050', '{\"frozen\": 0.034}', '{\"frozen\": 0.041, \"normal\": 0.056, \"refrigeration\": 0.06}', '600', '6.5');
INSERT INTO `orders` VALUES (39, 'Sp39', '450.0-690.0', '870', '{\"frozen\": 0.006, \"normal\": 0.015, \"refrigeration\": 0.029}', '{\"frozen\": 0.078, \"normal\": 0.018, \"refrigeration\": 0.066}', '360', '3');
INSERT INTO `orders` VALUES (40, 'Sp40', '720-960', '1020', '{\"frozen\": 0.018, \"normal\": 0.01, \"refrigeration\": 0.002}', '{\"frozen\": 0.035, \"normal\": 0.074, \"refrigeration\": 0.098}', '570', '4');

-- ----------------------------
-- Table structure for stores
-- ----------------------------
DROP TABLE IF EXISTS `stores`;
CREATE TABLE `stores`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 100 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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

SET FOREIGN_KEY_CHECKS = 1;
