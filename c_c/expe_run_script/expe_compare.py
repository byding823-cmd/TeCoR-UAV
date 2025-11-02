# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import os

from change_geatpy_source_code.fvsd.methods import get_end_data
from route_planning.get_cost_and_sa_data import new_awGA, new_nsga2, new_nsga3
from compare.eswa_ga.main_run import run
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def get_compare_result():
    res_end_list_fga = get_end_data()
    eswa_res_end_list = run(100)
    res_end_awga = new_awGA.run(100)
    res_end_nsga2 = new_nsga2.run(100)
    res_end_nsga3 = new_nsga3.run(100)

    hega_cost = res_end_list_fga[1]["成本"]
    hega_sa = [abs(num) for num in res_end_list_fga[1]["满意度"]]

    eswa_cost = eswa_res_end_list["成本"]
    eswa_sa = [abs(num) for num in eswa_res_end_list["满意度"]]

    awga_cost = res_end_awga["成本"]
    awga_sa = [abs(num) for num in res_end_awga["满意度"]]

    nsga2_cost = res_end_nsga2["成本"]
    nsga2_sa = [abs(num) for num in res_end_nsga2["满意度"]]

    nsga3_cost = res_end_nsga3["成本"]
    nsga3_sa = [abs(num) for num in res_end_nsga3["满意度"]]

    print("===================propose===================")
    print("最优解 = ", res_end_list_fga[1]["最优目标函数值"])
    print("最优目标函数值 = ", res_end_list_fga[1]["最优解"])
    print("成本 = ", res_end_list_fga[1]["成本"])
    print("满意度 = ", res_end_list_fga[1]["满意度"])
    print("路径 = ", res_end_list_fga[1]["路径"])
    print("===================awga===================")
    print("最优解 = ", res_end_awga["最优目标函数值"])
    print("最优目标函数值 = ", res_end_awga["最优解"])
    print("成本 = ", res_end_awga["成本"])
    print("满意度 = ", res_end_awga["满意度"])
    print("路径 = ", res_end_awga["路径"])
    print("===================nsga2===================")
    print("最优解 = ", res_end_nsga2["最优目标函数值"])
    print("最优目标函数值 = ", res_end_nsga2["最优解"])
    print("成本 = ", res_end_nsga2["成本"])
    print("满意度 = ", res_end_nsga2["满意度"])
    print("路径 = ", res_end_nsga2["路径"])
    print("===================nsga3===================")
    print("最优解 = ", res_end_nsga3["最优目标函数值"])
    print("最优目标函数值 = ", res_end_nsga3["最优解"])
    print("成本 = ", res_end_nsga3["成本"])
    print("满意度 = ", res_end_nsga3["满意度"])
    print("路径 = ", res_end_nsga3["路径"])
    print("============eswa=============")
    print("解 = ", eswa_res_end_list["最优解"])
    print("目标函数 = ", eswa_res_end_list["最优目标函数值"])
    print("成本 = ", eswa_cost)
    print("服务质量 = ", eswa_sa)

    plt.scatter(hega_cost, hega_sa, label="propose", color="red", marker='o')
    plt.scatter(eswa_cost, eswa_sa, label="NSGA-II-VRPD", color="blue", marker='s')
    plt.scatter(awga_cost, awga_sa, label="awGA", color="green", marker='^')
    plt.scatter(nsga2_cost, nsga2_sa, label="NSGA-II", color="#9467bd", marker='v')
    plt.scatter(nsga3_cost, nsga3_sa, label="NSGA-III", color="orange", marker='D')

    plt.title("Comparison of different algorithms")
    plt.xlabel("Cost")
    plt.ylabel("Satisfaction")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               prop={'size': 8}, markerscale=0.8, handlelength=1.5)
    plt.tight_layout()
    plt.subplots_adjust(right=0.75)  # 可选，让右边更宽
    os.makedirs("expe_comp", exist_ok=True)
    plt.savefig("expe_comp/res.png", dpi=300, bbox_inches="tight")  # 保存为PNG
    plt.clf()
    return res_end_list_fga


if __name__ == '__main__':
    res_end_list_fga = get_compare_result()

