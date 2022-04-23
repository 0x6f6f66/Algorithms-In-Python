"""
https://structy.net/problems/island-count
"""


def islandCountMy(grid):  # My solution, but didnt figure out how to make upper bounds checker dynamic
    map_ = makeMap(grid)
    visited = set()
    count = 0

    for node in map_:
        if explore(map_, node, visited):
            count += 1

    return count


def exploreMy(map_, node, visited):
    if node in visited:
        return False

    if map_[node] == 'W':
        return False

    visited.add(node)

    row = node[0]
    column = node[1]

    down = None
    left = None
    up = None
    right = None

    if row - 1 >= 0:
        down = (row - 1, column)
    if column - 1 >= 0:
        left = (row, column - 1)
    if row + 1 <= 5:  # TEMP - needs to be dynamic value
        up = (row + 1, column)
    if column + 1 <= 3:  # TEMP - needs to be dynamic value
        right = (row, column + 1)

    neighbours = [down, left, up, right]
    for neighbour in neighbours:
        if neighbour is not None:
            exploreMy(map_, neighbour, visited)

    return True


def makeMap(grid):
    map_ = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            map_[(i, j)] = grid[i][j]

    return map_


# ===================================================== #


def islandCount(grid):  # Tutorial solution | O(rc) , O(rc)
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if explore(grid, r, c, visited):
                count += 1

    return count


def explore(grid, r, c, visited):

    rowInbounds = 0 <= r < len(grid)
    colInbounds = 0 <= c < len(grid[0])

    if not (rowInbounds and colInbounds):
        return False

    pos = (r, c)  # Tutorial used string literals, but i will be using a tuple, since im in python :)
    if pos in visited:
        return False

    if grid[r][c] == 'W':
        return False

    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c + 1, visited)

    return True


if __name__ == '__main__':
    grid1 = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'L', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W'],
    ]

    grid2 = [
        ['W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W'],
        ['W', 'L', 'L', 'W'],
        ['W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W'],
    ]

    grid3 = [
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
    ]

    print(islandCount(grid1))
    print(islandCount(grid2))
    print(islandCount(grid3))

