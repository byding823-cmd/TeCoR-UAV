# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import os

from change_geatpy_source_code import change_low_none_m, low_all_conpoment
from matplotlib import pyplot as plt


def run_xiao_():
    all_component = low_all_conpoment.run(100)
    xiao_m = change_low_none_m.run(100)

    m_and_init_cost = all_component["成本"]
    m_and_init_sa = [abs(num) for num in all_component["满意度"]]

    xiao_m_cost = xiao_m["成本"]
    xiao_m_sa = [abs(num) for num in xiao_m["满意度"]]

    print("==========初始化+M===============")
    print("best_solution = ", all_component["最优解"])
    print("best_function_values = ", all_component["最优目标函数值"])
    print("routes", all_component["路径"])
    print("cost = ", all_component["成本"])
    print("sa", all_component["满意度"])

    print("===========消去M===============")
    print("best_solution = ", xiao_m["最优解"])
    print("best_function_values = ", xiao_m["最优目标函数值"])
    print("routes", xiao_m["路径"])
    print("cost = ", xiao_m["成本"])
    print("sa", xiao_m["满意度"])

    plt.scatter(m_and_init_cost, m_and_init_sa, label="Enhanced GA", color="blue", marker='o')
    plt.scatter(xiao_m_cost, xiao_m_sa, label="Enhanced GA Removal Improvement Operator", color="purple", marker='*')


    plt.title("Ablation Experiment Result Figure")
    plt.xlabel("Cost")
    plt.ylabel("Satisfaction")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               prop={'size': 8}, markerscale=0.8, handlelength=1.5)
    plt.tight_layout()
    plt.subplots_adjust(right=0.75)  # 可选，让右边更宽
    os.makedirs("Ablation_Experiment", exist_ok=True)
    plt.savefig("Ablation_Experiment/result_xiao_op.png", dpi=300, bbox_inches="tight")  # 保存为PNG


if __name__ == '__main__':
    run_xiao_()
