"""
https://structy.net/problems/connected-components-count
"""


def connectedComponentsCount(graph):
    count = 0
    visited = set()

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    return True


if __name__ == '__main__':
    graphs = [
        {
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        },
        {
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        },
        {
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        },
        {

        },
        {
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }
    ]

    for graph in graphs:
        print(connectedComponentsCount(graph))