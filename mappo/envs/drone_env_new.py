# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
from envs.evalute_reward import evaluate_route_cost
import gym
import numpy as np
from gym import spaces


def merge_with_separators(lists, separator=0):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)
        if i < len(lists) - 1:
            result.append(separator)
    return result


def decode_actions(actions):
    # [1, 0, 0, 0, 2, 1, 2, 0, 3, 1]
    uav1 = []
    uav2 = []
    uav3 = []
    uav4 = []
    uav5 = []
    uav6 = []
    # uav7 = []
    # uav8 = []
    for i in range(len(actions)):
        if actions[i] == 0:
            uav1.append(i + 1)
        elif actions[i] == 1:
            uav2.append(i + 1)
        elif actions[i] == 2:
            uav3.append(i + 1)
        elif actions[i] == 3:
            uav4.append(i + 1)
        elif actions[i] == 4:
            uav5.append(i + 1)
        elif actions[i] == 5:
            uav6.append(i + 1)
        # elif actions[i] == 6:
        #     uav7.append(i + 1)
        # elif actions[i] == 7:
        #     uav8.append(i + 1)
        else:
            pass
    end_list = [uav1, uav2, uav3, uav4, uav5, uav6]
    res_list = merge_with_separators(end_list, 0)
    return res_list



class DroneTaskEnv(gym.Env):
    def __init__(self, config):
        self.task_config = config[0]
        self.drones_config = config[1]
        self.depot_corr = config[2]
        self.state = None
        self.available_uav = None
        self.available_task = None
        self.uav_free = None
        self.task_needed = None
        self.task_coordinates = None
        self.MAX_TASK_DEMAND = max(ta['need'] for ta in self.task_config)
        self.MAX_UAV_CAPACITY = max(u['capacity'] for u in self.drones_config)
        self.num_tasks = len(self.task_config)
        self.num_uavs = len(self.drones_config)
        self.action_space = spaces.MultiDiscrete([self.num_tasks] * self.num_uavs)
        self.observation_space = spaces.Dict({
            "available_task": spaces.MultiBinary(self.num_tasks),  # 1标记任务有剩余，0标记任务已分配完
            "task_needed": spaces.Box(low=0.0, high=self.MAX_TASK_DEMAND, shape=(self.num_tasks,), dtype=np.float32),
            "uav_free": spaces.Box(low=0.0, high=self.MAX_UAV_CAPACITY, shape=(self.num_uavs,), dtype=np.float32),
            "task_coordinates": spaces.Box(
                low=0.0,
                high=100.0,
                shape=(self.num_tasks, 2),
                dtype=np.float32
            )
        })

    def reset(self):

        self.available_task = np.ones(self.num_tasks, dtype=np.int32)
        self.uav_free = np.array([uav['capacity'] for uav in self.drones_config], dtype=np.float32)
        self.task_needed = np.array([task['need'] for task in self.task_config], dtype=np.float32)
        self.task_coordinates = np.array([task["t_corr"] for task in self.task_config], dtype=np.float32)
        self.state = {
            "available": self.available_task.copy(),
            "task_needed": self.task_needed.copy(),
            "uav_free": self.uav_free.copy(),
            "task_coordinates": self.task_coordinates.copy()
        }
        return self.state

    def step(self, actions):
        done = False

        for i, uav_id in enumerate(actions):
            if uav_id >= self.num_uavs:
                continue

            if self.state["available"][i] == 1 and self.state["task_needed"][i] <= self.state["uav_free"][uav_id]:
                self.state["available"][i] = 0
                self.state["uav_free"][uav_id] -= self.state["task_needed"][i]
                self.state["task_needed"][i] = 0.0
            else:
                pass
        if np.sum(self.state["available"]) == 0:
            res_list = decode_actions(actions)
            need_time, sa, cost = evaluate_route_cost(res_list)
            if cost == 10000:
                rewards = 0
            else:
                distance_reward = ((5000 - cost) / (5000 - 400)) * 100
                sa_reward = -sa * 100
                rewards = (0.5 * distance_reward) + (0.5 * sa_reward)
                done = True
        else:
            rewards = 0

        obs = {
            "available": self.state["available"].copy(),
            "task_needed": self.state["task_needed"].copy(),
            "uav_free": self.state["uav_free"].copy(),
            "task_coordinates": self.state["task_coordinates"].copy()
        }

        info = {}

        return obs, rewards, done, info


