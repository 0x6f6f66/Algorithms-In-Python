# DFS Recursive
def hasPathDFSRec(graph, src, dst):  # n = # nodes | e = # edges | Time: O(e) | Space: O(n) |
    # we can also say, that n^2 = # of edges,
    # since worst case is each node has n number of edges.
    if src == dst:
        return True

    for neighbour in graph[src]:
        if hasPathDFSRec(graph, neighbour, dst):
            return True

    return False


# DFS Iterative
def hasPathDFS(graph, src, dst):
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True

        for neighbour in graph[current]:
            stack.append(neighbour)
    return False


# BFS Iterative
def hasPathBFS(graph, src, dst):
    queue = [src]
    while queue:
        current = queue.pop()
        if current == dst:
            return True

        for neighbour in graph[current]:
            queue.insert(0, neighbour)

    return False


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }  # acyclic = no cycles, unlike this -> {a: [b], b: [c], c: [a]}

    print(hasPathDFSRec(graph, "f", "h"))
    print(hasPathBFS(graph, "f", "h"))
    print(hasPathDFS(graph, "f", "h"))
