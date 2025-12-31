# -*- coding: utf-8 -*-
"""
@filename:cold_chain_env.py
@Author  : DY
@Software: PyCharm
@Date    : 2025/1/12 15:33
"""
import copy

import numpy as np
import pandas as pd
import json
import os
import math
import uuid
import gym
from dataclasses import dataclass
from utils.common import sum_ve,find_ve_vfuel_by_id_config,order_all_ton,all_fuel,all_back,sum_ve_and_back
from utils.GraphUtil import Graph


add_ton_fule = 0.01
location_one_step = 30
fuel_one_L = 7.2
one_ton_time = 60

@dataclass
class VehicleFulledException(Exception):
    pass


@dataclass
class ItemNotEnoughException(Exception):
    pass


@dataclass
class DistributionException(Exception):
    causer: Exception


@dataclass
class UnloadException(Exception):
    causer: Exception



class ColdChainEnv(gym.Env):
    def __init__(self, config: dict):
        super(ColdChainEnv, self).__init__()
        self.config = config
        self.graph = Graph()
        self.graph.creategraph(self.config["graph"])
        self.reset()

    def reset(self):
        self._steps = []
        self.tick = 0

        self.vehicles = self._initialize_vehicles()
        self.orders = self.config["orders"]
        for order in self.orders:
            order.update({"delivered": False})
            order.update({"satisfaction": 0})
        self.stores = {store["name"]: store.copy() for store in self.config["stores"]}
        for store in self.stores.values():
            store.update(
                {
                    "satisfaction": 0,
                }
            )

    def step(self, action: tuple[str, dict] = None):
        self.tick += 1
        if action:
            action_name, action_config = action
            self._steps.append((action_name, action_config))
            if action_name == "distribution":
                self._handle_distribution(action_config)
            elif action_name == "move":
                self._handle_move(action_config)
            elif action_name == "unload":
                self._handle_unload(action_config)

        return self._get_observation(), 0, True, {}  # TODO: rewards?

    def _initialize_vehicles(self):
        vehicles = []
        for _vehicle in self.config["vehicles"]:
            vehicle = _vehicle.copy()
            vehicle.update(
                {
                    "orders": [],
                    "location": {'0':'WareHouse'},
                    "mounted": [],
                    "mounted_normal": {},
                    "mounted_back": []
                }
            )
            vehicles.append(vehicle)
        return vehicles


    def _vehicle_can_accept_order(self, vehicle, order):
        all_new = 0
        all_back = 0
        all_normal = 0
        need_ = json.loads(order['buyitem'])
        need_back = json.loads(order['nback'])
        for n in need_.keys():
            all_new += need_[n]
        for ton in need_back.values():
            all_back += ton
        if len(vehicle['mounted_normal']) == 0:
            all_normal = 0
        else:
            for v in vehicle['mounted_normal'].values():
                part = str(v).split("-")
                num = float(part[1])
                all_normal += num
        if all_back >= all_new:
            sum_all = sum([box["ton"] for box in vehicle["mounted"]]) + all_normal + all_back
        else:
            sum_all = sum([box["ton"] for box in vehicle["mounted"]]) + all_normal + all_new
        return (
                sum_all <= vehicle["vcapacity"]
        )

    def _vehicle_can_unload(self, vehicle, order):
        buy_item = json.loads(order['buyitem'])
        isok = []
        for k, v in buy_item.items():
            v_list = []
            for box in vehicle['mounted']:
                if box['goodname'] == k and box['store'] == order['address']:
                    v_list.append(box['ton'])
            if sum(v_list) == v:
                isok.append(True)
        return all(isok)


    def _handle_distribution(self, action_config):
        vehicle = self._get_vehicle_by_id(action_config["vehicle_id"])
        for order_id in action_config["order_ids"]:
            order = self._get_order_by_id(order_id)
            if not self._vehicle_can_accept_order(vehicle, order):
                raise DistributionException(VehicleFulledException())
            self._distribute_order_to_vehicle(order, vehicle)
        new_fuel = find_ve_vfuel_by_id_config(self.config["vehicles"],action_config["vehicle_id"]) + sum_ve(vehicle) * add_ton_fule
        vehicle.update({"vfuel": new_fuel})
        all_ton = sum_ve(vehicle)
        vehicle['location'].update({str(all_ton * one_ton_time) + 'min(装货)': 'WareHouse'})

    def _distribute_order_to_vehicle(self, order, vehicle):
        order["delivered"] = False
        address = order['address']
        buy_item = json.loads(order["buyitem"])
        for good_name,good_num in buy_item.items():
            good = self._get_item_by_name(good_name)
            if good['gtype'] == 'frozen' or good['gtype'] == 'refrigeration':
                box = self._get_box_for_item(good)
                if good_num == box['ton']:
                    self._mount_boxes_on_vehicle(1, box["ton"], box, good, vehicle, address)
                shengxiade = good_num % box["ton"]
                self._mount_boxes_on_vehicle(math.ceil(good_num / box["ton"]), shengxiade, box, good, vehicle, address)
            else:
                vehicle['mounted_normal'].update(
                    {address: good_name+'-'+str(good_num)}
                )
        nback = json.loads(order["nback"])
        if len(nback) != 0:
            for good_names, good_nums in nback.items():
                good = self._get_item_by_name(good_names)
                if good['gtype'] == 'frozen' or good['gtype'] == 'refrigeration':
                    box = self._get_box_for_item(good)
                    self._mount_none_boxes_on_vehicle(math.ceil(good_nums / box["ton"]), box, good, vehicle, address)
        vehicle["orders"].append(order)
        vehicle['location'].update({'0': 'WareHouse'})

    def _update_satisfaction(self, order):
        current_time = str(order['need_times']).split('m')[0]
        current_time = float(current_time)
        desired_time_min = str(order['timestage']).split('-')[0]
        desired_time_max = str(order['timestage']).split('-')[1]
        zuizao = float(order["early_time"])
        latest_need_time = order['dtime']
        interval = float(latest_need_time) - float(desired_time_max)
        lowing_rate = 1 / interval
        interval_early = float(desired_time_min) - zuizao
        if interval_early == 0:
            l_r = 10000
        else:
            l_r = 1 / interval_early
        satisfaction = 0
        if current_time > float(latest_need_time) or current_time < float(zuizao):
            satisfaction = 0
        elif float(zuizao) <= current_time < float(desired_time_min):
            satisfaction = 1 - (current_time - float(zuizao)) * l_r
        elif float(desired_time_max) <= current_time <= float(latest_need_time):
            satisfaction = 1 - (current_time - float(desired_time_max)) * lowing_rate
        elif float(desired_time_max) >= current_time >= float(desired_time_min):
            satisfaction = 1
        if satisfaction < 0 or satisfaction > 1:
            satisfaction = 0
        order["satisfaction"] = satisfaction
        self.get_store_by_address(order['address'])['satisfaction'] = satisfaction

    def _get_item_by_name(self, name):
        return next(item for item in self.config["goods"] if item["gname"] == name)

    def _get_box_for_item(self, item):
        #
        return next(
            box
            for box in self.config["box"]
            if box["type"] == item["gtype"]
        )

    def _mount_boxes_on_vehicle(self, box_count, shengxiade, box, good, vehicle,address):
        for cishu in range(int(box_count)):
            box_copy = box.copy()
            item_copy = good.copy()
            box_copy['id'] = str(uuid.uuid4())
            box_copy["goodname"] = item_copy["gname"]
            box_copy["box_types"] = "送货"
            if cishu == int(box_count) - 1:
                box_copy.update({"ton": round(shengxiade, 4)})
                box_copy["orgprice"] = item_copy["gprice"] * shengxiade
                box_copy["curprice"] = item_copy["gprice"] * shengxiade
            else:
                box_copy["orgprice"] = item_copy["gprice"] * box['ton']
                box_copy["curprice"] = item_copy["gprice"] * box['ton']
            box_copy["store"] = address
            if box_copy["ton"] != 0:
                vehicle["mounted"].append(box_copy)

    def _mount_none_boxes_on_vehicle(self, count, box, good, vehicle, address):
        for _ in range(int(count)):
            box_copy = box.copy()
            item_copy = good.copy()
            box_copy['id'] = str(uuid.uuid4())
            box_copy.update({"ton": 0})
            box_copy["goodname"] = item_copy["gname"]
            box_copy["store"] = address
            box_copy["box_types"] = "装退货"
            vehicle["mounted_back"].append(box_copy)

    def _remove_boxes_on_vehicle(self, box_count, item, vehicle):
        boxes_with_target_item = [
            box for box in vehicle["mounted"] if box["item"]["name"] == item["name"]
        ]
        for i in range(box_count):
            vehicle["mounted"].remove(boxes_with_target_item[i])

    def _handle_move(self, action_config):
        vehicle = self._get_vehicle_by_id(action_config["vehicle_id"])
        from_ = list(vehicle['location'].values())[-1]
        orders = self._get_order_by_id(action_config['order_id'])
        if orders:
            self._move_vehicle_to_store(vehicle, from_, orders, action_config['order_id'])

    def _move_vehicle_to_store(self, vehicle, from_, store, order_id):
        all_ton_now = sum_ve_and_back(vehicle)
        speed = vehicle["speed"] - all_ton_now
        target_location = store["address"]
        distance, paths = self.graph.dijkstra(from_, target_location)
        order = self._get_order_by_id(order_id)
        unload_time, upload_time = order_all_ton(order)
        last0 = list(vehicle['location'].keys())[-1].split('m')[0]
        last0 = float(last0)
        order.update({"need_times": str(round(distance / speed * 60, 2) + last0 + unload_time) + 'min'})
        order.update({"fuel": str(round(distance*vehicle['vfuel'], 4)) + 'L'})
        step_num = math.ceil(round(distance / speed * 60, 2) / location_one_step)
        dis_step_one = location_one_step / 60 * speed
        now = 0
        last1 = list(vehicle['location'].keys())[-1].split('m')[0]
        last1 = float(last1)
        for i in range(1, step_num + 1):
            self._corruption_items()
            now += dis_step_one
            if now < distance:
                ns = str(round(now / distance * 100, 2)) + '%' + order['address'] + ' 进度'
                vehicle['location'].update({str(i*location_one_step + last1) + 'min': ns})
            else:
                vehicle['location'].update({str(round(distance / speed * 60 + last1, 2)) + 'min': target_location})

    def _handle_unload(self, action_config):
        vehicle = self._get_vehicle_by_id(action_config["vehicle_id"])
        order = self._get_order_by_id(action_config['order_id'])
        if self._vehicle_can_unload(vehicle, order):
            self._unload_order_from_vehicle(order, vehicle)
        else:
            raise UnloadException(ItemNotEnoughException())

    def _unload_order_from_vehicle(self, order, vehicle):
        unload_time, upload_time = order_all_ton(order)
        last = list(vehicle['location'].keys())[-1].split('m')[0]
        last = float(last)
        address = order["address"]
        filtered_mounted = [item for item in vehicle['mounted'] if item['store'] != address]
        vehicle['mounted'].clear()
        vehicle['mounted'] = filtered_mounted
        vehicle['location'].update({str(last + unload_time) + 'min(卸货过程)': address})
        if address in vehicle['mounted_normal']:
            del vehicle['mounted_normal'][address]

        if len(order['nback']) > 0:
            box_list = self.get_cur_order_back_box(order, vehicle)
            self.update_box_price(vehicle, order, box_list)
            vehicle['location'].update({str(last + unload_time + upload_time) + 'min(装退货过程)': address})
        order.update({"delivered": True})
        last1 = list(vehicle['location'].keys())[-1].split('m')[0]
        last1 = float(last1)
        vehicle['location'].update({str(last1 + float(order["remain_time"])) + 'min(订单完成等待时间)': address})
        new_fuel = find_ve_vfuel_by_id_config(self.config["vehicles"], vehicle['vid']) + sum_ve_and_back(vehicle) * add_ton_fule
        vehicle.update({"vfuel": round(new_fuel, 4)})
        self._update_satisfaction(order)

    def get_cur_order_back_box(self, order, vehicle):
        res_list = []
        for box in vehicle['mounted_back']:
            if box['store'] == order['address']:
                res_list.append(box)
        return res_list
    def update_box_price(self,ve, order, box_list):
        order_back = json.loads(order['nback'])
        for good_name,good_num in order_back.items():
            good = self._get_item_by_name(good_name)
            if good['gtype'] == 'frozen' or good['gtype'] == 'refrigeration':
                frozen_box_list = self.find_frozen_box(good['gtype'], box_list)
                if len(box_list) == 1:
                    frozen_box_list[0].update({"ton": good_num})
                    frozen_box_list[0].update({'orgprice': good["gprice"] * good_num})
                    frozen_box_list[0].update({'curprice': good["gprice"] * good_num})
                else:
                    shengxiade = good_num % 0.05
                    for i in range(len(frozen_box_list)):
                        if i == len(frozen_box_list) - 1 and shengxiade != 0:
                            frozen_box_list[i].update({"ton": shengxiade})
                            frozen_box_list[i].update({'orgprice': good["gprice"] * shengxiade})
                            frozen_box_list[i].update({'curprice': good["gprice"] * shengxiade})
                        else:
                            frozen_box_list[i].update({"ton": 0.05})
                            frozen_box_list[i].update({'orgprice': good["gprice"] * frozen_box_list[i]["ton"]})
                            frozen_box_list[i].update({'curprice': good["gprice"] * frozen_box_list[i]["ton"]})
            else:
                normal_dict = {"goodname": good_name, "store": order['address'], "orgprice": good["gprice"] * good_num,
                               "curprice": good["gprice"] * good_num, "ton": good_num}
                ve["mounted_back"].append(normal_dict)

    def _get_vehicle_by_id(self, vehicle_id):
        return next(vehicle for vehicle in self.vehicles if vehicle["vid"] == vehicle_id)

    def _get_order_by_id(self, order_id):
        return next(order for order in self.orders if order["id"] == order_id)

    def _get_order_by_address(self, address):
        return next(order for order in self.orders if order['address'] == address)

    def get_store_by_address(self,address):
        for k,v in self.stores.items():
            if k == address:
                return v

    def _get_observation(self):
        return {
            "tick": self.tick,
            "orders": self.orders,
            "stores": list(self.stores.values()),
            "vehicles": self.vehicles,
        }

    def _corruption_items(self):
        for vehicle in self.vehicles:
            for box in vehicle["mounted"]:
                goodname = box["goodname"]
                goods = self._get_item_by_name(goodname)
                if box["curprice"] - box["orgprice"] * goods["gcorate"] > 0:
                    box["curprice"] =round(box["curprice"] - box["orgprice"] * goods["gcorate"],2)
                else:
                    box["curprice"] = 0
            for item in vehicle["mounted_back"]:
                if item["curprice"] is not None:
                    goods = self._get_item_by_name(item["goodname"])
                    if item["curprice"] - item["orgprice"] * goods["gcorate"] > 0:
                        item["curprice"] = round(item["curprice"] - item["orgprice"] * goods["gcorate"], 2)
                    else:
                        item["curprice"] = 0

    def used_ve_cost(self,vid):
        vehicle = self._get_vehicle_by_id(vid)
        last = list(vehicle["location"].keys())[-1].split("m")[0]
        address = list(vehicle["location"].values())[-1]
        d, p = self.graph.dijkstra(address, 'WareHouse')
        all_ton_now = sum_ve_and_back(vehicle)
        speed_now = vehicle['speed'] - all_ton_now
        all_time = str(round(float(last) + d / speed_now * 60,2)) + 'min'
        distribution_time = round(float(last),2)
        back_time = round(d / speed_now * 60,2)
        all_fuels = all_fuel(vehicle)
        fuel_back = all_back(vehicle) + find_ve_vfuel_by_id_config(self.config["vehicles"],vid)
        all_ve_cost = round(float(all_fuels + fuel_back * d)*fuel_one_L + vehicle["vcost"] + vehicle["vfix"], 4)
        fuel_cost = round(float(all_fuels + fuel_back * d) * fuel_one_L, 4)
        return all_time, distribution_time, back_time, all_ve_cost, fuel_cost

    def render_all_vehicles(self, methods: str):
        all_time_list = []
        distribution_time_list = []
        back_time_list = []
        all_ve_cost_list = []
        fuel_cost_list = []
        vid_list = []
        maintenance_cost_list = []
        driver_cost = []
        speed_list = []
        ve_capacity_list = []
        for vehicle in self.vehicles:
            all_time, distribution_time, back_time, all_ve_cost, fuel_cost = self.used_ve_cost(vehicle["vid"])
            if all_time != '0.0min':
                all_time_list.append(float(all_time.split('m')[0]))
                distribution_time_list.append(distribution_time)
                back_time_list.append(back_time)
                all_ve_cost_list.append(all_ve_cost)
                fuel_cost_list.append(fuel_cost)
                vid_list.append(vehicle["vid"])
                maintenance_cost_list.append(vehicle["vfix"])
                driver_cost.append(vehicle["vcost"])
                speed_list.append(vehicle["speed"])
                ve_capacity_list.append(vehicle["vcapacity"])

        all_time_list_all = sum(all_time_list)
        distribution_time_list_all = sum(distribution_time_list)
        back_time_list_all = sum(back_time_list)
        all_ve_cost_list_all = sum(all_ve_cost_list)
        fuel_cost_list_all = sum(fuel_cost_list)
        maintenance_cost_list_all = sum(maintenance_cost_list)
        driver_cost_list_all = sum(driver_cost)
        all_time_list.append(all_time_list_all)
        all_time_list.append(all_time_list_all / (len(all_time_list)-1))
        distribution_time_list.append(distribution_time_list_all)
        distribution_time_list.append(distribution_time_list_all / (len(distribution_time_list)-1))
        back_time_list.append(back_time_list_all)
        back_time_list.append(back_time_list_all / (len(back_time_list)-1))
        all_ve_cost_list.append(all_ve_cost_list_all)
        all_ve_cost_list.append(all_ve_cost_list_all / (len(all_ve_cost_list)-1))
        fuel_cost_list.append(fuel_cost_list_all)
        fuel_cost_list.append(fuel_cost_list_all / (len(fuel_cost_list)-1))
        maintenance_cost_list.append(maintenance_cost_list_all)
        maintenance_cost_list.append(maintenance_cost_list_all / (len(maintenance_cost_list)-1))
        driver_cost.append(driver_cost_list_all)
        driver_cost.append(driver_cost_list_all / (len(driver_cost)-1))
        vid_list.append(0)
        vid_list.append(0)
        speed_list.append(0)
        speed_list.append(0)
        ve_capacity_list.append(0)
        ve_capacity_list.append(0)


        data = {
            'vid': vid_list,
            'speed_empty': speed_list,
            'capacity': ve_capacity_list,
            'all_time': all_time_list,
            'distribution_time': distribution_time_list,
            'back_time': back_time_list,
            'all_ve_cost': all_ve_cost_list,
            'fuel_cost': fuel_cost_list,
            'maintenance_cost':maintenance_cost_list,
            'driver_cost': driver_cost
        }
        df = pd.DataFrame(data)
        df.to_excel(f'{methods}.xlsx', index=False)
        return 'ok'

    def all_order_render(self,methods:str):
        oid_list = []
        o_address_list = []
        o_status = []
        o_need_time_list = []
        o_need_fuel_list = []
        o_satisfaction_list = []
        for order in self.orders:
            oid_list.append(order["id"])
            o_address_list.append(order["address"])
            o_status.append("Delivered" if order["delivered"] else "Pending")
            o_need_time_list.append(order["need_times"])
            o_need_fuel_list.append(order["fuel"])
            o_satisfaction_list.append(order["satisfaction"])
        o_satisfaction_list.append(sum(o_satisfaction_list) / len(o_satisfaction_list))
        oid_list.append(0)
        o_address_list.append(0)
        o_status.append(0)
        o_need_time_list.append(0)
        o_need_fuel_list.append(0)
        datas = {
            "订单id": oid_list,
            "订单地址": o_address_list,
            "订单状态": o_status,
            "订单需要时间": o_need_time_list,
            "订单油耗": o_need_fuel_list,
            "订单满意度": o_satisfaction_list
        }
        df = pd.DataFrame(datas)
        df.to_excel(f'{methods}_orders.xlsx', index=False)
        return "ok"

    def render(self, mode="human"):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Tick: {self.tick}")
        print("\nVehicles:")
        for vehicle in self.vehicles:
            orders = ", ".join([str(order["id"]) for order in vehicle["orders"]])
            print(f"  Vehicle {vehicle['vid']} (Type: {vehicle['vtype']}):")
            print(f"    Location: {vehicle['location']}")
            print(f"    Orders: {orders if orders else 'No orders'}")
            print(f"    Mounted Cold Items: {len(vehicle['mounted'])} items")
            print(f'    Mounted Normal Items: {len(vehicle["mounted_normal"])} items')
            if vehicle["mounted"]:
                print(f"    Boxes:")
                for box in vehicle["mounted"]:
                    item_name = box["goodname"]
                    item_count = box["ton"]
                    print(
                        f"      - {item_name}: {item_count}tons (Box ID: {box['id']}, Price: {box['curprice']:.2f}, For:{box['store']})"
                    )
            else:
                print(f"    Boxes: No items loaded.")

            if vehicle['mounted_normal']:
                print("    Normal:")
                for k,v in vehicle['mounted_normal'].items():
                    if isinstance(v, str):
                        item_name = str(v).split('-')[0]
                        item_ton = str(v).split('-')[1]
                        print(
                            f"      - {item_name}: {item_ton}tons (For:{k})"
                        )
                    else:
                        print(
                            f"      - {k}退的 {v}tons货。"
                        )
            else:
                print(f"    Normal: No items loaded.")

        print("\nStores:")
        for store_name, store in self.stores.items():
            print(f"  Store {store_name}:")
            print(f"    Satisfaction: {store['satisfaction']*100:.2f}%")
            print(f"    Address: {store['name']}")

        print("\nOrders:")
        for order in self.orders:
            items = json.loads(order['buyitem'])
            status = "Delivered" if order["delivered"] else "Pending"

            print(f"  Order {order['id']} for Store {order['address']}:")
            print(f"    Status: {status}")
            if 'need_times' in order:
                print(f"    NeedTime: {order['need_times']}")
            if 'fuel' in order:
                print(f"    NeedFuel: {order['fuel']}")
            print(
                f"    Items: {', '.join([item +'(' + str(ton) + 'tons)' for item,ton in items.items()])}"
            )
            print(f"    Desired Time Range(min): {order['timestage']}")
            print(f"    Latest Time(min): {order['dtime']}")

    def find_frozen_box(self, good_type, box_list):
        res_list = []
        for box in box_list:
            if box["type"] == good_type:
                res_list.append(box)
        return res_list