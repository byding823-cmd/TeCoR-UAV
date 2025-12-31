# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
from tools import data_insert
from change_geatpy_source_code.fcsf import methods_expe1
from run_script.geatpy_awGA import main
from tools.MySqlConn import database_op

def main_run1():
    data_insert.sql_insert_graph_con_expe("theo_distance")

def main_run2():
    best_, best_fun = methods_expe1.get_end_data()
    print("最优解 = ", best_)
    print("最优目标函数 = ", best_fun)
    return best_, best_fun

def main_run3():
    database_op("DELETE FROM graph")
    data_insert.sql_insert_graph_con_expe("real_distance")

def main_run4(best_fun):
    main(best_fun)

if __name__ == '__main__':
    # database_op("DELETE FROM graph")

    # 插入理论距离
    # main_run1()

    # 根据理论距离运行
    # print(main_run2())

    # 删除理论加入真实距离
    # main_run3()

    main_run4([11, 19, 15, 2, 33, 0, 23, 28, 39, 27, 4, 0, 31, 34, 30, 9, 16, 32, 38, 0, 21, 20, 22, 6, 37, 36, 26, 0, 10, 12, 8, 25, 1, 7, 5, 3, 0, 17, 13, 24, 40, 29, 18, 35, 14])


