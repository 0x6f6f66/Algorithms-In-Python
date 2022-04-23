"""
https://structy.net/problems/largest-component
"""


def largest_component(graph):
    visited = set()

    largest = 0
    for node in graph:
        count = explore_count(graph, node, visited)
        if count > largest:
            largest = count

    return largest


def explore_count(graph, node, visited):
    if node in visited:
        return 0

    count = 1
    visited.add(node)

    for neighbour in graph[node]:
        count += explore_count(graph, neighbour, visited)

    return count


if __name__ == '__main__':
    pass

