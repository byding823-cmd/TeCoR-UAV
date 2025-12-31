# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import random

import numpy as np
import geatpy as ea

import ps_env
from tools.MySqlConn import getdata
from tools.GraphUtil import Graph
from tools.common import load_config
from tools.return_all_num import return_all_num
from route_planning.fenpian_geatpy.new_temp_nsga2 import moea_NSGA2_templet

globe_order_unm, ve_nums_ = return_all_num()
ORDERS, VE, GRAPHS, GOODS, STORES, BOX = getdata()

def get_shortest_path_distance(start, end):
    graph = Graph()
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    graph.creategraph(graphs)
    route_len, path = graph.dijkstra(start, end)
    return route_len, path


def find_ve_by_id(id):
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    return next(v for v in ve if v["vid"] == id)


def find_order_by_id(id):
    orders, ve, graphs, goods, stores, box = ORDERS, VE, GRAPHS, GOODS, STORES, BOX
    return next(o for o in orders if o["id"] == id)


def com_all_time_and_satisfaction(all_dict):
    need_times = []
    _satisfaction = []
    all_order = all_dict["orders"]
    for item in all_order:
        if 'need_times' in item:
            need_times.append(float(str(item['need_times']).split('m')[0]))
        _satisfaction.append(item['satisfaction'])
    need_time_total = max(need_times)
    _satisfaction_total = round(sum(_satisfaction), 3)
    return need_time_total, _satisfaction_total


def one_order_all_distacne(order_list):
    paths = ["WareHouse"]
    all_distance = 0
    for order_id in order_list:
        order = find_order_by_id(order_id)
        address = order["address"]
        d, p = get_shortest_path_distance(paths[len(paths) - 1], address)
        print(d)
        all_distance += d
        paths.append(address)
    return all_distance

def evaluate_route_cost(route, v_id, order_list):
    route = route.tolist()
    route = [int(x) for x in route]
    route = [order_list[idx] for idx in route]
    all_com = {}
    config = load_config()
    env = ps_env.ColdChainEnv(config)
    action_distribution = ("distribution", {"vehicle_id": v_id, "order_ids": route})
    try:
        observation, reward, done, info = env.step(action_distribution)
    except ps_env.DistributionException as e:
        causer: ps_env.VehicleFulledException = e.causer
    action_distribution_orders = action_distribution[1]['order_ids']
    for i in range(len(action_distribution_orders)):
        orders = env._get_order_by_id(action_distribution_orders[i])
        action_move = ("move", {"vehicle_id": v_id, "order_id": orders['id']})
        observation_move, reward, done, info = env.step(action_move)
        action_unload = ("unload", {"vehicle_id": v_id, "order_id": orders['id']})
        try:
            observation_end, reward, done, info = env.step(action_unload)
            all_com = observation_end
        except ps_env.UnloadException as e:
            causer: ps_env.ItemNotEnoughException = e.causer
    # 计算总距离和总满意度
    need_time_total, all_satisfaction = com_all_time_and_satisfaction(all_com)
    all_cost = 0
    for v in env.vehicles:
        all_time, distribution_time, back_time, all_ve_cost, fuel_cost = env.used_ve_cost(v["vid"])
        if all_time != '0.0min':
            all_cost += all_ve_cost
    return need_time_total, -all_satisfaction, all_cost


class MyProblem(ea.Problem):
    def __init__(self, o_num, v_num, order_list, v_id):
        name = 'MyProblem'  # 问题名称
        M = 2  # 目标维数（双目标）
        maxormins = [1, 1]  # 目标最小化标记列表，1表示最小化，-1表示最大化
        Dim = o_num + v_num - 1  # 决策变量维数（染色体长度）
        varTypes = [1] * Dim  # 决策变量类型，1表示离散型
        lb = [0] * Dim  # 决策变量下界
        ub = [Dim - 1] * Dim  # 决策变量上界（11 代表 0）
        lbin = [1] + [1] * (Dim - 1)  # 决策变量下边界（开头不能为0）
        ubin = [1] * Dim  # 决策变量上边界
        self.order_list = order_list
        self.v_id = v_id
        # 调用父类构造方法
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):
        Vars = pop.Phen  # 获取种群表现型矩阵（染色体）
        pop_size = Vars.shape[0]  # 种群大小
        ObjV = np.zeros((pop_size, self.M))  # 初始化目标函数值矩阵
        for i in range(pop_size):
            chromosome = Vars[i, :]
            need_time_total, all_satisfaction, all_cost = evaluate_route_cost(chromosome, self.v_id, self.order_list)  # 计算适应度值
            ObjV[i, 0] = all_cost  # 第一个目标函数值
            ObjV[i, 1] = all_satisfaction  # 第二个目标函数值
        pop.ObjV = ObjV  # 赋值给种群的目标函数值矩阵

    def calReferObjV(self):
        N = 100  # 生成100个参考点
        Vars = np.zeros((N, self.Dim))
        for i in range(N):
            end_list = [i for i in range(self.Dim)]
            chromosome = np.array(end_list)
            Vars[i, :] = chromosome
        ObjV = np.zeros((N, self.M))
        for i in range(N):
            need_time_total, all_satisfaction, all_cost = evaluate_route_cost(Vars[i, :], self.v_id, self.order_list)
            ObjV[i, 0] = round(all_cost, 2)
            ObjV[i, 1] = round(all_satisfaction, 2)
        return ObjV

