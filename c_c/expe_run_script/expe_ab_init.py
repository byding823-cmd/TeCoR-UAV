# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import os

from change_geatpy_source_code import only_init, change_low_none_init
from matplotlib import pyplot as plt


def run_xiao_():
    all_component = only_init.run(100)
    xiao_init = change_low_none_init.run(100)
    mab_and_init_cost = all_component["成本"]
    mab_and_init_sa = [abs(num) for num in all_component["满意度"]]

    xiao_init_cost = xiao_init["成本"]
    xiao_init_sa = [abs(num) for num in xiao_init["满意度"]]


    print("==========初始化===============")
    print("best_solution = ", all_component["最优解"])
    print("best_function_values = ", all_component["最优目标函数值"])
    print("routes", all_component["路径"])
    print("cost = ", all_component["成本"])
    print("sa", all_component["满意度"])

    print("===========消去初始化===============")
    print("best_solution = ", xiao_init["最优解"])
    print("best_function_values = ", xiao_init["最优目标函数值"])
    print("routes", xiao_init["路径"])
    print("cost = ", xiao_init["成本"])
    print("sa", xiao_init["满意度"])

    plt.scatter(mab_and_init_cost, mab_and_init_sa, label="low_ga", color="blue", marker='o')
    plt.scatter(xiao_init_cost, xiao_init_sa, label="Removing Population Initialization", color="purple", marker='*')
    plt.title("Ablation Experiment Result Figure")
    plt.xlabel("Cost")
    plt.ylabel("Satisfaction")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               prop={'size': 8}, markerscale=0.8, handlelength=1.5)
    plt.tight_layout()
    plt.subplots_adjust(right=0.75)  # 可选，让右边更宽
    os.makedirs("Ablation_Experiment", exist_ok=True)
    plt.savefig("Ablation_Experiment/xiao_init_result.png", dpi=300, bbox_inches="tight")  # 保存为PNG


if __name__ == '__main__':
    run_xiao_()
