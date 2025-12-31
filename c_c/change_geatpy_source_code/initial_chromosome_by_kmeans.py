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
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from tools.MySqlConn import getdata
from run_script import orders_distr
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体

ORDERS, VE, GRAP, GOODS, STORES, BOXES = getdata()
def create_point_to_corr():
    df1 = pd.read_excel("../3DObstacle_avoidance/urban/distance_terrain.xlsx", usecols=['end', 'end_coordinate'])
    df2 = pd.read_excel("../3DObstacle_avoidance/urban/distance_terrain.xlsx", usecols=['start', 'start_coordinate'])
    data_corr1 = df1.drop_duplicates().values.tolist()
    data_corr2 = df2.drop_duplicates().values.tolist()
    data_corr = data_corr1 + data_corr2
    return set(map(tuple, data_corr))

def point_to_corr():
    res_set_point = create_point_to_corr()
    return [
        {"address": point[0], "corr": list(ast.literal_eval(point[1]))[:2]}
        for point in res_set_point
    ]

"""
    拿到40个点
"""
def create_corr(point_to_corr_list):
    return np.array([item["corr"] for item in point_to_corr_list])

"""
    使用KMeans聚类
"""
def work_kmeans():
    # 列表字典 [{"address": point[0], "corr": [corr_list[0], corr_list[1]]}]
    point_to_corr_list = point_to_corr()
    dpet_corr = None
    for datas_ in point_to_corr_list:
        if datas_["address"] == "Sp0":
            dpet_corr = datas_["corr"]
            break
    point_to_corr_list = [item for item in point_to_corr_list if item["address"] != "Sp0"]
    point_to_corr_list_new = sorted(point_to_corr_list, key=lambda x: int(x["address"].replace("Sp", "")))
    points = create_corr(point_to_corr_list_new)
    kmeans = KMeans(n_clusters=4, random_state=23)
    labels = kmeans.fit_predict(points)
    centers = kmeans.cluster_centers_
    target_point = np.array(dpet_corr)
    distances = np.linalg.norm(centers - target_point, axis=1)
    coord_to_address = {tuple(item["corr"]): int(str(item["address"]).split("p")[1]) for item in point_to_corr_list}
    clustered_points = [[] for _ in range(4)]
    for point, label in zip(points, labels):
        point_key = tuple(point)
        clustered_points[label].append(coord_to_address.get(point_key))
    new_list_for_corr = []
    for s in range(len(distances)):
        new_dict_for_corr = {}
        new_dict_for_corr.update({"center": list(centers[s]), "distance": distances[s], "content": clustered_points[s]})
        new_list_for_corr.append(new_dict_for_corr)
    sorted_clusters = sorted(new_list_for_corr, key=lambda x: x['distance'])
    clustered_points_for_return = [items["content"] for items in sorted_clusters]

    # colors = ['red', 'blue', 'green', 'purple']
    # plt.figure(figsize=(8, 6))
    # for i in range(4):
    #     cluster_coords = [point for point, label in zip(points, labels) if label == i]
    #     x = [p[0] for p in cluster_coords]
    #     y = [p[1] for p in cluster_coords]
    #     plt.scatter(x, y, c=colors[i], label=f'Cluster {i}')
    #
    # plt.title('Clustering Results')
    # plt.xlabel('X Coordinate')
    # plt.ylabel('Y Coordinate')
    # plt.legend()
    # plt.grid(False)
    # plt.tight_layout()
    # plt.savefig("Clustering_Results.png", dpi=300, bbox_inches="tight")

    return clustered_points_for_return

def merge_with_separators(lists, separator=0):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(separator)
    return result


def coms(flat_list):
    orders, ve, graph, goods, stores, box = ORDERS, VE, GRAP, GOODS, STORES, BOXES
    ve = sorted(ve, key=lambda x: x['vcapacity'])
    now_order_list = flat_list
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

def generate_ok_chroms(orders_nums, duoshaoge):
    clustered_points = work_kmeans()
    flat_list = [item for sublist in clustered_points for item in sublist]
    order_all_list, ve = coms(flat_list)
    res_fen_datas = orders_distr.fenche(order_all_list, ve)
    res_end_list = []
    if res_fen_datas[0]:
        sorted_res_fen_data = sorted(res_fen_datas[1], key=lambda x: x['vid'])
        for datass in sorted_res_fen_data:
            res_end_list.append(datass['pre_mounted'])
    initial_chroms_listss = []
    for i in range(duoshaoge):
        initial_chroms = []
        for data in res_end_list:
            random.shuffle(data)
            initial_chroms.append(data)
        add_0 = merge_with_separators(initial_chroms, separator=0)
        orders_num = orders_nums + 1
        for sne in range(len(add_0)):
            if add_0[sne] == 0:
                add_0[sne] = orders_num
                orders_num += 1
        initial_chroms_listss.append(add_0)
    return initial_chroms_listss

if __name__ == '__main__':
    print(work_kmeans())