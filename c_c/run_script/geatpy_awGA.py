# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""

import ps_env
from tools.common import load_config
from run_script import orders_distr


def main(best_fun):
    # 读配置
    config = load_config()

    # 激活环境
    env = ps_env.ColdChainEnv(config)

    action_distribution_config = orders_distr.geatpy_distribution(best_fun)
    for a in action_distribution_config:
        action_distribution = ("distribution",{"vehicle_id": a['vid'], "order_ids": a['pre_mounted']})
        try:
            observation, reward, done, info = env.step(action_distribution)
        except ps_env.DistributionException as e:
            causer: ps_env.VehicleFulledException = e.causer
        # 根据订单移动
        action_distribution_orders = action_distribution[1]['order_ids']
        for i in range(len(action_distribution_orders)):
            orders = env._get_order_by_id(action_distribution_orders[i])
            action_move = ("move", {"vehicle_id": a['vid'],"order_id": orders['id']})
            observation_move, reward, done, info = env.step(action_move)
            action_unload = ("unload", {"vehicle_id": a['vid'], "order_id": orders['id']})
            try:
                observation, reward, done, info = env.step(action_unload)
            except ps_env.UnloadException as e:
                causer: ps_env.ItemNotEnoughException = e.causer

    print(env.render_all_vehicles("_awGA"))
    print(env.all_order_render("_awGA"))