def fenpian(ok_chromosome):
    res_data = []
    for i in range(ve_nums_):
        res_data.append([])
    i = 0
    for num in ok_chromosome:
        if num > globe_order_unm or num == 0:
            i += 1
            continue
        else:
            res_data[i].append(num)
    return res_data


def run(aspect_jie, maxgen):
    res_data_list = []
    ok_chromosome = aspect_jie
    fenpian_list = fenpian(ok_chromosome)
    print(fenpian_list)
    i = 1
    for f in fenpian_list:
        if len(f) > 0:
            res_dict = {}
            o_num = len(f)
            v_num = 1
            problem = MyProblem(o_num, v_num, f, i)
            num = len(problem.order_list)
            custom_permutations = [
                [k for k in range(num)]
                for _ in range(5)
            ]
            remaining_count = 50 - len(custom_permutations)
            random_permutations = [np.random.permutation(num).tolist() for _ in range(remaining_count)]
            propopulation = custom_permutations + random_permutations
            random.shuffle(propopulation)
            Fields = np.vstack([
                np.zeros(num, dtype=int),  # 下界（全0）
                np.full(num, num - 1, dtype=int),  # 上界（num-1）
                np.ones(num, dtype=int)
            ])
            prophetPop = ea.Population(Encoding='P', NIND=50, Chrom=np.array(propopulation), Field=Fields)

            # 构建多目标优化算法
            algorithm = moea_NSGA2_templet(
                problem,
                ea.Population(Encoding='P', NIND=50),
                MAXGEN=maxgen,
                logTras=10,
                trappedValue=1e-6,
                maxTrappedCount=10,
                prophetPop=prophetPop,
            )
            res = ea.optimize(
                algorithm,
                verbose=True,
                drawing=0,
                outputMsg=True,
                drawLog=False,
                saveFlag=False
            )
            duiying_list = []
            for ks in range(len(res['ObjV'])):
                duiying_dict = {}
                duiying_dict.update({"target_data": res['ObjV'][ks], "routes": res['Vars'][ks]})
                duiying_list.append(duiying_dict)
            maxormins = np.array([1, 1])
            levels, _ = ea.ndsortESS(res['ObjV'], res['ObjV'].shape[0], None, None, maxormins)
            res_data = []
            for idg, (obj, lvl) in enumerate(zip(res['ObjV'], levels)):
                if lvl == 1.0:
                    res_data.append(list(obj))
            print_res = []
            for igggs in range(len(res_data)):
                for data in duiying_list:
                    res_dictssss = {}
                    if list(data["target_data"]) == res_data[igggs]:
                        res_dictssss.update({"target_data": list(data["target_data"]), "routes": list(data["routes"])})
                        print_res.append(res_dictssss)
                        break
            cost_end = [list_data_["target_data"][0] for list_data_ in print_res]
            sa_end = [list_data_["target_data"][1] for list_data_ in print_res]
            route_end = [list_data_["routes"] for list_data_ in print_res]
            end_check = []
            for m in range(len(cost_end)):
                end_check.append(cost_end[m] * 0.5 + sa_end[m] * 0.5 * 1000)
            best_perm_index = end_check.index(min(end_check))
            res_dict.update({"vid": i})
            best_perm_indices = route_end[best_perm_index]
            best_perm = [problem.order_list[idx] for idx in best_perm_indices]  # 将索引映射到实际值
            res_dict.update({"最优解：": best_perm})
            resssss = [cost_end[best_perm_index], sa_end[best_perm_index]]
            rounded_values = [round(value, 3) for value in resssss]
            res_dict.update({"最优目标函数值：": rounded_values})
            routes = list(route_end)
            all_routes = []
            for route in routes:
                route = list(route)
                best_perm = [problem.order_list[idx] for idx in route]
                all_routes.append(best_perm)
            res_dict.update({"路径": all_routes})
            res_dict.update({"成本": cost_end})
            res_dict.update({"满意度": sa_end})
            res_data_list.append(res_dict)
            i += 1
        else:
            res_dict = {}
            res_dict.update({"vid": i})
            res_dict.update({"最优解：": [0]})
            res_dict.update({"最优目标函数值：": [0, 0]})
            res_data_list.append(res_dict)
            i += 1
            continue

    return res_data_list

