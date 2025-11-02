import itertools
import math
import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.interpolate import make_interp_spline

plt.rcParams['font.family'] = 'SimHei'
import matplotlib
matplotlib.use('Qt5Agg')


def generate_terrain():
    x = y = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    return X, Y, Z

def cube_to_cylinder_boundaries(cubes, margin=0.01):
    cylinders = []
    for cube in cubes:
        x0, y0, z0, dx, dy, dz = cube
        center_x = (x0 + dx + x0) / 2
        center_y = (y0 + dy + y0) / 2
        radius = np.sqrt((dx / 2)**2 + (dy / 2)**2) + margin
        height = dz + margin
        base_z = z0
        cylinders.append((center_x, center_y, base_z, radius, height))
    return cylinders


def plot_terrain_with_cubes(x, y, z, start_point_list, end_point_list, cubes):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, z, cmap='terrain', rstride=50, cstride=50, alpha=0.8)  # 调整rstride和cstride提高性能
    for i in range(len(start_point_list)):
        if i == len(start_point_list) - 1:
            ax.scatter(*start_point_list[i], color='green', s=100, label='p_i', depthshade=False)
        elif i == len(start_point_list) - 2:
            ax.scatter(*start_point_list[i], color='red', s=100, label='WareHouse', depthshade=False)
        else:
            ax.scatter(*start_point_list[i], color='green', s=100, depthshade=False)
        ax.scatter(*end_point_list[i], color='green', s=100, depthshade=False)

    counts = 1
    for cube in cubes:
        x0, y0, z0, dx, dy, dz = cube
        vertices = [
            [x0, y0, z0],
            [x0 + dx, y0, z0],
            [x0 + dx, y0 + dy, z0],
            [x0, y0 + dy, z0],
            [x0, y0, z0 + dz],
            [x0 + dx, y0, z0 + dz],
            [x0 + dx, y0 + dy, z0 + dz],
            [x0, y0 + dy, z0 + dz]
        ]

        faces = [
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]],
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[2], vertices[3], vertices[7], vertices[6]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[3], vertices[7], vertices[4]]
        ]

        if counts <= 5:
            ax.add_collection3d(Poly3DCollection(
                faces,
                facecolors='yellow',
                linewidths=1,
                edgecolors='black',
                alpha=0.5
            ))

        elif 5 < counts <= 10:
            ax.add_collection3d(Poly3DCollection(
                faces,
                facecolors='blue',
                linewidths=1,
                edgecolors='black',
                alpha=0.5
            ))

        elif 10 < counts:
            ax.add_collection3d(Poly3DCollection(
                faces,
                facecolors='red',
                linewidths=1,
                edgecolors='black',
                alpha=0.5
            ))
        counts += 1
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 160)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title('3D Urban Environmental Model', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(False)
    return ax


def project_point_to_cylinder_surface(x, y, z, cylinders, prev_point=None):
    counts = -1
    for i in range(len(cylinders)):
        if judgment_point_is_not_suitable_only(x, y, z, cylinders[i]):
            counts = i
            break
    if counts == -1:
        return (x, y, z)
    else:
        cx, cy, z0, radius, height = cylinders[counts]
        dx = x - cx
        dy = y - cy
        dist = np.hypot(dx, dy)
        if dist == 0:
            if prev_point is not None:
                pdx = prev_point[0] - cx
                pdy = prev_point[1] - cy
                pdist = np.hypot(pdx, pdy)
                if pdist == 0:
                    ux, uy = radius, 0.0
                else:
                    ux, uy = pdx / pdist, pdy / pdist
            else:
                ux, uy = radius, 0.0
        else:
            ux, uy = dx / dist, dy / dist
        proj_x = cx + (radius+0.5) * ux
        proj_y = cy + (radius+0.5) * uy
        proj_z = z

        top_x = cx + (radius+0.5) * ux
        top_y = cy + (radius+0.5) * uy
        top_z = z0 + height + 0.5

        def dist_to(px, py, pz):
            return np.sqrt((px - x) ** 2 + (py - y) ** 2 + (pz - z) ** 2)

        candidates = [
            (proj_x, proj_y, proj_z),
            (top_x, top_y, top_z)
        ]
        return min(candidates, key=lambda p: dist_to(*p))


def is_point_in_cylinder(x, y, z, cylinder):
    cx, cy, z0, radius, height = cylinder
    o_s_distance = (cx - x) ** 2 + (cy - y) ** 2
    if o_s_distance <= (radius+0.1) ** 2:
        inside_xy = True
    else:
        inside_xy = False
    if z0 <= z <= z0 + height + 0.1:
        inside_z = True
    else:
        inside_z = False
    return inside_xy and inside_z


def judgment_point_is_not_suitable(x, y, z, cylinders):
    res_list = []
    for cylinder in cylinders:
        cx, cy, z0, radius, height = cylinder
        o_s_distance = (cx - x) ** 2 + (cy - y) ** 2
        if o_s_distance <= (radius+0.5) ** 2:
            inside_xy = True
        else:
            inside_xy = False
        if z0 <= z <= z0 + height + 0.5:
            inside_z = True
        else:
            inside_z = False
        res_list.append(inside_xy and inside_z)
    return any(res_list)


def judgment_point_is_not_suitable_only(x, y, z, cylinder):
    cx, cy, z0, radius, height = cylinder
    o_s_distance = (cx - x) ** 2 + (cy - y) ** 2
    if o_s_distance <= (radius+0.5) ** 2:
        inside_xy = True
    else:
        inside_xy = False
    if z0 <= z <= z0 + height + 0.5:
        inside_z = True
    else:
        inside_z = False
    return inside_xy and inside_z


def initialize_pso(num_particles, num_waypoints, start_point, end_point, cylinders):
    particles = []
    for _ in range(num_particles):
        waypoints = []
        for t in np.linspace(0, 1, num_waypoints + 2)[1:-1]:
            px = (1 - t) * start_point[0] + t * end_point[0] + np.random.normal(0, 0.3)
            py = (1 - t) * start_point[1] + t * end_point[1] + np.random.normal(0, 0.3)
            pz = random.randint(0, 10) + 0.05 * np.random.normal()
            if judgment_point_is_not_suitable(px, py, pz, cylinders):
                suitable_point = project_point_to_cylinder_surface(px, py, pz, cylinders)
                suitable_point = list(suitable_point)
                suitable_point[2] = max(0, suitable_point[2])
            else:
                suitable_point = [px, py, pz]
            waypoints.extend([suitable_point[0], suitable_point[1], max(suitable_point[2], 0)])  # 确保高度不小于0
        particles.append(waypoints)
    return np.array(particles)


def is_line_crossing_cylinder_center(p1, p2, cylinder):
    cx, cy, _, _, _ = cylinder
    x1, y1 = p1[:2]
    x2, y2 = p2[:2]
    d1 = np.hypot(x1 - cx, y1 - cy)
    d2 = np.hypot(x2 - cx, y2 - cy)
    d12 = np.hypot(x2 - x1, y2 - y1)
    return abs((d1 + d2) - d12) < 1e-1

def calculate_fitness(particle, start_point, end_point, cylinders):
    path = decode_path(particle, start_point, end_point)
    path = path.copy()
    paths = path.tolist()
    sliding_pairs = [paths[i:i + 2] for i in range(0, len(paths) - 2 + 1, 1)]
    counts_penalty = 0
    for pair in sliding_pairs:
        for cylinder in cylinders:
            if is_line_crossing_cylinder_center(pair[0], pair[1], cylinder):
                counts_penalty += 100000
    segments = np.diff(path, axis=0)
    path_length = np.sum(np.linalg.norm(segments, axis=1))
    penalty = 0
    angle_penalty = 0
    for point in path:
        ok_x, ok_y, ok_z = project_point_to_cylinder_surface(point[0], point[1], point[2], cylinders)
        if judgment_point_is_not_suitable(point[0], point[1], point[2], cylinders):
            penalty += 50 * ((ok_x - point[0]) ** 2 + (ok_y - point[1]) ** 2 + (ok_z - point[2]) ** 2)  # 二次惩罚更严格
        angles = []
        for i in range(1, len(path) - 1):
            v1 = path[i] - path[i - 1]
            v2 = path[i + 1] - path[i]
            cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            angles.append(np.arccos(np.clip(cos_angle, -1, 1)))

        if angles:
            angle_penalty = np.mean(angles) * 1
        else:
            angle_penalty = 0

    return path_length + penalty + angle_penalty + counts_penalty

def decode_path(particle, start_point, end_point):
    waypoints = np.array(particle).reshape(-1, 3)
    return np.vstack([start_point, waypoints, end_point])


def pso_path_planning(start_point, end_point, cylinders):
    num_particles = 50
    num_waypoints = 6
    max_iter = 40
    c1, c2 = 2.0, 2.0
    process = []

    particles = initialize_pso(num_particles, num_waypoints, start_point, end_point, cylinders)
    velocities = np.random.uniform(-0.5, 0.5, size=particles.shape)
    pbest_positions = particles.copy()
    pbest_fitness = np.array([calculate_fitness(p, start_point, end_point, cylinders) for p in particles])
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

            velocities[i] = np.clip(velocities[i], -1, 2)
            particles[i] += velocities[i]
            current_fitness = calculate_fitness(particles[i], start_point, end_point, cylinders)
            if current_fitness < pbest_fitness[i]:
                pbest_positions[i] = particles[i]
                pbest_fitness[i] = current_fitness
        if np.min(pbest_fitness) < gbest_fitness:
            gbest_position = pbest_positions[np.argmin(pbest_fitness)]
            gbest_fitness = np.min(pbest_fitness)
            res = decode_path(gbest_position, start_point, end_point)
            process.append(list(res))
        if iter % 10 == 0:
            print(f"Iteration {iter}: Best Fitness = {gbest_fitness:.4f}")

    return decode_path(gbest_position, start_point, end_point), process, gbest_fitness


def smooth_path(path, cylinders):
    extended_path = np.vstack([
        path[0], path[0],  # 重复起点
        path,
        path[-1], path[-1]  # 重复终点
    ])

    t = np.linspace(0, 1, len(extended_path))

    spline_x = make_interp_spline(t, extended_path[:, 0], k=3)
    spline_y = make_interp_spline(t, extended_path[:, 1], k=3)
    spline_z = make_interp_spline(t, extended_path[:, 2], k=3)

    tt = np.linspace(t[2], t[-3], 100)
    smoothed_x = spline_x(tt)
    smoothed_y = spline_y(tt)
    smoothed_z = spline_z(tt)
    corrected_points = []
    for i in range(len(smoothed_x)):
        x, y, z = smoothed_x[i], smoothed_y[i], smoothed_z[i]
        if judgment_point_is_not_suitable(x, y, z, cylinders):
            suitable_point = project_point_to_cylinder_surface(x, y, z, cylinders)
            x, y = suitable_point[0], suitable_point[1]
            z = max(suitable_point[2], 0)
        corrected_points.append([x, y, z])
    corrected_points = np.array(corrected_points)
    new_t = np.linspace(0, 1, len(corrected_points))
    new_spline_x = make_interp_spline(new_t, corrected_points[:, 0], k=3)
    new_spline_y = make_interp_spline(new_t, corrected_points[:, 1], k=3)
    new_spline_z = make_interp_spline(new_t, corrected_points[:, 2], k=3)
    final_tt = np.linspace(0, 1, 100)
    final_x = new_spline_x(final_tt)
    final_y = new_spline_y(final_tt)
    final_z = new_spline_z(final_tt)
    for i in range(len(final_x)):
        xs, ys, zs = final_x[i], final_y[i], final_z[i]
        if judgment_point_is_not_suitable(xs, ys, zs, cylinders):
            suitable_point = project_point_to_cylinder_surface(xs, ys, zs, cylinders)
            final_x[i], final_y[i], final_z[i] = suitable_point[0], suitable_point[1], suitable_point[2]
    smooth_paths = np.column_stack([final_x, final_y, final_z])
    diffs = np.diff(smooth_paths, axis=0)
    segments_length = np.linalg.norm(diffs, axis=1)
    total_length = np.sum(segments_length)
    return smooth_paths, total_length

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
    df.to_excel("distance_terrain.xlsx", engine="openpyxl")

def calculate_theo_distance(start_point, end_point):
    start_point_list = list(start_point)
    end_point_list = list(end_point)
    diss = []
    for i in range(len(start_point_list)):
        diss.append((end_point_list[i] - start_point_list[i]) ** 2)
    diss_sum = sum(diss)
    return math.sqrt(diss_sum)

def run_script():
    cubes = [
        (10, 45, 0, 4, 5, 45),
        (5, 59, 0, 6, 5, 35),
        (20, 45, 0, 7, 7, 50),
        (20, 60, 0, 7, 8, 39),
        (33, 55, 0, 6, 4, 36),


        (90, 65, 0, 8, 9, 56),
        (75, 68, 0, 7, 5, 55),
        (88, 80, 0, 6, 6, 57),
        (68, 55, 0, 10, 6, 52),
        (65, 80, 0, 10, 7, 59),


        (60, 20, 0, 10, 10, 34),
        (76, 11, 0, 6, 8, 35),
        (90, 20, 0, 8, 6, 38),
        (76, 30, 0, 10, 10, 40),

        (10, 20, 0, 10, 10, 25)

    ]
    # 膨胀边界
    cylinders = cube_to_cylinder_boundaries(cubes, 0.8)
    point_list = []
    res_list = []
    for i in range(51):
        zao1 = np.random.normal(0, 0.3)
        zao2 = np.random.normal(0, 0.3)
        zao3 = np.random.normal(0, 0.3)
        _point_x = random.randint(0, 100) + zao1
        _point_y = random.randint(0, 100) + zao2
        _point_z = random.randint(5, 10) + zao3
        if judgment_point_is_not_suitable(_point_x, _point_y, _point_z, cylinders):
            suitable_point = list(project_point_to_cylinder_surface(_point_x, _point_y, _point_z, cylinders))
            suitable_point[2] = max(0, suitable_point[2])
        else:
            suitable_point = [_point_x, _point_y, _point_z]
        now_point = np.array(suitable_point)
        point_list.append({"address": "Sp" + str(i), "coordinate": list(now_point)})
    combinations = list(itertools.combinations(point_list, 2))
    counts = 0
    for combination in combinations:
        counts += 1
        print(f"==========迭代次数: {counts}=========")
        res_dict = {}
        res_dict.update({"start": combination[0]["address"], "end": combination[1]["address"],
                         "theo_distance": calculate_theo_distance(combination[0]["coordinate"],
                                                                  combination[1]["coordinate"]),
                         "start_coordinate": combination[0]["coordinate"],
                         "end_coordinate": combination[1]["coordinate"]})
        raw_path, process, real_distance = pso_path_planning(combination[0]["coordinate"], combination[1]["coordinate"],
                                                             cylinders)
        res_dict.update({"real_distance": real_distance})
        res_dict.update({"raw_path": raw_path})
        res_list.append(res_dict)
    return res_list, cubes, cylinders


def plot_ax(res_data, cylinders, cubes_):
    x, y, z = generate_terrain()
    start_coordinate_list = []
    end_coordinate_list = []
    raw_path_list = []
    smoothed_path_list = []
    for data in res_data:
        start_coordinate = data["start_coordinate"]
        end_coordinate = data["end_coordinate"]
        raw_path = data["raw_path"]
        now_smooth_path, total_length = smooth_path(raw_path, cylinders)
        data.update({"real_distance": total_length})
        start_coordinate_list.append(start_coordinate)
        end_coordinate_list.append(end_coordinate)
        raw_path_list.append(raw_path)
        smoothed_path_list.append(now_smooth_path)
    ax = plot_terrain_with_cubes(x, y, z, start_coordinate_list, end_coordinate_list, cubes_)

    for t in range(len(smoothed_path_list)):
        if t == len(smoothed_path_list) - 1:
            ax.plot(smoothed_path_list[t][:, 0], smoothed_path_list[t][:, 1], smoothed_path_list[t][:, 2],
                label='Smoothed Path', linewidth=3, color='darkred')
        else:
            ax.plot(smoothed_path_list[t][:, 0], smoothed_path_list[t][:, 1], smoothed_path_list[t][:, 2]
                    , linewidth=3, color='darkred')
    save_res_dict(res_data)

    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    res_data, cubes, cylinders = run_script()
    plot_ax(res_data, cylinders, cubes)

