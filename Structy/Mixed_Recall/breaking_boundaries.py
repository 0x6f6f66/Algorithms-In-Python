"""
https://structy.net/problems/premium/breaking-boundaries
"""

# m - rows
# n - columns
# k - moves
# r - row pos
# c - col pos


def breaking_boundaries(m, n, k, r, c, memo=None):
    if memo is None:
        memo = {}

    rowInbounds = 0 <= r < m
    colInbounds = 0 <= c < n

    if not rowInbounds or not colInbounds:
        return 1

    if k == 0:
        return 0

    pos = (r, c, k)
    if pos in memo:
        return memo[pos]

    ways = 0
    ways += breaking_boundaries(m, n, k - 1, r + 1, c, memo)
    ways += breaking_boundaries(m, n, k - 1, r, c + 1, memo)
    ways += breaking_boundaries(m, n, k - 1, r - 1, c, memo)
    ways += breaking_boundaries(m, n, k - 1, r, c - 1, memo)

    memo[pos] = ways
    return memo[pos]

"""
    0   1   2  3
0   x
1
2
"""


if __name__ == '__main__':
    print(breaking_boundaries(3, 4, 2, 0, 0)) # -> 4
    print(breaking_boundaries(6, 6, 12, 3, 4))  # -> 871065