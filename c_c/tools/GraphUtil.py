# -*- coding: utf-8 -*-
"""
@filename:GraphUtil.py
@Author  : DY
@Software: PyCharm
@Date    : 2025/1/5 13:59
"""
import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        # 添加双向边
        self.nodes[from_node][to_node] = weight
        self.nodes[to_node][from_node] = weight

    def dijkstra(self, start, end):
        # 初始化距离字典，所有节点的距离设置为无穷大
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0  # 起点到自身的距离为0

        # 存储每个节点的前驱节点，用于回溯路径
        previous = {node: None for node in self.nodes}

        # 优先队列，存储 (距离, 节点) 的元组
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # 如果当前节点是终点，提前结束
            if current_node == end:
                break

            # 如果当前节点的距离大于已知的最短距离，跳过
            if current_distance > distances[current_node]:
                continue

            # 遍历当前节点的邻居
            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + weight

                # 如果找到更短的路径，更新距离和前驱节点，并加入优先队列
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()  # 反转路径，从起点到终点

        return distances[end], path

    def creategraph(self, res):
        for row in res:
            self.add_edge(row['gfrom'], row['gto'], row['weight'])


