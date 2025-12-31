# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""

import math
import random
import time
from tools.MySqlConn import getdata
from compare.eswa_2024_sa import init_tools, evaluate_for_solution, vnd, variation_def

ORDERS, VE, GRAPHS, GOODS, STORES, BOXES = getdata()


def initial_solution():
    return init_tools.get_best_init_solution(init_tools.get_candidate_solution(20))


def variation_function(solution):
    neighborhoods = ["swap11", "swap22", "two_opt", "shift10", "shift20"]
    selected = random.choice(neighborhoods)
    if selected == "swap11":
        new_solution = variation_def.variation_swap(solution, len(ORDERS))
    elif selected == "swap22":
        new_solution = variation_def.variation_swap22(solution)
    elif selected == "two_opt":
        new_solution = variation_def.variation_2opt(solution)
    elif selected == "shift10":
        new_solution = variation_def.variation_relocate(solution)
    elif selected == "shift20":
        new_solution = variation_def.variation_shift20(solution)
    else:
        new_solution = solution
    need_time1, satisfaction1, cost1 = evaluate_for_solution.evaluate_route_cost(new_solution)
    if need_time1 == 10000:
        return solution
    else:
        return new_solution


def simulated_annealing(max_iterations_per_temp: int, initial_temp, final_temp, nls, nni, epsilon):
    # 初始化
    current_solution = initial_solution()
    need_time, satisfaction, cost = evaluate_for_solution.evaluate_route_cost(current_solution)
    current_score = satisfaction * 0.5 * 1000 + cost * 0.5
    current_two_target = [cost, satisfaction]

    best_solution = current_solution.copy()
    best_score = current_score
    best_two_target = current_two_target.copy()

    T = initial_temp
    iterations = 0

    while T > final_temp:
        print(f"======第{iterations}代=======")
        print(f"当前最优解 = {best_solution}")
        print(f"最优双目标 = {best_two_target}")
        print(f"当前解 = {current_solution}")
        print(f"当前目标值 = {current_two_target}")

        for _ in range(max_iterations_per_temp):
            new_solution = variation_function(current_solution)
            need_time, satisfaction, cost = evaluate_for_solution.evaluate_route_cost(new_solution)
            new_score = satisfaction * 0.5 * 1000 + cost * 0.5
            new_two_target = [cost, satisfaction]
            delta = new_score - current_score  # <0 表示更好
            if delta < 0 or random.random() < math.exp(-delta / max(T, 1e-12)):
                current_solution = new_solution
                current_score = new_score
                current_two_target = new_two_target

                if current_score < best_score:
                    best_solution = current_solution.copy()
                    best_score = current_score
                    best_two_target = current_two_target.copy()

                if delta < 0:
                    cur_sol_vnd, cur_score_vnd, cur_two_target_vnd = vnd.vnd_stage(
                        current_solution, nls, nni, epsilon, len(ORDERS)
                    )
                    if cur_score_vnd < current_score:
                        current_solution = cur_sol_vnd
                        current_score = cur_score_vnd
                        current_two_target = cur_two_target_vnd

                        if current_score < best_score:
                            best_solution = current_solution.copy()
                            best_score = current_score
                            best_two_target = current_two_target.copy()

        T *= 0.997
        iterations += 1

    return best_solution, best_two_target


if __name__ == '__main__':
    start1 = time.perf_counter()
    best_solution, best_two_target = simulated_annealing(10000, 50, 35, 45, 7, 0.015)
    end_time = time.perf_counter()
    print("最优解 = ", best_solution)
    print("最优目标函数值 = ", best_two_target)
    print(f"函数执行耗时: {end_time - start1:.4f} 秒")
