# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import ast
import json
import random

import numpy as np
import pandas as pd
from tools.MySqlConn import database_op
def read_xls(store_num):
    df = pd.read_excel(r'E:\code\experiment\really_expe\c_c\c_c\datas\节点间的距离.xls', usecols=range(store_num + 2))
    matrix = df.iloc[:store_num + 1, 1:store_num + 2].to_numpy()
    return matrix if np.allclose(matrix, matrix.T) else "矩阵不是对称的，换个方式处理"

def read_xlsx(what_distance: str):
    df = pd.read_excel("../3DObstacle_avoidance/urban/distance_terrain.xlsx", usecols=['start', 'end', what_distance])
    return df.values
def generation_data(matrix, store_num):
    return [
        {'from': f"Sp{i}", 'to': f"Sp{j}", 'distance': matrix[i, j]}
        for i in range(store_num + 1) for j in range(i)
    ]

def sql_insert_graph():
    now_data = generation_data(read_xls(10), 10)
    i = 1
    for datas in now_data:
        if datas['from'] == 'Sp0':
            datas.update({'from': 'WareHouse'})
        if datas['to'] == 'Sp0':
            datas.update({'to': 'WareHouse'})
        f = datas["from"]
        t = datas["to"]
        w = datas["distance"]
        sqls = "INSERT INTO `graph` (`id`, `gfrom`, `gto`,`weight`) VALUES (%s, %s, %s, %s)"
        database_op(sqls,(i, f, t, w))
        i = i + 1

def sql_insert_graph_con_expe(wwhat_distance: str):
    now_data = read_xlsx(wwhat_distance)
    res_list = []
    for datas in now_data:
        res_dict = {}
        res_dict.update({'from': datas[0], 'to': datas[1], 'distance': round(datas[2], 2)})
        if res_dict['from'] == 'Sp0':
            res_dict.update({'from': 'WareHouse'})
        if res_dict['to'] == 'Sp0':
            res_dict.update({'to': 'WareHouse'})
        res_list.append(res_dict)
    counts = 1
    for res in res_list:
        f = res["from"]
        t = res["to"]
        w = res["distance"]
        sqls = "INSERT INTO `graph` (`id`, `gfrom`, `gto`,`weight`) VALUES (%s, %s, %s, %s)"
        database_op(sqls, (counts, f, t, w))
        counts += 1


def read_orders():
    df = pd.read_excel(r'E:\code\new_expe\new_expe_o3\c_c\datas\order3.xls')
    return df.iloc[2:26, :].to_numpy()

def insert_order():
    order_datas = read_orders()
    for data in order_datas:
        oid = data[0]
        address = f"Sp{int(oid)}"
        order_need_dict = {key: value / 1000 for key, value in zip(['frozen', 'refrigeration', 'normal'], data[1:4]) if
                           value != 0}
        order_back_dict = {key: value / 1000 for key, value in zip(['frozen', 'refrigeration', 'normal'], data[4:7]) if
                           value != 0}

        order_need = json.dumps(order_need_dict)
        order_back = json.dumps(order_back_dict)
        time_list = ast.literal_eval(data[7])
        timestage = f"{time_list[0] * 60}-{time_list[1] * 60}"
        max_time = ast.literal_eval(data[8])
        early_time = max_time[0] * 60
        dtime = max_time[1] * 60
        remain_time = data[9]
        sqls = "INSERT INTO `orders` (`id`, `address`, `timestage`, `dtime`, `nback`, `buyitem`, `early_time`,`remain_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        database_op(sqls, (oid, address, timestage, dtime, order_back, order_need, early_time, remain_time))

def insert_store(store_num):
    for i in range(1, store_num + 1):
        name = f"Sp{i}"
        sqls = "INSERT INTO `stores` (`id`, `name`) VALUES (%s, %s)"
        database_op(sqls, (i, name))

def insert_only_graph(end_num, num):
    # end_num = 最后一个点
    # num = 加多少点？
    for i in range(num):
        weight = random.uniform(10, 99)
        weight = round(weight, 2)
        gfrom = "Sp" + str(end_num + 1)
        if i == 0:
            gto = "WareHouse"
        else:
            gto = "Sp" + str(i)
        print(gfrom, gto, weight)
        sqls = "INSERT INTO `graph` (`gfrom`, `gto`, `weight`) VALUES (%s, %s, %s)"
        database_op(sqls, (gfrom, gto, weight))


# if __name__ == '__main__':
#     sql_insert_graph_con_expe("theo_distance")