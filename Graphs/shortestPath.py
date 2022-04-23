"""
https://structy.net/problems/shortest-path
"""


def shortestPath(edges, nodeA, nodeB, visited=None):
    graph = createGraph(edges)

    if visited is None:
        visited = {nodeA}  # set literal, as opposed to set([nodeA])

    queue = [(nodeA, 0)]

    while queue:
        node, distance = queue.pop()

        if node == nodeB:
            return distance

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(node)
                queue.insert(0, (neighbour, distance + 1))

    return -1


def createGraph(edges):
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


if __name__ == '__main__':
    tests = [
        {
            'edges': [
                ['w', 'x'],
                ['x', 'y'],
                ['z', 'y'],
                ['z', 'v'],
                ['w', 'v']
            ],
            'nodeA': 'w',
            'nodeB': 'z',
            'result': 2
        },
        {
            'edges': [
                ['w', 'x'],
                ['x', 'y'],
                ['z', 'y'],
                ['z', 'v'],
                ['w', 'v']
            ],
            'nodeA': 'y',
            'nodeB': 'x',
            'result': 1
        },
        {
            'edges': [
                ['a', 'c'],
                ['a', 'b'],
                ['c', 'b'],
                ['c', 'd'],
                ['b', 'd'],
                ['e', 'd'],
                ['g', 'f']
            ],
            'nodeA': 'a',
            'nodeB': 'e',
            'result': 3
        },
        {
            'edges': [
                ['a', 'c'],
                ['a', 'b'],
                ['c', 'b'],
                ['c', 'd'],
                ['b', 'd'],
                ['e', 'd'],
                ['g', 'f']
            ],
            'nodeA': 'e',
            'nodeB': 'c',
            'result': 2
        },
        {
            'edges': [
                ['a', 'c'],
                ['a', 'b'],
                ['c', 'b'],
                ['c', 'd'],
                ['b', 'd'],
                ['e', 'd'],
                ['g', 'f']
            ],
            'nodeA': 'b',
            'nodeB': 'g',
            'result': -1
        },
        {
            'edges': [
                ['c', 'n'],
                ['c', 'e'],
                ['c', 's'],
                ['c', 'w'],
                ['w', 'e'],
            ],
            'nodeA': 'n',
            'nodeB': 'e',
            'result': 2
        },
        {
            'edges': [
                ['m', 'n'],
                ['n', 'o'],
                ['o', 'p'],
                ['p', 'q'],
                ['t', 'o'],
                ['r', 'q'],
                ['r', 's']
            ],
            'nodeA': 'm',
            'nodeB': 's',
            'result': 6
        }
    ]

    count = 1
    for test in tests:
        edges = test['edges']
        nodeA = test['nodeA']
        nodeB = test['nodeB']
        result = test['result']

        print(f"[Test {count}]")
        print(f"actual : {shortestPath(edges, nodeA, nodeB)} | expected : {result}")
        print()

        count += 1
