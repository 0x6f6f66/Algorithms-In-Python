def depthFirstPrint(graph, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def depthFirstPrintRec(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRec(graph, neighbor)


if __name__ == '__main__':
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    # Depth First Search: abdfce or acebdf

    # depthFirstPrint(graph, "a")
    depthFirstPrintRec(graph, "a")