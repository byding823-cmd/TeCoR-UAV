# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import geatpy as ea
import numpy as np

from change_geatpy_source_code import change_low_
from route_planning.fenpian_geatpy import nsga2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 无头模式
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体

def get_end_data():
    res_dict_return1 = change_low_.run(maxgen=100)
    res_dict_return2 = nsga2.end_run(res_dict_return1["最优解"], 50)

    jie1 = []
    jie2 = []
    for i in range(len(res_dict_return1["成本"])):
        res_dict = {}
        jie1_data = [res_dict_return1["成本"][i], res_dict_return1["满意度"][i]]
        res_dict.update({"jie": jie1_data, "routes": res_dict_return1["路径"][i]})
        jie1.append(res_dict)

    for j in range(len(res_dict_return2["成本"])):
        res_dict = {}
        jie2_data = [res_dict_return2["成本"][j], res_dict_return2["满意度"][j]]
        res_dict.update({"jie": jie2_data, "routes": res_dict_return2["路径"][j]})
        jie2.append(res_dict)

    jies = jie1 + jie2
    Objv_list = [d["jie"] for d in jies]
    ObjV = np.array(Objv_list)
    maxormins = np.array([1, 1])
    levels, _ = ea.ndsortESS(ObjV, ObjV.shape[0], None, None, maxormins)
    res_data = []
    for i, (obj, lvl) in enumerate(zip(ObjV, levels)):
        if lvl == 1.0:
            res_data.append(list(obj))
    print_res = []
    for i in range(len(res_data)):
        for data in jies:
            res_dicts = {}
            if data["jie"] == res_data[i]:
                res_dicts.update({"jie": data["jie"], "routes": data["routes"]})
                print_res.append(res_dicts)
                break
    cost_end = [list_data["jie"][0] for list_data in print_res]
    sa_end = [list_data["jie"][1] for list_data in print_res]
    route_end = [list_data["routes"] for list_data in print_res]

    integrated_cost_satisfaction = []
    for i in range(len(cost_end)):
        integrated_cost_satisfaction.append(cost_end[i] * 0.5 + sa_end[i] * 1000 * 0.5)
    min_value = min(integrated_cost_satisfaction)
    min_index = integrated_cost_satisfaction.index(min_value)

    print("===================一层===================")
    print("最优解 = ", res_dict_return1["最优解"])
    print("最优目标函数值 = ", res_dict_return1["最优目标函数值"])
    print("成本 = ", res_dict_return1["成本"])
    print("满意度 = ", res_dict_return1["满意度"])
    print("路径 = ", res_dict_return1["路径"])
    print("===================二层===================")
    print("最优解 = ", [cost_end[min_index], sa_end[min_index]])
    print("最优目标函数值 = ", route_end[min_index])
    print("成本 = ", cost_end)
    print("满意度 = ", sa_end)
    print("路径 = ", route_end)

    # # 绘制帕累托前沿
    # cost_n = res_dict_return1["成本"]
    # satisfaction_n = [abs(num) for num in res_dict_return1["满意度"]]
    #
    # cost_uu = cost_end
    # satisfaction_uu = [abs(num) for num in sa_end]

    # plt.scatter(cost_n, satisfaction_n, label="单层改进遗传算法", color="blue", marker='o')
    # plt.scatter(cost_uu, satisfaction_uu, label="分层改进遗传算法", color='red', marker='x')
    #
    # plt.title("分层改进遗传算法 vs 单层改进遗传算法")
    # plt.xlabel("成本")
    # plt.ylabel("满意度")
    # plt.legend()
    # plt.savefig("两层 vs 一层1.png", dpi=300, bbox_inches="tight")
    # print("图形已保存为 两层 vs 一层1.png")
    return [cost_end[min_index], sa_end[min_index]], route_end[min_index]

if __name__ == '__main__':
    get_end_data()

