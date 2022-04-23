"""
https://structy.net/problems/count-paths
"""


#My Solution
def count_paths(grid, r=0, c=0, memo=None):
    if memo is None:
        memo = {}

    rowInBounds = 0 <= r < len(grid)
    colInBounds = 0 <= c < len(grid[0])

    if not rowInBounds or not colInBounds or grid[r][c] == 'X':
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    if (r, c) in memo:
        return memo[(r, c)]

    paths = 0

    paths += count_paths(grid, r + 1, c, memo)
    paths += count_paths(grid, r, c + 1, memo)

    memo[(r, c)] = paths
    return paths


#Structy Solution
def count_paths2(grid):
    return _count_paths2(grid, 0, 0, {})


def _count_paths2(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    down_count = _count_paths2(grid, r + 1, c, memo)
    right_count = _count_paths2(grid, r, c + 1, memo)

    memo[pos] = down_count + right_count
    return memo[pos]


if __name__ == '__main__':
    grid = [
        ["O", "O", "O"],
        ["O", "O", "X"],
        ["O", "O", "O"],
    ]

    print(count_paths2(grid))  # -> 3