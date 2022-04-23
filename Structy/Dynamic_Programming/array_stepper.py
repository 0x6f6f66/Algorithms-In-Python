"""
https://structy.net/problems/array-stepper
"""


def array_stepper(numbers, i=0, memo=None):
    if memo is None:
        memo = {}

    if i in memo:
        return memo[i]

    if i >= len(numbers) - 1:
        return True

    for step in range(1, numbers[i] + 1):
        if array_stepper(numbers, i + step, memo):
            memo[i] = True
            return True

    memo[i] = False
    return False


if __name__ == '__main__':
    print(array_stepper([2, 4, 2, 0, 0, 1]))  # -> True
    print(array_stepper([2, 3, 2, 0, 0, 1]))  # -> False
