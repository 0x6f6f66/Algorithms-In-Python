"""
https://structy.net/problems/min-change
"""


def min_change(amount, coins):
    answer = _min_change(amount, coins)
    if answer == float('inf'):
        return -1
    else:
        return answer


def _min_change(amount, coins, memo=None):
    if memo is None:
        memo = {}

    if amount < 0:
        return float('inf')

    if amount == 0:
        return 0

    if amount in memo:
        return memo[amount]

    minimum = float('inf')
    for coin in coins:
        remainder = amount - coin
        num_coins = 1 + _min_change(remainder, coins, memo)
        if num_coins < minimum:
            minimum = num_coins

    memo[amount] = minimum
    return minimum


if __name__ == '__main__':
    print(min_change(8, [4, 5, 1, 12]))  # -> 2, because 4+4 is the minimum coins possible
