"""
https://structy.net/problems/premium/longest-path
"""


def longest_path(graph):
    distance = {}
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0

    for neighbour in graph[node]:
        attempt = traverse_distance(graph, neighbour, distance)
        if attempt > max_distance:
            max_distance = attempt

    distance[node] = 1 + max_distance
    return distance[node]


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': [],
        'q': ['r'],
        'r': ['s', 'u', 't'],
        's': ['t'],
        't': ['u'],
        'u': []
    }

    print(longest_path(graph))  # -> 4