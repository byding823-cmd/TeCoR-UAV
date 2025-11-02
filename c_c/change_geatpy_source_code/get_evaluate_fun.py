# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import json
import ps_env
from tools.MySqlConn import getdata
from tools.GraphUtil import Graph
from tools.common import load_config
from tools.return_all_num import return_all_num


order_num_all_, ve_nums = return_all_num()
ORDERS, VE, GRAPHS, GOODS, STORES, BOX = getdata()


# 计算最短路径距离(图，起，终)
def get_shortest_path_distance(start, end):
    graph = Graph()
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    graph.creategraph(graphs)
    route_len, path = graph.dijkstra(start, end)
    return route_len, path


def distribution_by_route(route):
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    # 按照染色体分车：
    for v in ve:
        v.update({"pre_mounted": []})
    counts = 0
    for i in range(len(route)):
        # 换车逻辑
        if route[i] > 0:
            ve[counts]["pre_mounted"].append(route[i])
        elif route[i] == 0:
            counts += 1
            continue
    res_data = []
    for v in ve:
        res_dict = {}
        res_dict["vid"] = v["vid"]
        res_dict["pre_mounted"] = v["pre_mounted"]
        res_data.append(res_dict)
    return res_data


def distribution_judgment(distribution_result):
    for i in range(len(distribution_result)):
        pre_mounted = distribution_result[i]["pre_mounted"]
        vid = distribution_result[i]["vid"]
        ve = find_ve_by_id(vid)
        alls = 0
        for order in pre_mounted:
            alls_one = com_all_by_order_id(order)
            alls = alls + alls_one
        if alls <= ve["vcapacity"]:
            distribution_result[i].update({"isok": True})
        else:
            distribution_result[i].update({"isok": False})
    return all(item['isok'] for item in distribution_result)


def com_all_by_order_id(id):
    alls = 0
    order = find_order_by_id(id)
    buy_items = json.loads(order['buyitem'])
    for v in buy_items.values():
        alls += v
    return alls


def find_ve_by_id(id):
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    return next(v for v in ve if v["vid"] == id)


def find_order_by_id(id):
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    return next(o for o in orders if o["id"] == id)


def com_all_time_and_satisfaction(all_dict):
    all_order = all_dict["orders"]
    need_time_total = max(float(str(item['need_times']).split('m')[0]) for item in all_order)
    all_satisfaction = round(sum(item['satisfaction'] for item in all_order), 2)
    return need_time_total, all_satisfaction


def one_order_all_distacne(order_list):
    paths = ["WareHouse"]
    all_distance = 0
    for order_id in order_list:
        order = find_order_by_id(order_id)
        address = order["address"]
        d, p = get_shortest_path_distance(paths[len(paths) - 1], address)
        all_distance += d
        paths.append(address)
    return all_distance


def evaluate_route_cost(route):
    route = route.tolist()
    route = [int(x) for x in route]
    all_com = {}
    all_distance = []
    route = [0 if order_num_all_+1 <= x <= order_num_all_+ve_nums else x for x in route]
    distribution_result = distribution_by_route(route)
    if distribution_judgment(distribution_result):
        config = load_config()
        env = ps_env.ColdChainEnv(config)
        for item in distribution_result:
            all_distance.append(one_order_all_distacne(item['pre_mounted']))
            action_distribution = ("distribution", {"vehicle_id": item['vid'], "order_ids": item['pre_mounted']})
            try:
                observation, reward, done, info = env.step(action_distribution)
            except ps_env.DistributionException as e:
                causer: ps_env.VehicleFulledException = e.causer
            action_distribution_orders = action_distribution[1]['order_ids']
            for i in range(len(action_distribution_orders)):
                orders = env._get_order_by_id(action_distribution_orders[i])
                action_move = ("move", {"vehicle_id": item['vid'], "order_id": orders['id']})
                observation_move, reward, done, info = env.step(action_move)
                action_unload = ("unload", {"vehicle_id": item['vid'], "order_id": orders['id']})
                try:
                    observation_end, reward, done, info = env.step(action_unload)
                    all_com = observation_end
                except ps_env.UnloadException as e:
                    causer: ps_env.ItemNotEnoughException = e.causer
        need_time_total, all_satisfaction = com_all_time_and_satisfaction(all_com)
        all_distances = sum(all_distance)
        all_cost = 0
        for v in env.vehicles:
            all_time, distribution_time, back_time, all_ve_cost, fuel_cost = env.used_ve_cost(v["vid"])
            if all_time != '0.0min':
                all_cost += all_ve_cost
        return need_time_total, -all_satisfaction, all_cost
    else:
        return 10000, 10000, 10000


def get_order_id():
    res_data = []
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    for o in orders:
        res_data.append(o["id"])
    return res_data