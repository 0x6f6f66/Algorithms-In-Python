"""
https://structy.net/problems/island-count
"""


def island_count(grid):
    count = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if explore(grid, i, j, visited):
                count += 1
    return count


def explore(grid, row, col, visited):
    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False

    if (row, col) in visited:
        return False

    if grid[row][col] == 'W':
        return False

    visited.add((row, col))

    explore(grid, row + 1, col, visited)
    explore(grid, row, col + 1, visited)
    explore(grid, row - 1, col, visited)
    explore(grid, row, col - 1, visited)

    return True




