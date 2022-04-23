"""
https://structy.net/problems/premium/binary-search
"""


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        current = numbers[mid]

        if current == target:
            return mid

        if current < target:
            low = mid + 1

        elif current > target:
            high = mid - 1

    return -1


"""

target: 9
current: 5

0 1 2 3 4 5 6 7 8 9
l         m       h

               
"""

if __name__ == '__main__':
    print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6))  # -> 6
    print(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27))  # -> -1
    print(binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8))  # -> 2
    print(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28))  # -> 8
    print(binary_search([7, 9], 7))  # -> 0
