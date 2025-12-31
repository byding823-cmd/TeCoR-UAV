# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import ast
import json
import random

import pandas as pd

from run_script import orders_distr
from tools.MySqlConn import getdata

ORDERS, VE, GRAP, GOODS, STORES, BOXES = getdata()


def coms():
    orders, ve, graph, goods, stores, box = ORDERS, VE, GRAP, GOODS, STORES, BOXES
    now_order_list = create_new_orders()
    now_new_order = []
    for data1 in now_order_list:
        for data2 in orders:
            if data2["id"] == data1:
                now_new_order.append(data2)
                break
    orders = now_new_order.copy()
    order_all_list = []
    for order in orders:
        now_dict = {}
        all = 0
        order_buyitem = json.loads(order['buyitem'])
        for k, v in order_buyitem.items():
            all += v
        now_dict['order_id'] = order['id']
        now_dict['all_ton'] = round(all, 4)
        now_dict['address'] = order['address']
        now_dict['timestage'] = order['timestage']
        now_dict['dtime'] = order['dtime']
        order_all_list.append(now_dict)
    for v in ve:
        v.update({'pre_mounted': []})
    return order_all_list, ve


def create_point_to_corr():
    df = pd.read_excel("../3DObstacle_avoidance/urban/distance_terrain.xlsx", usecols=['end', 'end_coordinate'])
    data_corr = df.values.tolist()
    tuple_data = [tuple(item) for item in data_corr]
    res_set = set(tuple_data)
    return res_set


def get_warehouse_corr():
    df = pd.read_excel("../3DObstacle_avoidance/urban/distance_terrain.xlsx", usecols=['start', 'start_coordinate'])
    data_corr = df.values.tolist()
    warehouse_corr = None
    for item_list in data_corr:
        if item_list[0] == "Sp0":
            warehouse_corr = ast.literal_eval(item_list[1])
            break
    return warehouse_corr[:-1]


def get_quadrant(warehouse_corr):
    if warehouse_corr[0] > 50 and warehouse_corr[1] >= 50:
        return 1
    elif warehouse_corr[0] <= 50 and warehouse_corr[1] > 50:
        return 2
    elif warehouse_corr[0] < 50 and warehouse_corr[1] <= 50:
        return 3
    elif warehouse_corr[0] >= 50 and warehouse_corr[1] < 50:
        return 4
    elif warehouse_corr[0] == 50 and warehouse_corr[1] == 50:
        return 1


def divide_area():
    warehouse_corr = get_warehouse_corr()
    quadrant = get_quadrant(warehouse_corr)
    area_1_o = []
    area_2_o = []
    area_3_o = []
    area_4_o = []
    point_to_corr = create_point_to_corr()
    point_to_corr_list = list(point_to_corr)
    if 15 <= warehouse_corr[0] <= 85 and 15 <= warehouse_corr[1] <= 85:
        for datas in point_to_corr_list:
            if datas[0] != "Sp0":
                corr_list = ast.literal_eval(datas[1])
                if corr_list[0] > warehouse_corr[0] and corr_list[1] >= warehouse_corr[1]:
                    area_1_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] <= warehouse_corr[0] and corr_list[1] > warehouse_corr[1]:
                    area_2_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] < warehouse_corr[0] and corr_list[1] <= warehouse_corr[1]:
                    area_3_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] >= warehouse_corr[0] and corr_list[1] < warehouse_corr[1]:
                    area_4_o.append(int(datas[0].split('p')[1]))
                else:
                    area_1_o.append(int(datas[0].split('p')[1]))
    else:
        for datas in point_to_corr_list:
            if datas[0] != "Sp0":
                corr_list = ast.literal_eval(datas[1])
                if corr_list[0] > 50 and corr_list[1] >= 50:
                    area_1_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] <= 50 < corr_list[1]:
                    area_2_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] < 50 and corr_list[1] <= 50:
                    area_3_o.append(int(datas[0].split('p')[1]))
                elif corr_list[0] >= 50 > corr_list[1]:
                    area_4_o.append(int(datas[0].split('p')[1]))
                else:
                    area_1_o.append(int(datas[0].split('p')[1]))
    if quadrant == 1:
        return area_1_o, area_2_o, area_3_o, area_4_o
    elif quadrant == 2:
        return area_2_o, area_3_o, area_4_o, area_1_o
    elif quadrant == 3:
        return area_3_o, area_4_o, area_1_o, area_2_o
    else:
        return area_4_o, area_1_o, area_2_o, area_3_o


def create_new_orders():
    area_1_o, area_2_o, area_3_o, area_4_o = divide_area()
    now_order_id_list = area_1_o + area_2_o + area_3_o + area_4_o
    return now_order_id_list


def create_initial_chrom_ready():
    order_all_list, ve = coms()
    ve_sort = sorted(ve, key=lambda x: x['vcapacity'])
    res_fen_data = orders_distr.fenche(order_all_list, ve_sort)
    res_end_list = []
    if res_fen_data[0]:
        ve_sort = sorted(res_fen_data[1], key=lambda x: x['vid'])
        for datass in ve_sort:
            res_end_list.append(datass['pre_mounted'])
    return res_end_list


def merge_with_separators(lists, separator=0):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(separator)
    return result


def get_end_initial_chrom(nnid, orders_all_nums_):
    create_initial_chrom_ready_list = create_initial_chrom_ready()
    initial_chroms_list = []
    for i in range(nnid):
        initial_chroms = []
        for data in create_initial_chrom_ready_list:
            random.shuffle(data)
            initial_chroms.append(data)
        add_0 = merge_with_separators(initial_chroms, separator=0)
        orders_num = orders_all_nums_ + 1
        for sne in range(len(add_0)):
            if add_0[sne] == 0:
                add_0[sne] = orders_num
                orders_num += 1
        initial_chroms_list.append(add_0)

    return initial_chroms_list
