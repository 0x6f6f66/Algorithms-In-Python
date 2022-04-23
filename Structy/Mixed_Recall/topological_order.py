"""
https://structy.net/problems/premium/topological-order
"""

from collections import deque


def topological_order(graph):
    order = []
    num_parents = make_num_parents(graph)

    ready = deque([node for node in num_parents if num_parents[node] == 0])

    while ready:
        current = ready.pop()
        order.append(current)

        for child in graph[current]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.appendleft(child)

    return order


def make_num_parents(graph):
    num_parents = {}

    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    return num_parents


if __name__ == '__main__':
    print(topological_order({
        "a": ["f"],
        "b": ["d"],
        "c": ["a", "f"],
        "d": ["e"],
        "e": [],
        "f": ["b", "e"],
    }))  # -> ['c', 'a', 'f', 'b', 'd', 'e']

    print(topological_order({
        "h": ["l", "m"],
        "i": ["k"],
        "j": ["k", "i"],
        "k": ["h", "m"],
        "l": ["m"],
        "m": [],
    }))  # -> ['j', 'i', 'k', 'h', 'l', 'm']

    print(topological_order({
        "q": [],
        "r": ["q"],
        "s": ["r"],
        "t": ["s"],
    }))  # -> ['t', 's', 'r', 'q']

    print(topological_order({
        "v": ["z", "w"],
        "w": [],
        "x": ["w", "v", "z"],
        "y": ["x"],
        "z": ["w"],
    }))  # -> ['y', 'x', 'v', 'z', 'w']
