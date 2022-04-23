"""
https://structy.net/problems/premium/safe-cracking
"""

from typing import List, Tuple, Dict


def safe_cracking(hints: List[Tuple[int, int]]) -> str:
    graph = assemble_graph(hints)
    return topological_order(graph)


def assemble_graph(edges: List[Tuple[int, int]]) -> Dict:
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    return graph


def topological_order(graph: Dict) -> str:
    num_parents = {}

    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    ready = [node for node in num_parents if num_parents[node] == 0]
    order = []

    while ready:
        current = ready.pop()
        order.append(str(current))
        for child in graph[current]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return ''.join(order)


if __name__ == '__main__':
    print(safe_cracking([
        (7, 1),
        (1, 8),
        (7, 8),
    ]))  # -> '718'

    print(safe_cracking([
        (3, 1),
        (4, 7),
        (5, 9),
        (4, 3),
        (7, 3),
        (3, 5),
        (9, 1),
    ]))  # -> '473591'

    print(safe_cracking([
        (2, 5),
        (8, 6),
        (0, 6),
        (6, 2),
        (0, 8),
        (2, 3),
        (3, 5),
        (6, 5),
    ]))  # -> '086235'

    print(safe_cracking([
        (0, 1),
        (6, 0),
        (1, 8),
    ]))  # -> '6018'

    print(safe_cracking([
        (8, 9),
        (4, 2),
        (8, 2),
        (3, 8),
        (2, 9),
        (4, 9),
        (8, 4),
    ]))  # -> '38429'