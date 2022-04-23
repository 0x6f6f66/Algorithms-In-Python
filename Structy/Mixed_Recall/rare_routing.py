"""
https://structy.net/problems/premium/rare-routing
"""


def rare_routing(n, roads):
    graph = make_graph2(n, roads)
    visited = set()

    explore_result = explore(0, graph, visited, None)

    return explore_result and len(visited) == n


def explore(node, graph, visited, last_node):
    if node in visited:
        return False

    visited.add(node)

    for neighbour in graph[node]:
        if neighbour != last_node and explore(neighbour, graph, visited, node) is False:
            return False

    return True


# My original make graph method
def make_graph(edges):
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


# Structy graph method. (Makes a difference if we get a big num of cities with some cities have no roads)
def make_graph2(n, roads):
    graph = {}

    for city in range(0, n):
        graph[city] = []

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    return graph


if __name__ == '__main__':
    """
    tests = [
        {
            'edges': [
                (0, 1),
                (0, 2),
                (0, 3)
            ],
            'n': 4
        },
        {
            'edges': [
                (0, 1),
                (0, 2),
                (0, 3),
                (3, 2)
            ],
            'n': 4
        },
        {
            'edges': [
                (1, 2),
                (5, 4),
                (3, 0),
                (0, 1),
                (0, 4),
            ],
            'n': 6
        },
        {
            'edges': [
                (1, 2),
                (4, 1),
                (5, 4),
                (3, 0),
                (0, 1),
                (0, 4),
            ],
            'n': 6
        },
        {
            'edges': [
                (0, 1),
                (3, 2),
            ],
            'n': 4
        },
        {
            'edges': [
                (0, 1),
                (3, 2),
            ],
            'n': 7
        }
    ]

    for test in tests:
        print(make_graph(test['edges']))
        print(make_graph2(test['n'], test['edges']))
        print()
    """

    print(rare_routing(4, [
        (0, 1),
        (0, 2),
        (0, 3)
    ]))  # -> True

    print(rare_routing(4, [
        (0, 1),
        (0, 2),
        (0, 3),
        (3, 2)
    ]))  # -> False

    print(rare_routing(6, [
        (1, 2),
        (5, 4),
        (3, 0),
        (0, 1),
        (0, 4),
    ]))  # -> True

    print(rare_routing(6, [
        (1, 2),
        (4, 1),
        (5, 4),
        (3, 0),
        (0, 1),
        (0, 4),
    ]))  # -> False

    print(rare_routing(4, [
        (0, 1),
        (3, 2),
    ]))  # -> False