def data_opss(datas):
    index = []
    data_list = []
    for data in datas:
        data_dict = {}
        if '路径' in data:
            data_dict['vid'] = data['vid']
            data_dict['length'] = len(data['路径'])
            data_dict['routes'] = data['路径']
            index.append(len(data['路径']))
            data_list.append(data_dict)
        else:
            data_dict['vid'] = data['vid']
            data_dict['length'] = 0
            data_dict['routes'] = []
            data_list.append(data_dict)
    indexs = min(index)
    for da in data_list:
        if da['length'] < indexs:
            # 填充足够的0
            for j in range(indexs):
                da['routes'].append([0])
    # print(data_list)
    end_route_all = []
    for i in range(indexs):
        end_route = []
        for j in range(len(data_list)):
            end_route.extend(data_list[j]['routes'][i])
            if end_route[-1] != 0 and j != len(data_list) - 1:
                end_route.append(0)
        end_route_all.append(end_route)
    return end_route_all


def op_duiqi(end_res):
    daizhevid = []
    for datas in end_res:
        daizheviddict = {}
        if "成本" in datas:
            daizheviddict.update({"vid": datas['vid'], "cost": datas['成本'], "sa": datas["满意度"], "routes": datas['路径']})
            daizhevid.append(daizheviddict)
    data_leagths = [len(c["cost"]) for c in daizhevid]
    max_leagth = max(data_leagths)
    copyed_list = []
    for j in range(len(daizhevid)):
        res_copy_dict = {}
        end_check = [daizhevid[j]["cost"][m] * 0.5 + daizhevid[j]["sa"][m] * 0.5 * 1000 for m in range(len(daizhevid[j]["cost"]))]
        best_perm_index = end_check.index(min(end_check))
        res_copy_dict.update({"vid": daizhevid[j]["vid"], "copys_cost": daizhevid[j]["cost"][best_perm_index], "copys_sa": daizhevid[j]["sa"][best_perm_index], "copys_routes": daizhevid[j]["routes"][best_perm_index]})
        copyed_list.append(res_copy_dict)
    for p in range(len(end_res)):
        if "成本" in end_res[p] and len(end_res[p]['成本']) < max_leagth:
            num_add = max_leagth - len(end_res[p]['成本'])
            # 找到当前对应的vid
            copyed_datass = get_copy_data(copyed_list, end_res[p])
            new_cost_list = num_add * [copyed_datass['copys_cost']]
            new_sa_list = num_add * [copyed_datass['copys_sa']]
            new_routes_list = num_add * [copyed_datass['copys_routes']]
            old_cost_lists = end_res[p]["成本"]
            old_sa_lists = end_res[p]['满意度']
            old_routes_lists = end_res[p]['路径']
            end_res[p].update({"成本": new_cost_list + old_cost_lists, "满意度": new_sa_list + old_sa_lists, "路径": new_routes_list + old_routes_lists})
    return end_res

def get_copy_data(copyed_list, end_resp):
    res_copy_list = None
    for copydata in copyed_list:
        if copydata['vid'] == end_resp['vid']:
            res_copy_list = copydata
            break
    return res_copy_list


def end_run(aspect_jie, maxgen=50):
    end_r = run(aspect_jie, maxgen)
    print("end_r = ", end_r)
    # 对齐解
    end_res_new = op_duiqi(end_r)
    res_dict_return = {}
    end_cost_list = [data['成本'] for data in end_res_new if '成本' in data]
    end_sa_list = [data['满意度'] for data in end_res_new if '满意度' in data]
    summed_sa_lists = [sum(sa) / globe_order_unm for sa in zip(*end_sa_list)]
    summed_lists = [sum(costs) for costs in zip(*end_cost_list)]
    end_route = []
    Goal_function_value = []
    end_value = []
    end_road_ = data_opss(end_res_new)
    for i in range(len(end_res_new)):
        Goal_function_value.append(list(end_res_new[i]['最优目标函数值：']))
        if end_route and end_route[-1] != 0:
            end_route.append(0)
        end_route.extend(end_res_new[i]['最优解：'])
    cost = [item[0] for item in Goal_function_value]
    sati = [item[1] for item in Goal_function_value]
    end_value.append(sum(cost))
    end_value.append(sum(sati) / globe_order_unm)
    print("最终路径 = ", end_route)
    print("最优目标函数值列表 = ", end_value)
    print("合并的帕累托前沿：\n")
    print("成本 = ", summed_lists)
    print("满意度 = ", summed_sa_lists)
    print("路径 = ", end_road_)
    res_dict_return.update(
        {"最优解": end_route, "最优目标函数值": end_value, "路径": end_road_, "成本": summed_lists,
         "满意度": summed_sa_lists})
    return res_dict_return

# if __name__ == '__main__':
#     print(end_run([14, 8, 7, 9, 0, 3, 19, 2, 4, 16, 10, 13, 0, 20, 11, 6, 12, 1, 0, 5, 18, 17, 15], 50))