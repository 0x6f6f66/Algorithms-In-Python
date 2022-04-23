"""
https://structy.net/problems/sum-possible
"""


def sum_possible(amount, numbers, memo=None):
    if memo is None:
        memo = {}

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        remainder = amount - num
        if sum_possible(remainder, numbers, memo):
            memo[amount] = True
            return memo[amount]

    memo[amount] = False
    return memo[amount]


if __name__ == '__main__':
    print(sum_possible(8, [5, 12, 4]))  # -> True, 4 + 4
    print(sum_possible(15, [6, 2, 10, 19]))  # -> False