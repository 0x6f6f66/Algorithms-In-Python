def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    print(graph)  # temp
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, src, dst, visited):
    print(src)  # temp
    if src == dst:
        return True

    if src in visited:
        return False  # if its visited must have travelled it before

    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited):
            return True
    return False


# my solution (creates an adjacency list)
def buildGraph(edges):
    graph = {}
    for edge in edges:
        for node in edge:
            if node not in graph:
                graph[node] = []
            temp = edge.copy()
            temp.remove(node)
            graph[node].append(*temp)
    return graph


"""
# tutorial solution (But, i guess it only works for this particular graph)
def buildGraph(edges):
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
"""


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

    print(undirectedPath(edges, "i", "m"))
