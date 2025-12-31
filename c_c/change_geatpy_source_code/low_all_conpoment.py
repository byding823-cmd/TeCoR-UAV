# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import json
import random
import numpy as np
import geatpy as ea
import ps_env
from run_script import orders_distr
from tools.MySqlConn import getdata
from tools.GraphUtil import Graph
from tools.common import load_config
from tools.return_all_num import return_all_num
from change_geatpy_source_code.moea_NSGA2_tems import moea_NSGA2_templetss


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
    # 将 11 还原为 0
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


def fix_chromosome(chromosome):
    for i in range(1, len(chromosome)):
        if chromosome[i] == 0 and chromosome[i - 1] == 0:
            # 如果发现连续0，则将当前0替换为非0值
            chromosome[i] = random.randint(1, len(chromosome))  # 假设基因的取值范围是 [1, Dim]
    return chromosome


def is_zero_contiune(chromosome):
    for i in range(1, len(chromosome)):
        if chromosome[i] == 0 and chromosome[i - 1] == 0:
            return True
        return False


# 遗传算法适应度评估函数
class MyProblem(ea.Problem):
    def __init__(self, o_num, v_num):
        name = 'MyProblem'
        M = 2
        maxormins = [1, 1]
        Dim = o_num + v_num - 1
        varTypes = [1] * Dim
        lb = [1] * Dim
        ub = [Dim] * Dim
        lbin = [1] + [1] * (Dim - 1)
        ubin = [1] * Dim
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        self.alls_cost = []
        self.alls_satisfaction = []
        self.best_cost = []
        self.best_satisfaction = []

    def aimFunc(self, pop):
        Vars = pop.Phen
        pop_size = Vars.shape[0]
        ObjV = np.zeros((pop_size, self.M))
        for i in range(pop_size):
            chromosome = Vars[i, :]
            need_time_total, all_satisfaction, all_cost = evaluate_route_cost(chromosome)  # 计算适应度值
            ObjV[i, 0] = all_cost
            ObjV[i, 1] = all_satisfaction / order_num_all_
        now_cost = round(np.min(ObjV[:, 0]), 4)
        now_satisfaction = round(np.min(ObjV[:, 1]), 4)
        self.best_cost.append(now_cost if not self.best_cost else min(now_cost, self.best_cost[-1]))
        self.best_satisfaction.append(
            now_satisfaction if not self.best_satisfaction else min(now_satisfaction, self.best_satisfaction[-1]))
        self.alls_cost.append(round(np.min(ObjV[:, 0]), 4))
        self.alls_satisfaction.append(round(np.min(ObjV[:, 1]), 4))
        pop.ObjV = ObjV


class HybridSelection:
    def __init__(self, p_mab=0.2, alpha=1.0, warmup=0.2, warm_mid=0.4, maxgens=100):
        self.p_mab = p_mab
        self.alpha = alpha
        self.mab_selector = MABSelection(alpha=alpha)
        self.warmup = warmup * maxgens
        self.warm_mid = warm_mid * maxgens
        self.count = 0
        self.name = 'HybridSelection'

    def do(self, pop, FitnV):
        self.count += 1
        if self.count <= self.warmup:
            self.mab_selector = MABSelection(alpha=2.0)
            return self.mab_selector.do(pop, FitnV), "mab"  # MAB选择
        if self.warmup < self.count <= self.warm_mid:
            if random.random() < self.p_mab:
                self.mab_selector = MABSelection(alpha=1.0)
                return self.mab_selector.do(pop, FitnV), "mab"  # MAB选择
            else:
                # print("tour is being called!")
                return "tour", "tour"
        if self.count > self.warm_mid:
            # print("tour is being called!")
            return "tour", "tour"


class MABSelection:
    def __init__(self, alpha=1.0, sel_rate=0.5, maximize=False):
        self.alpha = alpha
        self.sel_rate = sel_rate
        self.maximize = maximize
        self.name = 'MABSelection'

    def do(self, pop, FitnV):
        N = pop.sizes
        fitn = (FitnV - np.min(FitnV)) / (np.max(FitnV) - np.min(FitnV) + 1e-6)
        rewards = fitn if self.maximize else (1 - fitn)
        counts = np.ones(N)
        values = rewards.flatten()
        total_counts = np.sum(counts)
        avg_rewards = values / counts
        ucb_values = avg_rewards + self.alpha * np.sqrt(
            np.log(total_counts + 1e-6) / (counts + 1e-6)
        )
        n_select = int(self.sel_rate * N)

        if n_select >= N:
            selected_indices = np.arange(N)
        elif n_select <= 0:
            selected_indices = np.random.choice(np.arange(N), N, replace=False)
        else:
            elite_idx = np.argsort(ucb_values)[-n_select:]
            remain_idx = np.setdiff1d(np.arange(N), elite_idx)

            if len(remain_idx) >= N - n_select:
                rand_idx = np.random.choice(remain_idx, N - n_select, replace=False)
                selected_indices = np.concatenate([elite_idx, rand_idx])
            else:
                selected_indices = elite_idx

        return pop[selected_indices]


