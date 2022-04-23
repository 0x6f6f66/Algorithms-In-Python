"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
"""


def snail(snail_map):
    visited = set()
    return explore(snail_map, 0, 0, True, visited)


def explore(graph, r, c, isUp, visited):
    rowInbounds = 0 <= r < len(graph)
    colInbounds = 0 <= c < len(graph[-1])

    pos = (r, c)
    if (pos in visited) or (not (rowInbounds and colInbounds)):
        return []

    print(f'{graph[r][c]}')
    visited.add(pos)

    goingUp = []
    if isUp:
        goingUp = [*explore(graph, r - 1, c, True, visited)]

    right = [*explore(graph, r, c + 1, False, visited)]
    down = [*explore(graph, r + 1, c, False, visited)]
    left = [*explore(graph, r, c - 1, False, visited)]
    up = [*explore(graph, r - 1, c, True, visited)]

    result = [graph[r][c], *right, *down, *left, *up, *goingUp]

    return result


if __name__ == '__main__':
    snail_map = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    snail_map2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]

    snail_map3 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    print(snail(snail_map3))


    """
    [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
    """

