"""
https://structy.net/problems/undirected-path
"""


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    visited = set()
    if has_path(graph, node_A, node_B, visited):
        return True
    return False


def has_path(graph, src, dst, visited):
    if src in visited:
        return False

    if src == dst:
        return True

    visited.add(src)

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst, visited):
            return True

    return False


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

if __name__ == '__main__':
    pass