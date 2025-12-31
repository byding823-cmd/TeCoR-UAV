# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import json
from envs.evalute_reward import evaluate_route_cost
from envs.drone_env_new import decode_actions


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到")
    except json.JSONDecodeError:
        print(f"错误: 文件 '{file_path}' 不是有效的JSON格式")
    except Exception as e:
        print(f"读取文件时发生错误: {str(e)}")
    return None


if __name__ == '__main__':
    json_data = read_json_file("../best_actions.json")
    print(decode_actions(json_data[-1]))
    need_time, sa, cost = evaluate_route_cost(decode_actions(json_data[-1]))
    print("cost = ", cost)
    print("need_time = ", need_time)
    print("sa = ", sa)
