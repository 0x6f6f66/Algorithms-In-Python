def bestSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    combination = [*table[i], num]
                    if not table[i + num] or len(table[i + num]) > len(combination):
                        table[i + num] = combination

    return table[target]


if __name__ == '__main__':
    print(bestSum(7, [2, 3, 5, 7]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(8, [1, 4, 5]))
    print(bestSum(100, [1, 2, 5, 25]))
    print(bestSum(100, [25, 1, 5, 2]))

