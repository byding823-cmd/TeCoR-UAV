# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import ast
import json
import math
import random
import re

import numpy as np
import pandas as pd
from compare.eswa_2024_sa.evaluate_for_solution import evaluate_route_cost
from tools.MySqlConn import getdata

ORDERS, VE, GRAPHS, GOODS, STORES, BOXES = getdata()


def create_task_point_to_corr():
    df = pd.read_excel("../../3D路径规划/平面柱体情况/distance_terrain.xlsx", usecols=['end', 'end_coordinate'])
    data_corr = df.values.tolist()
    tuple_data = [tuple(item) for item in data_corr]
    res_set = set(tuple_data)
    return res_set


def get_warehouse_corr():
    df = pd.read_excel("../../3D路径规划/平面柱体情况/distance_terrain.xlsx", usecols=['start', 'start_coordinate'])
    data_corr = df.values.tolist()
    warehouse_corr = None
    for item_list in data_corr:
        if item_list[0] == "Sp0":
            warehouse_corr = ast.literal_eval(item_list[1])
            break
    return warehouse_corr


def sort_create_task_point_to_corr_res(res_set):
    data_list = list(res_set)
    sorted_list = sorted(
        data_list,
        key=lambda x: int(re.search(r'Sp(\d+)', x[0]).group(1))
    )
    return sorted_list


def euclid(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2])


def get_user_list(corr_list_set):
    res_dict = {}
    for item in corr_list_set:
        res_dict.update({int(item[0][2:]): ast.literal_eval(item[1])})
    return res_dict


def com_all_by_order_id(order):
    return max(
        sum(json.loads(order['buyitem']).values()),
        sum(json.loads(order['nback']).values())
    )


def get_user_demand():
    res_dict = {}
    for item in ORDERS:
        res_dict.update({int(item["id"]): round(com_all_by_order_id(item), 3)})
    return res_dict


def get_uav_capacity():
    return [
        datas["vcapacity"]
        for datas in VE
    ]


def init_nn_chromosome_single_depot(depot_xy, cust_xy, demand, m_vehicles, q, r_top=3):
    users = set(cust_xy.keys())
    chrom = []
    used = 0

    while users and used < m_vehicles:
        load = 0.0
        cur_xy = depot_xy
        while True and users:
            cur_xys = cur_xy.copy()
            feas = [k for k in users if load + demand[k] <= q[used]]
            if not feas:
                break
            feas.sort(key=lambda k: euclid(cur_xys, cust_xy[k]))
            pick_from = feas[:min(r_top, len(feas))]
            k = random.choice(pick_from)
            chrom.append(k)
            users.remove(k)
            load += demand[k]
            cur_xys = cust_xy[k]
            if not users:
                break
        used += 1
        if users and used < m_vehicles:
            chrom.append(0)

    if users:
        return None
    if len(chrom) < len(cust_xy) + len(q) - 1:
        counts = len(cust_xy) + len(q) - 1 - len(chrom)
        for _ in range(counts):
            chrom.append(0)
    countssss = len(cust_xy)
    for sne in range(len(chrom)):
        if chrom[sne] == 0:
            countssss += 1
            chrom[sne] = countssss
    return chrom


def get_candidate_solution(k):
    return [
        init_nn_chromosome_single_depot(get_warehouse_corr(),
                                        get_user_list(sort_create_task_point_to_corr_res(create_task_point_to_corr())),
                                        get_user_demand(),
                                        8,
                                        get_uav_capacity(),
                                        3)
        for _ in range(k)
    ]


def get_best_init_solution(res_candidate_solution):
    res_score = []
    for datas in res_candidate_solution:
        need_time, satisfaction, cost = evaluate_route_cost(datas)
        res_score.append(satisfaction * 0.5 * 1000 + cost * 0.5)
    min_index = res_score.index(min(res_score))
    return res_candidate_solution[min_index]
