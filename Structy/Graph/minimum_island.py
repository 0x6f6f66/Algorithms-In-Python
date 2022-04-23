"""

"""


def minimum_island(grid):
    visited = set()
    minimum_size = float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            size = explore_size(grid, i, j, visited)
            print(size)
            if 0 < size < minimum_size:
                minimum_size = size
    return minimum_size


def explore_size(grid, row, col, visited):
    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])

    if not rowInbounds or not colInbounds:
        return 0

    if (row, col) in visited:
        return 0

    if grid[row][col] == 'W':
        return 0

    visited.add((row, col))

    size = 1

    size += explore_size(grid, row + 1, col, visited)
    size += explore_size(grid, row, col + 1, visited)
    size += explore_size(grid, row - 1, col, visited)
    size += explore_size(grid, row, col - 1, visited)

    return size


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(minimum_island(grid))  # -> 2

