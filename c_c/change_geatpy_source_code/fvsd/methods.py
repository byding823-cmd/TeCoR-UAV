# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import time
import geatpy as ea
import numpy as np

from change_geatpy_source_code import change_low_
from route_planning.fenpian_geatpy import nsga2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 无头模式
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体

def get_end_data():
    start1 = time.perf_counter()  # 获取开始时间戳
    res_dict_return1 = change_low_.run(maxgen=100)
    end1 = time.perf_counter()  # 获取结束时间戳
    res_dict_return2 = nsga2.end_run(res_dict_return1["最优解"], 50)
    end2 = time.perf_counter()  # 获取结束时间戳

    jie1 = []
    jie2 = []
    for i in range(len(res_dict_return1["成本"])):
        res_dict = {}
        jie1_data = [res_dict_return1["成本"][i], res_dict_return1["满意度"][i]]
        res_dict.update({"jie": jie1_data, "routes": res_dict_return1["路径"][i]})
        jie1.append(res_dict)

    for i in range(len(res_dict_return2["成本"])):
        res_dict = {}
        jie2_data = [res_dict_return2["成本"][i], res_dict_return2["满意度"][i]]
        res_dict.update({"jie": jie2_data, "routes": res_dict_return2["路径"][i]})
        jie2.append(res_dict)

    jies = jie1 + jie2
    Objv_list = [d["jie"] for d in jies]
    ObjV = np.array(Objv_list)
    maxormins = np.array([1, 1])
    levels, _ = ea.ndsortESS(ObjV, ObjV.shape[0], None, None, maxormins)
    res_data = []
    for i, (obj, lvl) in enumerate(zip(ObjV, levels)):
        if lvl == 1.0 or lvl == 2.0:
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
        integrated_cost_satisfaction.append(cost_end[i] * 0.4 + sa_end[i] * 1000 * 0.6)
    min_value = min(integrated_cost_satisfaction)
    min_index = integrated_cost_satisfaction.index(min_value)

    res_end_list = []
    res_end_expe1 = {}
    res_end_expe2 = {}
    res_end_expe1.update({"low_level_times": round(end1 - start1, 4), "最优解": res_dict_return1["最优解"],
                         "最优目标函数值": res_dict_return1["最优目标函数值"],
                         "成本": res_dict_return1["成本"],
                         "满意度": res_dict_return1["满意度"],
                         "路径": res_dict_return1["路径"]
                         })
    res_end_list.append(res_end_expe1)
    res_end_expe2.update({"high_level_times": round(end2 - start1, 4), "最优解": [cost_end[min_index], sa_end[min_index]],
                          "最优目标函数值": route_end[min_index],
                          "成本": cost_end,
                          "满意度": sa_end,
                          "路径": route_end
                          })
    res_end_list.append(res_end_expe2)

    return res_end_list


