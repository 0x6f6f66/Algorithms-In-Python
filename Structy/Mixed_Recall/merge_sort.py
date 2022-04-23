"""
https://structy.net/problems/premium/merge-sort
"""

from typing import List


"""

[1, 3, 5, 2, 4]
 1, 3
 5, 2, 4

    1, 3
    1
    3
    

"""


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    midpoint: int = len(nums)//2

    left: list = nums[:midpoint]
    right: list = nums[midpoint:]

    sorted_left: list = merge_sort(left)
    sorted_right: list = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left: list, right: list) -> List[int]:
    result = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        current_left = left[i]
        current_right = right[j]

        if current_left <= current_right:
            result.append(current_left)
            i += 1

        if current_right <= current_left:
            result.append(current_right)
            j += 1

    while i < len(left):
        current_left = left[i]
        result.append(current_left)
        i += 1

    while j < len(right):
        current_right = right[j]
        result.append(current_right)
        j += 1

    return result


if __name__ == '__main__':
    numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
    print(merge_sort(numbers))
    # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ]

    numbers = [7, -30, -4, -1, 12, 0, 20]
    print(merge_sort(numbers))
    # -> [ -30, -4, -1, 0, 7, 12, 20 ]

    numbers = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(merge_sort(numbers))
    # -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]

