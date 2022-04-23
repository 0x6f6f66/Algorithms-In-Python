"""
https://structy.net/problems/tribonacci
"""


def tribonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1

    memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
    return memo[n]


if __name__ == '__main__':
    print(tribonacci(5))
