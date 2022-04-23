"""
https://structy.net/problems/premium/pair-sum
"""


# First attempt
def pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] + numbers[j] == target:
                return j, i


# My Solution after approach
def pair_sum2(numbers, target):
    previous = {}

    for i in range(len(numbers)):
        num = numbers[i]
        complement = target - num

        if complement in previous:
            return previous[complement], i

        previous[num] = i


# Structy Solution
def pair_sum3(numbers, target):
    previous = {}

    for index, num in enumerate(numbers):
        complement = target - num

        if complement in previous:
            return previous[complement], index

        previous[num] = index


# test to see how different i, j nested loops work
def test(numbers):
    for i in range(len(numbers)):
        for j in range(i):
            print(i, j)
    print()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(i, j)


if __name__ == '__main__':
    print(pair_sum3([9, 9], 18)) # -> (0, 1))

    #print(test([1, 2, 3, 4]))