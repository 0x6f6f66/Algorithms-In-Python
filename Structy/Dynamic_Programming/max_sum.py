"""
https://structy.net/problems/max-path-sum
"""


def max_path_sum(grid, r=0, c=0, memo=None):
    if memo is None:
        memo = {}

    pos = (r, c)
    if pos in memo:
        return memo[pos]

    if r == len(grid) or c == len(grid[0]):
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down_value = max_path_sum(grid, r + 1, c, memo)
    right_value = max_path_sum(grid, r, c + 1, memo)

    max_value = grid[r][c] + max(down_value, right_value)

    memo[pos] = max_value
    return max_value


if __name__ == '__main__':
    grid = [
        [1, 2, 8, 1],
        [3, 1, 12, 10],
        [4, 0, 6, 3],
    ]
    print(max_path_sum(grid))  # -> 36

    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    print(max_path_sum(grid))  # -> 27