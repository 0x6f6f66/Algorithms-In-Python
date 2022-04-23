"""
https://structy.net/problems/has-path
"""


def has_path(graph, src, dst):
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True

    return False
