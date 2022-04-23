def breadthFirstPrint(graph, source):
    queue = [source]
    while queue:
        current = queue.pop()
        print(current)
        for neighbour in graph[current]:
            queue.insert(0, neighbour)


if __name__ == '__main__':
    graph = {
        "a": ["c", "b"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }

    breadthFirstPrint(graph, "a")  # acbedf