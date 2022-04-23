def howSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    table[i + num] = [*table[i], num]

    return table[target]


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))