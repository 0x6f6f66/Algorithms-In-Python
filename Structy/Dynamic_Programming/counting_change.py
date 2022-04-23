"""
https://structy.net/problems/counting-change
"""


def counting_change(amount, coins, i=0, memo={}):
    key = (amount, i)
    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if i == len(coins):
        return 0

    coin = coins[i]
    total_ways = 0
    for qty in range(0, (amount // coin) + 1):
        remainder = amount - qty * coin
        total_ways += counting_change(remainder, coins, i + 1)

    memo[key] = total_ways
    return total_ways


if __name__ == '__main__':
    pass