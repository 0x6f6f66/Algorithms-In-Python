"""
https://structy.net/problems/non-adjacent-sum
"""


def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})


def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(nums):
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude = _non_adjacent_sum(nums, i + 1, memo)

    memo[i] = max(include, exclude)
    return memo[i]


if __name__ == '__main__':
    nums = [2, 4, 5, 12, 7]
    print(non_adjacent_sum(nums))  # -> 16