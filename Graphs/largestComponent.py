def largestComponent(graph):
    largest = 0
    for node in graph:
        size = exploreSize(graph, node)
        if size > largest:
            largest = size
    return largest


def exploreSize(graph, node, visited=None):
    if visited == None:
        visited = set()

    if node in visited:
        return 0

    visited.add(node)

    size = 1

    for neighbour in graph[node]:
        size += exploreSize(graph, neighbour, visited)

    return size


if __name__ == '__main__':
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    print(largestComponent(graph))
