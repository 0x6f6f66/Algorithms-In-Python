"""
https://structy.net/problems/shortest-path
"""

from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    queue = deque([(node_A, 0)])
    visited = set(node_A)

    while queue:
        current, index = queue.popleft()

        visited.add(current)

        if current == node_B:
            return index

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour, index + 1))

    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