def get_ok_chromosomes_random(methods:str):
    if methods == 'sjf':
        res_data = orders_distr.ve_sort_distribution()
    elif methods == 'fifo':
        res_data = orders_distr.ve_sequence_distribution()
    elif methods == 'prior':
        res_data = orders_distr.prior_distribution()
    elif methods == 'path':
        res_data = orders_distr.path_distribution()
    else:
        res_data = orders_distr.random_distribution_main()
    return res_data

def generate_qifashi_chroms(res_data, duoshao):
    all_res_chroms = []
    if res_data[0]:
        sorted_data = sorted(res_data[1], key=lambda x: x['vid'])
        for _ in range(duoshao):
            res_chromosomes = []  # 每轮都初始化一次
            count = order_num_all_
            for i in range(len(sorted_data)):
                new_xulie = sorted_data[i]['pre_mounted'][:]  # 创建副本
                random.shuffle(new_xulie)
                res_chromosomes += new_xulie
                res_chromosomes.append(count + 1)
                count += 1
            all_res_chroms.append(res_chromosomes[:-1])  # 最后一个计数不要了
    return all_res_chroms


def run(maxgen=100):
    problem = MyProblem(order_num_all_, ve_nums)
    lens_chrom = order_num_all_ + ve_nums - 1
    qifashi_sjf = generate_qifashi_chroms(get_ok_chromosomes_random("sjf"), 1)
    qifashi_fifo = generate_qifashi_chroms(get_ok_chromosomes_random("fifo"), 1)
    qifashi_prior = generate_qifashi_chroms(get_ok_chromosomes_random("prior"), 1)
    methods_ok_ = qifashi_prior + qifashi_fifo + qifashi_sjf
    methods_ok_end = methods_ok_ * 16
    for snn in range(50 - len(methods_ok_end)):
        methods_ok_end.append(qifashi_sjf[0])
    Fields = np.vstack([
        np.ones(lens_chrom, dtype=int),  # 下界（全0）
        np.full(lens_chrom, lens_chrom, dtype=int),  # 上界（num-1）
        np.ones(lens_chrom, dtype=int)
    ])
    prophetPop = ea.Population(Encoding='P', NIND=50, Chrom=np.array(methods_ok_end), Field=Fields)
    algorithm = moea_NSGA2_templetss(
        problem,
        ea.Population(Encoding='P', NIND=50),
        MAXGEN=maxgen,
        logTras=10,
        trappedValue=1e-6,
        maxTrappedCount=10,
        prophetPop=prophetPop,
        selectStyle=HybridSelection(0.5, 1.0, 0.1, 0.3, maxgens=maxgen)  # 使用混合选择算子
    )


    res = ea.optimize(
        algorithm,
        verbose=True,
        drawing=0,
        outputMsg=True,
        drawLog=False,
        saveFlag=False,
        parallel=True
    )

    res_dict_return = {}
    route_list = []
    routes_list = list(res['Vars'][0:])
    for item in routes_list:
        routes_now = list(item)
        routes_now_end = [0 if order_num_all_+1 <= x <= order_num_all_ + ve_nums - 1 else x for x in routes_now]
        route_list.append(routes_now_end)
    cost_all_end = list(res['ObjV'][:, 0])
    satisfaction_all_end = list(res['ObjV'][:, 1])
    integrated_cost_satisfaction = []
    for i in range(len(cost_all_end)):
        integrated_cost_satisfaction.append(cost_all_end[i] * 0.4 + satisfaction_all_end[i] * 1000 * 0.6)
    min_value = min(integrated_cost_satisfaction)
    min_index = integrated_cost_satisfaction.index(min_value)
    print('最优解：', route_list[min_index])
    ress = list(res['ObjV'][min_index])
    rounded_values = [round(value, 3) for value in ress]
    print('最优目标函数值：', rounded_values)
    print("路径 = ", route_list)
    print("成本 = ", cost_all_end)
    print("满意度 = ", satisfaction_all_end)
    res_dict_return.update({"最优解": route_list[min_index], "最优目标函数值": rounded_values, "路径": route_list, "成本": cost_all_end, "满意度": satisfaction_all_end})
    return res_dict_return


if __name__ == "__main__":
    run(100)