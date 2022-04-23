def depth_first_print(graph, start):
    if start not in graph:
        return
    print(start)
    for neighbour in graph[start]:
        depth_first_print(graph, neighbour)


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    depth_first_print(graph, 'a')