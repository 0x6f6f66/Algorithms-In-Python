"""
https://structy.net/problems/premium/max-increasing-subseq
"""


def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, float("-inf"), {})


def _max_increasing_subseq(numbers, i, previous, memo):
    key = (i, previous)
    if key in memo:
        return memo[key]

    if i == len(numbers):
        return 0

    current = numbers[i]
    options = []

    dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
    options.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
        options.append(take_current)

    memo[key] = max(options)
    return memo[key]


if __name__ == '__main__':
    numbers = [6, 9, 7, 8]
    print(max_increasing_subseq(numbers))  # -> 3

    numbers = [4, 18, 20, 10, 12, 15, 19]
    print(max_increasing_subseq(numbers))  # -> 5

    numbers = [7, 14, 10, 12]
    print(max_increasing_subseq(numbers))  # -> 3

