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

 Date: 16/12/2025 14:52:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
) ENGINE = InnoDB AUTO_INCREMENT = 250 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

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
INSERT INTO `orders` VALUES (41, 'Sp41', '447-551', '629', '{\"frozen\": 0.028, \"refrigeration\": 0.016}', '{\"frozen\": 0.039, \"normal\": 0.095, \"refrigeration\": 0.068}', '367', '7');
INSERT INTO `orders` VALUES (42, 'Sp42', '206-316', '398', '{\"frozen\": 0.02, \"normal\": 0.055, \"refrigeration\": 0.04}', '{\"frozen\": 0.028, \"normal\": 0.082, \"refrigeration\": 0.06}', '121', '2');
INSERT INTO `orders` VALUES (43, 'Sp43', '547-646', '724', '{\"frozen\": 0.008, \"normal\": 0.018, \"refrigeration\": 0.002}', '{\"frozen\": 0.093, \"normal\": 0.055, \"refrigeration\": 0.067}', '461', '4');
INSERT INTO `orders` VALUES (44, 'Sp44', '571-687', '760', '{\"frozen\": 0.02, \"normal\": 0.026, \"refrigeration\": 0.028}', '{\"frozen\": 0.061, \"normal\": 0.031, \"refrigeration\": 0.064}', '483', '10');
INSERT INTO `orders` VALUES (45, 'Sp45', '261-368', '445', '{\"frozen\": 0.03, \"normal\": 0.014, \"refrigeration\": 0.027}', '{\"frozen\": 0.045, \"normal\": 0.018, \"refrigeration\": 0.047}', '189', '3');
INSERT INTO `orders` VALUES (46, 'Sp46', '175-291', '375', '{\"frozen\": 0.004, \"normal\": 0.016, \"refrigeration\": 0.019}', '{\"frozen\": 0.047, \"normal\": 0.094, \"refrigeration\": 0.044}', '91', '2');
INSERT INTO `orders` VALUES (47, 'Sp47', '452-570', '643', '{\"frozen\": 0.015, \"normal\": 0.015, \"refrigeration\": 0.023}', '{\"frozen\": 0.047, \"normal\": 0.049, \"refrigeration\": 0.058}', '379', '2');
INSERT INTO `orders` VALUES (48, 'Sp48', '95-189', '277', '{\"frozen\": 0.026, \"normal\": 0.025, \"refrigeration\": 0.016}', '{\"frozen\": 0.073, \"normal\": 0.052, \"refrigeration\": 0.078}', '20', '2');
INSERT INTO `orders` VALUES (49, 'Sp49', '579-681', '766', '{\"normal\": 0.019, \"refrigeration\": 0.008}', '{\"frozen\": 0.035, \"normal\": 0.081, \"refrigeration\": 0.081}', '504', '10');
INSERT INTO `orders` VALUES (50, 'Sp50', '296-415', '494', '{\"frozen\": 0.004, \"normal\": 0.018, \"refrigeration\": 0.024}', '{\"frozen\": 0.031, \"normal\": 0.059, \"refrigeration\": 0.057}', '216', '2');

SET FOREIGN_KEY_CHECKS = 1;
