def allSum(target, numbers):  # My own problem
    table = [[] for _ in range(target + 1)]
    table[0] = [[]]

    for i in range(target):
        if table[i]:
            for num in numbers:
                if i + num <= target:
                    for tbl in table[i]:
                        table[i + num].append([*tbl, num])

    return table[target]


if __name__ == '__main__':
    print(allSum(8, [2, 3, 5]))  # O(numbers ^ target)
