def fib(n):
    table = [0 for _ in range(n + 1)]
    table[1] = 1

    for i in range(n):
        if i + 1 == n:
            table[i + 1] += table[i]
        else:
            table[i + 1] += table[i]
            table[i + 2] += table[i]

    return table[n]


if __name__ == '__main__':
    print(fib(8))
