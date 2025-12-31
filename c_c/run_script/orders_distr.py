# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import json
import random
from tools.GraphUtil import Graph

from tools.MySqlConn import database_op, getdata


def orders_org():
    order_all_list, ve = coms()
    order_ton_sorted_data = sorted(order_all_list, key=lambda x: x['all_ton'])
    ve_sort = sorted(ve, key=lambda x: x['vcapacity'])
    return order_ton_sorted_data, ve_sort


def order_can_not_ve(order, ve):
    pre_mounted_ve = ve['pre_mounted']
    if len(pre_mounted_ve) == 0 and order['all_ton'] <= ve['vcapacity']:
        return True
    else:
        alls = 0
        for id in pre_mounted_ve:
            orders_ = findorderbyid(id)
            alls = alls + orders_['all_ton']
        if alls + order['all_ton'] <= ve['vcapacity']:
            return True
        else:
            return False


def findorderbyid(id):
    order_ton_sorted_data, ve_sort = orders_org()
    return next(o for o in order_ton_sorted_data if o["order_id"] == id)


def remove_orders(order_ton_sorted_data, id):
    for o in order_ton_sorted_data:
        if o['order_id'] == id:
            order_ton_sorted_data.remove(o)
    return order_ton_sorted_data


def fenche(order_s, ve_s):
    i = 0
    j = 0
    now_order = order_s
    for v in ve_s:
        while j < len(now_order):
            if order_can_not_ve(now_order[j], v):
                v['pre_mounted'].append(now_order[j]['order_id'])
                now_order = remove_orders(order_s, now_order[j]['order_id'])
                continue
            else:
                break

    while (i < 10):
        # print(i)
        if len(now_order) == 0:
            break
        if len(now_order) > 0:
            for v in ve_s:
                for order in now_order:
                    if order_can_not_ve(order, v):
                        v['pre_mounted'].append(order['order_id'])
                        now_order = remove_orders(order_s, order['order_id'])
                        continue
                    else:
                        break
        i += 1
    is_ok = False
    if len(now_order) == 0:
        is_ok = True
    res_data = []
    for v in ve_s:
        res_dict = {}
        res_dict.update({'vid': v['vid'], 'pre_mounted': v['pre_mounted']})
        res_data.append(res_dict)
    return is_ok, res_data


# 排序分配
def ve_sort_distribution():
    order_ton_sorted_data, ve_sort = orders_org()
    return fenche(order_ton_sorted_data, ve_sort)


def coms():
    orders, ve, graph, goods, stores, box = getdata()

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


# 顺序分配
def ve_sequence_distribution():
    order_all_list, ve = coms()
    return fenche(order_all_list, ve)


def dislocate_distribution():
    order_all_list, ve = coms()
    random.shuffle(order_all_list)
    random.shuffle(ve)
    return fenche(order_all_list, ve)


def random_distribution_main():
    is_ok, res_data = dislocate_distribution()
    if is_ok:
        return is_ok, res_data
    else:
        i = 0
        while not is_ok:
            is_ok, res_data = dislocate_distribution()
            i += 1
            if is_ok or i > 10:
                break
        return is_ok, res_data


def order_operate(order_all_list):
    graph = Graph()
    orders, ve, graphs, goods, stores, box = getdata()
    graph.creategraph(graphs)
    for order in order_all_list:
        d, p = graph.dijkstra("WareHouse", order['address'])
        order.update({'distance': d})
        order.update({'path': p})
    return order_all_list


def path_distribution():
    order_all_list, ve = coms()
    order_op = order_operate(order_all_list)
    sort_list = sort_by_overlapping_path(order_op)
    return fenche(sort_list, ve)


def sort_by_overlapping_path(data):
    def is_overlapping(path1, path2):
        return path1 == path2[:len(path1)] or path2 == path1[:len(path2)]

    groups = []
    for item in data:
        path = item['path']
        added = False
        for group in groups:
            if any(is_overlapping(path, existing_item['path']) for existing_item in group):
                group.append(item)
                added = True
                break
        if not added:
            groups.append([item])

    for group in groups:
        group.sort(key=lambda x: len(x['path']))
    groups.sort(key=lambda group: group[0]['path'])
    sorted_data = [item for group in groups for item in group]
    return sorted_data


def prior_compute(order_all_list):
    graph = Graph()
    orders, ve, graphs, goods, stores, box = getdata()
    graph.creategraph(graphs)
    all_times = 0
    all_path_distance = 0
    for order in order_all_list:
        need_time_min = str(order['timestage']).split('-')[0]
        all_times += float(need_time_min)
        d, p = graph.dijkstra("WareHouse", order['address'])
        all_path_distance += float(d)
    for order in order_all_list:
        need_time_min = order['timestage'].split('-')[0]
        need_time_rate = round(100 - float(need_time_min) / all_times * 100, 2)
        d, p = graph.dijkstra("WareHouse", order['address'])
        distance_rate = round(d / all_path_distance * 100, 2)
        order.update({'time_rate': need_time_rate})
        order.update({'distance_rate': distance_rate})
    for order in order_all_list:
        order.update({'all_rate': round(order['distance_rate'] * 10 + order['time_rate'], 2)})
    order_return = sorted(order_all_list, key=lambda x: x['all_rate'], reverse=True)
    return order_return


def prior_distribution():
    order_all_list, ve = coms()
    order_new = prior_compute(order_all_list)
    for i in range(len(ve)):
        if order_can_not_ve(order_new[i], ve[i]):
            ve[i]['pre_mounted'].append(order_new[i]['order_id'])
    yiguazai = []
    for v in ve:
        yiguazai = yiguazai + v['pre_mounted']
    for i in range(len(yiguazai)):
        order_new = [d for d in order_new if d.get("order_id") != yiguazai[i]]
    return fenche(order_new, ve)


def geatpy_distribution(geatpy_list):
    count = 0
    order_all_list, ve = coms()
    for n in geatpy_list:
        if n > 0:
            ve[count]['pre_mounted'].append(n)
        elif n == 0:
            count += 1
            continue
    res_list = []
    for v in ve:
        res_dict = {}
        res_dict['vid'] = v['vid']
        res_dict['pre_mounted'] = v['pre_mounted']
        res_list.append(res_dict)
    return res_list


if __name__ == '__main__':
    print("Random = ", random_distribution_main())

    print("SJF = ", ve_sort_distribution())

    print("FIFO = ", ve_sequence_distribution())

    print("Path_dis = ", path_distribution())

    print("Prior = ", prior_distribution())
