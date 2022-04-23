"""
https://structy.net/problems/fib
"""


def fib(n, memo=None):
    if memo is None:
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == '__main__':
    print(fib(0))