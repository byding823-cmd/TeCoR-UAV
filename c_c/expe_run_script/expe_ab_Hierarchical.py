# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import os

from change_geatpy_source_code.fvsd.methods import get_end_data
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'


def get_compare_result():
    return get_end_data()


def plot_xiao_fenceng(res_end_list):
    hhga_cost = res_end_list[1]["成本"]
    hhga_sa = [abs(num) for num in res_end_list[1]["满意度"]]
    hga_cost = res_end_list[0]["成本"]
    hga_sa = [abs(num) for num in res_end_list[0]["满意度"]]
    plt.scatter(hhga_cost, hhga_sa, label="Hierarchical Enhanced GA", color="blue", marker='o')
    plt.scatter(hga_cost, hga_sa, label="Enhanced GA", color="purple", marker='x')
    plt.title("Ablation Experiment Result Figure")
    plt.xlabel("Cost")
    plt.ylabel("Satisfaction")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
               prop={'size': 8}, markerscale=0.8, handlelength=1.5)
    plt.tight_layout()
    plt.subplots_adjust(right=0.75)  # 可选，让右边更宽
    os.makedirs("Ablation_Experiment", exist_ok=True)
    plt.savefig("Ablation_Experiment/xiao_f.png", dpi=300, bbox_inches="tight")  # 保存为PNG
    print("===================二层===================")
    print("最优解 = ", res_end_list[1]["最优目标函数值"])
    print("最优目标函数值 = ", res_end_list[1]["最优解"])
    print("成本 = ", res_end_list[1]["成本"])
    print("满意度 = ", res_end_list[1]["满意度"])
    print("路径 = ", res_end_list[1]["路径"])
    print("===================一层===================")
    print("最优解 = ", res_end_list[0]["最优解"])
    print("最优目标函数值 = ", res_end_list[0]["最优目标函数值"])
    print("成本 = ", res_end_list[0]["成本"])
    print("满意度 = ", res_end_list[0]["满意度"])
    print("路径 = ", res_end_list[0]["路径"])


if __name__ == '__main__':
    res_end_list_fga = get_compare_result()
    plot_xiao_fenceng(res_end_list_fga)

