"""
https://structy.net/problems/connected-components-count
"""


def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, node, visited):
    if node in visited:
        return False

    visited.add(node)

    for neighbour in graph[node]:
        explore(graph, neighbour, visited)

    return True


if __name__ == '__main__':
    pass