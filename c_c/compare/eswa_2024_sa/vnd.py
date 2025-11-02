# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import random

from compare.eswa_2024_sa.evaluate_for_solution import evaluate_route_cost
from compare.eswa_2024_sa import variation_def, variation_def_vnd


def generate_neighbor(X, op_name, length, mode):
    """

    :param X:
    :param op_name:
    :param length:
    :param mode: intra-route; inter-route
    :return:
    """
    # 例如：
    if op_name == "swap11" and mode == "inter-route":
        return variation_def.variation_swap(X, length)
    elif op_name == "swap22" and mode == "inter-route":
        return variation_def.variation_swap22(X)
    elif op_name == "two_opt" and mode == "inter-route":
        return variation_def.variation_2opt(X)
    elif op_name == "shift10" and mode == "inter-route":
        return variation_def.variation_relocate(X)
    elif op_name == "shift20" and mode == "inter-route":
        return variation_def.variation_shift20(X)
    if op_name == "swap11" and mode == "intra-route":
        return variation_def_vnd.variation_swap_vnd(X, length)
    elif op_name == "swap22" and mode == "intra-route":
        return variation_def_vnd.variation_swap22_vnd(X, length)
    elif op_name == "two_opt" and mode == "intra-route":
        return variation_def_vnd.variation_2opt_vnd(X, length)
    elif op_name == "shift10" and mode == "intra-route":
        return variation_def_vnd.variation_relocate_vnd(X, length)
    elif op_name == "shift20" and mode == "intra-route":
        return variation_def_vnd.variation_shift20_vnd(X, length)

def vnd_stage(current_solution, nls, nni, epsilon, length):
    neighborhoods = ["swap11", "swap22", "two_opt", "shift10", "shift20"]  # 邻域序列
    X = current_solution
    ax, bx, cx = evaluate_route_cost(X)
    cost_X = bx * 0.5 * 1000 + cx * 0.5
    k = 0
    while k < len(neighborhoods):
        op = neighborhoods[k]
        no_improve_cnt = 0
        improved = False
        for i in range(nls):
            Y1 = generate_neighbor(X, op, length, mode="inter-route")
            if Y1 is None:
                Y1 = generate_neighbor(X, op, length, mode="intra-route")
                if Y1 is None:
                    break
            a, b, c = evaluate_route_cost(Y1)
            cost_Y = b * 0.5 * 1000 + c * 0.5
            delta = (cost_Y - cost_X) / max(1e-9, cost_X)  # 相对劣化
            if delta < 0:  # 严格改进
                X, cost_X = Y1, cost_Y
                improved = True
                break
            elif delta <= epsilon and no_improve_cnt < nni:
                X, cost_X = Y1, cost_Y
                no_improve_cnt += 1
            else:
                no_improve_cnt = 0
        if improved:
            k = 0  # 改进则重启
        else:
            k += 1  # 否则换下一个邻域
    enda, endb, endc = evaluate_route_cost(X)
    return X, endb * 0.5 * 1000 + endc * 0.5, [endc, endb]
