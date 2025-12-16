# -*- coding: utf-8 -*-
"""
@filename:common.py
@Author  : DY
@Software: PyCharm
@Date    : 2025/1/12 19:03
"""
import json
from tools import MySqlConn

add_ton_fule = 0.01
down_up_one_ton_min = 60
def load_config():
    config = {}
    orders, vehicles, graph, goods,stores,box = MySqlConn.getdata()
    config["orders"] = orders
    config["vehicles"] = vehicles
    config["graph"] = graph
    config["goods"] = goods
    config["stores"] = stores
    config["box"] = box
    return config

def sum_ve(ve):
    all = 0
    all_orders = ve["orders"]
    for item in all_orders:
        if item['delivered'] == False:
            buyitem_order = json.loads(item["buyitem"])
            for v in buyitem_order.values():
                all = all + v
    return all

def sum_ve_and_back(ve):
    song = sum_ve(ve)
    tui = 0
    for backs in ve["mounted_back"]:
        tui = tui + backs['ton']
    return song + tui



def find_ve_vfuel_by_id_config(vehicles,ve_id):
    or_vehicle = next(ve for ve in vehicles if ve['vid'] == ve_id)
    return or_vehicle['vfuel']

def order_all_ton(order):
    all_ton_up = 0
    all_ton_down = 0
    buyitem_order = json.loads(order['buyitem'])
    for v in buyitem_order.values():
        all_ton_up += v
    back_item = json.loads(order['nback'])
    for t in back_item.values():
        all_ton_down += t
    return all_ton_up * down_up_one_ton_min, all_ton_down * down_up_one_ton_min

def all_fuel(ve):
    all_fuel = 0
    for order in ve['orders']:
        all_fuel += float(order['fuel'].split('L')[0])
    return all_fuel

def all_back(ve):
    all_back = 0
    for item in ve['mounted_back']:
        if item['curprice'] is not None:
            all_back += float(item['ton'])
    return all_back * add_ton_fule




