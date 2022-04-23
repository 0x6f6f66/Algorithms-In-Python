"""
https://structy.net/problems/premium/pair-product
"""


def pair_product(numbers, target):
    previous = {}

    for index, num in enumerate(numbers):
        multiple = target / num

        if multiple in previous:
            return previous[multiple], index

        previous[num] = index


if __name__ == '__main__':
    print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)
    print(pair_product([3, 2, 5, 4, 1], 10))  # -> (1, 2)
    print(pair_product([4, 7, 9, 2, 5, 1], 5)) # -> (4, 5)