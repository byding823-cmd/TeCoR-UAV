# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import random


def variation_swap_vnd(solution, length):
    """
    :param solution:
    :param length: 有效任务id
    :return:
    """
    index_solution = [i for i in range(len(solution))]
    random.shuffle(index_solution)
    index1 = index_solution[0]
    index2 = index_solution[1]
    while solution[index1] > length or solution[index2] > length:
        random.shuffle(index_solution)
        index1 = index_solution[0]
        index2 = index_solution[1]
    solution[index1], solution[index2] = solution[index2], solution[index1]
    return solution


def variation_swap22_vnd(solution, length):
    sol = solution[:]  # 拷贝以免原地修改
    n = len(sol)
    i = random.randint(0, n - 3)
    j = random.randint(0, n - 3)
    while abs(i - j) < 2 or sol[i] > length or sol[i + 1] > length or sol[j] > length or sol[j + 1] > length:
        i = random.randint(0, n - 3)
        j = random.randint(0, n - 3)
    sol[i:i+2], sol[j:j+2] = sol[j:j+2], sol[i:i+2]
    return sol


def variation_relocate_vnd(solution, length):
    source_idx = random.randint(0, len(solution) - 1)
    while solution[source_idx] > length:
        source_idx = random.randint(0, len(solution) - 1)
    target_idx = random.randint(0, len(solution) - 1)
    while target_idx == source_idx or solution[target_idx] > length:
        target_idx = random.randint(0, len(solution) - 1)
    element = solution[source_idx]
    solution.pop(source_idx)
    solution.insert(target_idx, element)
    return solution


def variation_shift20_vnd(solution, length):
    sol = solution[:]
    n = len(sol)
    source_idx = random.randint(0, n - 3)
    while sol[source_idx] > length or sol[source_idx + 1] > length:
        source_idx = random.randint(0, n - 3)
    pair = sol[source_idx:source_idx + 2]
    del sol[source_idx:source_idx + 2]
    target_idx = random.randint(0, len(sol) - 1)
    while target_idx == source_idx or target_idx == source_idx + 1 or sol[target_idx] > length:
        target_idx = random.randint(0, len(sol) - 1)
    for k, v in enumerate(pair):
        sol.insert(target_idx + k, v)
    return sol


def variation_2opt_vnd(solution, length):
    i = random.randint(0, len(solution) - 2)
    j = random.randint(i + 1, len(solution) - 1)
    # 反转
    while any(x > length for x in solution[i:j+1]):
        i = random.randint(0, len(solution) - 2)
        j = random.randint(i + 1, len(solution) - 1)
    solution[i:j + 1] = solution[i:j + 1][::-1]
    return solution
