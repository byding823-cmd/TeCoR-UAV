# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""


def plot_duibi():
    # hhga
    成本1b = [2817.7552, 2834.2072000000003, 2817.7552, 2638.3195, 2534.4932000000003, 2556.2558, 2526.8059000000003,
              2509.7587, 2499.2110999999995, 2469.9055, 2552.264, 2414.7019, 2519.5135, 2442.6470000000004,
              2421.5086999999994, 2442.4284000000002, 2502.2970000000005, 2431.0716, 2431.7538999999997, 2439.3712,
              2488.214, 2425.7212, 2430.6289, 2404.8293000000003, 2478.844, 2373.2185]
    满意度1b = [-0.7034, -0.7336, -0.7034, -0.70054, -0.69836, -0.7157800000000001, -0.70392, -0.7001999999999999,
                -0.67494, -0.64866, -0.70522, -0.5529600000000001, -0.67876, -0.63852, -0.56392, -0.6574199999999999,
                -0.6657799999999999, -0.63822, -0.6353399999999999, -0.6430600000000001, -0.6685399999999998, -0.57974,
                -0.59216, -0.59432, -0.6612600000000001, -0.5297]

    成本2b = []
    满意度2b = []

    成本3b = []
    满意度3b = []

    成本4b = []
    满意度4b = []

    成本5b = [3309.4167, 3309.4167, 2995.3954999999996, 3078.9296999999997, 3222.8059999999996, 3065.0116999999996,
              3283.2596000000003, 3269.147, 3309.4167, 3309.4167, 3283.2596000000003, 3309.4167]
    服务质量5b = [0.5624, 0.5624, 0.4854, 0.5072, 0.5376, 0.48979999999999996, 0.5592, 0.5528, 0.5624, 0.5624, 0.5592,
                  0.5624]



    cost_hhga = np.array(成本1b)
    sa_hhga_ready = np.array(满意度1b)
    now_data_hhga = [[cost_hhga[i], sa_hhga_ready[i]] for i in range(len(cost_hhga))]

    cost_awga = np.array(成本2b)
    sa_awga = np.array(满意度2b)
    now_data_awga = [[cost_awga[i], sa_awga[i]] for i in range(len(cost_awga))]

    cost_nsga2 = np.array(成本3b)
    sa_nsga2 = np.array(满意度3b)
    now_data_nsga2 = [[cost_nsga2[i], sa_nsga2[i]] for i in range(len(cost_nsga2))]

    cost_nsga3 = np.array(成本4b)
    sa_nsga3 = np.array(满意度4b)
    now_data_nsga3 = [[cost_nsga3[i], sa_nsga3[i]] for i in range(len(cost_nsga3))]

    cost_app = np.array(成本5b)
    sa_app = np.array([-datas for datas in 服务质量5b])
    now_data_app = [[cost_app[i], sa_app[i]] for i in range(len(cost_app))]
    return np.array(now_data_hhga), np.array(now_data_awga), np.array(now_data_nsga2), np.array(now_data_nsga3), np.array(now_data_app)



if __name__ == '__main__':
    from pymoo.indicators.hv import HV
    import numpy as np

    hhga, awga, nsga2, nsga3, app = plot_duibi()
    all_data = np.vstack([hhga, app])
    epsilon = 0.05
    ref_point = np.max(all_data, axis=0) + epsilon
    print("参考点:", ref_point)
    hv_indicator = HV(ref_point=ref_point)
    hv_hhga = float(hv_indicator(np.array(hhga)))
    # hv_awga = float(hv_indicator(np.array(awga)))
    # hv_nsga2 = float(hv_indicator(np.array(nsga2)))
    # hv_nsga3 = float(hv_indicator(np.array(nsga3)))
    hv_app = float(hv_indicator(np.array(app)))

    print(round(hv_hhga, 3), "\t",
          round(hv_app, 3))