# -*- coding: UTF-8 -*-
"""
@filename:python_01.py
@author:DY
@time:2024-06-24
"""
import random
import itertools
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import RegularGridInterpolator, BSpline, make_interp_spline
import math
plt.rcParams['font.family'] = 'SimHei'
import matplotlib
matplotlib.use('Qt5Agg')


def generate_terrain():
    x = y = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    peak_params = [
        (70, 70, 40, 15, 15, 0),
        (13, 52, 34, 8, 8, 0),
        (27, 24, 28, 10, 8, 0),
        (40, 50, 35, 5, 5, 0),
        (30, 79, 40, 8, 8, 0),
        (70, 25, 25, 4, 5, 0),
    ]

    for x0, y0, h, wx, wy, angle in peak_params:
        theta = np.radians(angle)
        a = np.cos(theta) ** 2 / (2 * wx ** 2) + np.sin(theta) ** 2 / (2 * wy ** 2)
        b = np.sin(2 * theta) / (4 * wx ** 2) - np.sin(2 * theta) / (4 * wy ** 2)
        c = np.sin(theta) ** 2 / (2 * wx ** 2) + np.cos(theta) ** 2 / (2 * wy ** 2)
        Z += h * np.exp(-(a * (X - x0) ** 2 + c * (Y - y0) ** 2 + 2 * b * (X-x0)*(Y-y0)))

    assert Z.shape == X.shape, "Z shape must match X and Y shapes"

    interps = RegularGridInterpolator((x, y), Z, method='linear', bounds_error=False, fill_value=None)

    return X, Y, Z, interps


