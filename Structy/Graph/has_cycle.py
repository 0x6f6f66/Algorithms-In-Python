"""
https://structy.net/problems/premium/has-cycle
"""


def has_cycle(graph):
    visiting = set()
    visited = set()

    for node in graph:
        if cycle_detect(graph, node, visiting, visited):
            return True

    return False


def cycle_detect(graph, node, visiting, visited):
    print(node)
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbour in graph[node]:
        if cycle_detect(graph, neighbour, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False


print(has_cycle({
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
}) ) # -> True
