# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import ast
import json
import os
import re
import pandas as pd
import yaml

from scripts.train_new import train
from utils.Mysql import getdata

ORDERS, VE, GRAPH, GOODS, STORES, BOX = getdata()


def order_all_ton_new(order: dict) -> float:
    buy_items = json.loads(order['buyitem'])
    back_items = json.loads(order['nback'])
    total_buy = sum(buy_items.values())
    total_back = sum(back_items.values())
    return max(total_buy, total_back)


def create_point_to_corr():
    df1 = pd.read_excel("corr_data/distance.xlsx", usecols=['start', 'start_coordinate'])
    df2 = pd.read_excel("corr_data/distance.xlsx", usecols=['end', 'end_coordinate'])
    data_corr1 = df1.values.tolist()
    data_corr2 = df2.values.tolist()
    tuple_data1 = [tuple(item) for item in data_corr1]
    tuple_data2 = [tuple(item) for item in data_corr2]
    tuple_data = tuple_data1 + tuple_data2
    res_sets = set(tuple_data)
    res_data = [
        (dat[0], ast.literal_eval(dat[1])[:2])
        for dat in res_sets
    ]
    return sorted(res_data, key=lambda x: int(re.search(r'Sp(\d+)', x[0]).group(1)))


def load_config():
    orders, ve, graph, goods, stores, box = ORDERS, VE, GRAPH, GOODS, STORES, BOX
    uav_list = [
        {"vid": uav["vid"], "capacity": uav["vcapacity"]}
        for uav in ve
    ]

    corr_res = create_point_to_corr()

    task_list = [
        {"tid": ta["id"], "need": order_all_ton_new(ta), "t_corr": corr_res[ta["id"]][1]}
        for ta in orders
    ]
    return task_list, uav_list, corr_res[0][1]


def load_config_mappo(path):
    project_root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_root, path)
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


if __name__ == '__main__':
    env_config = load_config()
    train(env_config)