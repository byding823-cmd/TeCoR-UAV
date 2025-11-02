# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
from run_script import orders_distr
from compare.EAAI import (get_res)

def merge_with_separators(lists, separator=0):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(separator)
    return result

def allocation_loop():
    return orders_distr.ve_sequence_distribution()


def sorting_and_allocation_loop():
    return orders_distr.ve_sort_distribution()


def limit_and_allocation_loop():
    order_ton_sorted_data, ve_sort = orders_distr.orders_org()
    for i in range(len(ve_sort)):
        if orders_distr.order_can_not_ve(order_ton_sorted_data[i], ve_sort[i]):
            ve_sort[i]['pre_mounted'].append(order_ton_sorted_data[i]['order_id'])
    yiguazai = []
    for v in ve_sort:
        yiguazai = yiguazai + v['pre_mounted']
    for i in range(len(yiguazai)):
        order_ton_sorted_data = [d for d in order_ton_sorted_data if d.get("order_id") != yiguazai[i]]
    return orders_distr.fenche(order_ton_sorted_data, ve_sort)


def back_process(distr_res):
    if distr_res[0]:
        end_dis_list = []
        for data in distr_res[1]:
            end_dis_list.append(data['pre_mounted'])
        merge_res = merge_with_separators(end_dis_list, separator=0)
        return merge_res
    return distr_res[0]


def compute_al_res_data():
    al = back_process(allocation_loop())
    sal = back_process(sorting_and_allocation_loop())
    lal = back_process(limit_and_allocation_loop())
    get_res.main(al, "al")
    get_res.main(sal, "sal")
    get_res.main(lal, "lal")


if __name__ == '__main__':
    compute_al_res_data()


