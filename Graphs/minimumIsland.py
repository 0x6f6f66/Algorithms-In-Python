def minimumIsland(grid):  # O(rc) , O(rc)
    minSize = float('inf')
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            size = exploreSize(grid, r, c, visited)
            if 0 < size < minSize:
                minSize = size


    return minSize


def exploreSize(grid, r, c, visited):
    rowInbounds = 0 <= r < len(grid)
    colInbounds = 0 <= c < len(grid[0])

    if not rowInbounds and colInbounds:
        return 0

    pos = (r, c)

    if pos in visited:
        return 0

    visited.add(pos)

    if grid[r][c] == 'W':
        return 0

    size = 1

    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r, c - 1, visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r, c + 1, visited)

    return size


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'W', 'W'],
    ]

    print(minimumIsland(grid))