def plot_terrain(x, y, z, start_point_list, end_point_list):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='terrain', rstride=2, cstride=2, alpha=0.8)
    ax.scatter(None, None, label="P_i",color="green", alpha=0.5)
    for i in range(len(start_point_list)):
        if i == len(start_point_list) - 1:
            ax.scatter(*start_point_list[i], color='red', label="仓库", marker='*', s=100, depthshade=False)
        else:
            ax.scatter(*start_point_list[i], color='green', s=100, depthshade=False)
        ax.scatter(*end_point_list[i], color='green', s=100, depthshade=False)

    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Elevation')
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 110)
    ax.set_zlim(0, 90)
    ax.set_title('3D Terrain with PSO Path Planning', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(False)
    return ax


def initialize_pso(num_particles, num_waypoints, start_point, end_point, interp):
    particles = []
    for _ in range(num_particles):
        waypoints = []
        for t in np.linspace(0, 1, num_waypoints + 2)[1:-1]:
            px = (1 - t) * start_point[0] + t * end_point[0] + np.random.normal(0, 0.3)
            py = (1 - t) * start_point[1] + t * end_point[1] + np.random.normal(0, 0.3)
            pz = interp(np.array([[px, py]]))[0] + 0.05 * np.random.normal()
            waypoints.extend([px, py, max(pz, 0)])  # 确保高度不小于0
        particles.append(waypoints)
    return np.array(particles)


def calculate_fitness(particle, start_point, end_point, interp):
    path = decode_path(particle, start_point, end_point)
    segments = np.diff(path, axis=0)
    path_length = np.sum(np.linalg.norm(segments, axis=1))

    penalty = 0
    angle_penalty = 0
    for point in path:
        terrain_z = interp(np.array([point[0], point[1]]))[0]
        if point[2] < terrain_z:
            penalty += 50 * (terrain_z - point[2]) ** 2

        angles = []
        for i in range(1, len(path) - 1):
            v1 = path[i] - path[i - 1]
            v2 = path[i + 1] - path[i]
            cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            angles.append(np.arccos(np.clip(cos_angle, -1, 1)))

        if angles:
            angle_penalty = np.mean(angles)
        else:
            angle_penalty = 0

    return path_length + penalty + angle_penalty


def decode_path(particle, start_point, end_point):
    waypoints = np.array(particle).reshape(-1, 3)
    return np.vstack([start_point, waypoints, end_point])


def pso_path_planning(start_point, end_point, interp):
    num_particles = 50
    num_waypoints = 6
    max_iter = 40
    c1, c2 = 2.0, 2.0
    process = []

    particles = initialize_pso(num_particles, num_waypoints, start_point, end_point, interp)
    velocities = np.random.uniform(-0.5, 0.5, size=particles.shape)
    pbest_positions = particles.copy()
    pbest_fitness = np.array([calculate_fitness(p, start_point, end_point, interp) for p in particles])
    gbest_position = pbest_positions[np.argmin(pbest_fitness)]
    gbest_fitness = np.min(pbest_fitness)
    w_min, w_max = 0.4, 0.9
    for iter in range(max_iter):
        current_w = w_max - (w_max - w_min) * iter / max_iter
        for i in range(num_particles):
            r1, r2 = np.random.rand(2, num_waypoints * 3)
            velocities[i] = current_w * velocities[i] + \
                            c1 * r1 * (pbest_positions[i] - particles[i]) + \
                            c2 * r2 * (gbest_position - particles[i])
            velocities[i] = np.clip(velocities[i], -1, 1)
            particles[i] += velocities[i]
            current_fitness = calculate_fitness(particles[i], start_point, end_point, interp)
            if current_fitness < pbest_fitness[i]:
                pbest_positions[i] = particles[i]
                pbest_fitness[i] = current_fitness
        if np.min(pbest_fitness) < gbest_fitness:
            gbest_position = pbest_positions[np.argmin(pbest_fitness)]
            gbest_fitness = np.min(pbest_fitness)
            res = decode_path(gbest_position, start_point, end_point)
            process.append(list(res))

        # 打印进度
        if iter % 10 == 0:
            print(f"Iteration {iter}: Best Fitness = {gbest_fitness:.4f}")

    return decode_path(gbest_position, start_point, end_point), process, gbest_fitness


def smooth_path(path, interp):
    extended_path = np.vstack([
        path[0], path[0], path[0], path[0],  # 重复起点
        path,
        path[-1], path[-1], path[-1], path[-1] # 重复终点
    ])

    t = np.linspace(0, 1, len(extended_path))

    spline_x = make_interp_spline(t, extended_path[:, 0], k=3)
    spline_y = make_interp_spline(t, extended_path[:, 1], k=3)
    spline_z = make_interp_spline(t, extended_path[:, 2], k=3)

    tt = np.linspace(t[4], t[-5], 100)
    smoothed_x = spline_x(tt)
    smoothed_y = spline_y(tt)
    smoothed_z = spline_z(tt)
    corrected_points = []
    for i in range(len(smoothed_x)):
        terrain_z = interp(np.array([smoothed_x[i], smoothed_y[i]]))[0]
        if smoothed_z[i] < terrain_z:
            smoothed_z[i] = terrain_z + 0.3  # 保持安全高度
        corrected_points.append([smoothed_x[i], smoothed_y[i], smoothed_z[i]])
    corrected_points = np.array(corrected_points)
    new_t = np.linspace(0, 1, len(corrected_points))
    new_spline_x = make_interp_spline(new_t, corrected_points[:, 0], k=3)
    new_spline_y = make_interp_spline(new_t, corrected_points[:, 1], k=3)
    new_spline_z = make_interp_spline(new_t, corrected_points[:, 2], k=3)
    final_tt = np.linspace(0, 1, 100)
    final_x = new_spline_x(final_tt)
    final_y = new_spline_y(final_tt)
    final_z = new_spline_z(final_tt)

    smooth_paths = np.column_stack([final_x, final_y, final_z])
    diffs = np.diff(smooth_paths, axis=0)
    segments_length = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(segments_length)
    return smooth_paths, total_length

def calculate_theo_distance(start_point, end_point):
    start_point_list = list(start_point)
    end_point_list = list(end_point)
    diss = []
    for i in range(len(start_point_list)):
        diss.append((end_point_list[i] - start_point_list[i]) ** 2)
    diss_sum = sum(diss)
    return math.sqrt(diss_sum)


def res_run():
    point_list = []
    res_list = []
    x, y, z, terrain_interp = generate_terrain()
    for i in range(41):
        _px = random.randint(0, 100)
        _py = random.randint(0, 100)
        _pz = terrain_interp(np.array([_px, _py]))
        now_point = np.array([_px, _py, _pz[0]])
        point_list.append({"address": "Sp" + str(i), "coordinate": list(now_point)})
    combinations = list(itertools.combinations(point_list, 2))
    counts = 0
    for combination in combinations:
        counts += 1
        print(f"==========迭代次数: {counts}=========")
        res_dict = {}
        res_dict.update({"start": combination[0]["address"], "end": combination[1]["address"], "theo_distance": calculate_theo_distance(combination[0]["coordinate"], combination[1]["coordinate"]), "start_coordinate": combination[0]["coordinate"], "end_coordinate": combination[1]["coordinate"]})
        raw_path, process, real_distance = pso_path_planning(combination[0]["coordinate"], combination[1]["coordinate"], terrain_interp)
        res_dict.update({"real_distance": real_distance})
        res_dict.update({"raw_path": raw_path})
        res_list.append(res_dict)
    return res_list

def save_res_dict(res_dict):
    start_list = []
    end_list = []
    theo_distance_list = []
    start_coordinate = []
    end_coordinate = []
    real_distance = []
    for datas in res_dict:
        start_list.append(datas["start"])
        end_list.append(datas["end"])
        theo_distance_list.append(datas["theo_distance"])
        start_coordinate.append(datas["start_coordinate"])
        end_coordinate.append(datas["end_coordinate"])
        real_distance.append(datas["real_distance"])
    data_save = {
        "start": start_list,
        "end": end_list,
        "theo_distance": theo_distance_list,
        "start_coordinate": start_coordinate,
        "end_coordinate": end_coordinate,
        "real_distance": real_distance
    }
    df = pd.DataFrame(data_save)
    df.to_excel("distance.xlsx", engine="openpyxl")

def plot_ax(res_data):
    x, y, z, terrain_interp = generate_terrain()
    start_coordinate_list = []
    end_coordinate_list = []
    raw_path_list = []
    smoothed_path_list = []
    for data in res_data:
        start_coordinate = data["start_coordinate"]
        end_coordinate = data["end_coordinate"]
        raw_path = data["raw_path"]
        now_smooth_path, total_length = smooth_path(raw_path, terrain_interp)
        data.update({"real_distance": total_length})
        start_coordinate_list.append(start_coordinate)
        end_coordinate_list.append(end_coordinate)
        raw_path_list.append(raw_path)
        smoothed_path_list.append(now_smooth_path)
    ax = plot_terrain(x, y, z, start_coordinate_list, end_coordinate_list)

    for t in range(len(smoothed_path_list)):
        if t == len(smoothed_path_list) - 1:
            ax.plot(smoothed_path_list[t][:, 0], smoothed_path_list[t][:, 1], smoothed_path_list[t][:, 2],
                label='Smoothed Path', linewidth=3, color='darkred')
        else:
            ax.plot(smoothed_path_list[t][:, 0], smoothed_path_list[t][:, 1], smoothed_path_list[t][:, 2]
                    , linewidth=3, color='darkred')
    for k in range(len(raw_path_list)):
        if k == 0:
            ax.scatter(raw_path_list[k][1:-1, 0], raw_path_list[k][1:-1, 1], raw_path_list[k][1:-1, 2],
                       color='black', s=30, label='Waypoints')
        else:
            ax.scatter(raw_path_list[k][1:-1, 0], raw_path_list[k][1:-1, 1], raw_path_list[k][1:-1, 2],
                           color='black', s=30)
    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    start_time = time.perf_counter()
    res_data = res_run()
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(elapsed_time)
    result_list = []
    for data in res_data:
        dicts = {}
        dicts.update({"start": data["start"], "end": data["end"]})
        dicts.update({"start_coordinate": data["start_coordinate"]})
        dicts.update({"end_coordinate": data["end_coordinate"]})
        dicts.update({"theo_distance": data["theo_distance"]})
        dicts.update({"real_distance": data["real_distance"]})
        result_list.append(dicts)
    plot_ax(res_data)
    save_res_dict(res_data)
