def canSum(target, numbers):
    table = [False for _ in range(target + 1)]
    table[0] = True

    for i in range(target):
        if table[i]:  # If we can generate the number we are currently at.
            for num in numbers:
                if i + num <= target:  # Check if i + num is in bounds of target.
                    table[i + num] = True  # Then we can generate the number num spaces ahead.

    return table[target]


if __name__ == '__main__':
    print(canSum(7, [5, 3, 4]))
    print(canSum(7, [2, 3]))
    print(canSum(300, [11, 14]))