import time


def gridTraveler(m, n, memo=None):
    if memo is None:
        memo = {}

    if (m, n) in memo:  # case if exists in memo
        return memo[(m, n)]

    if (n, m) in memo:  # inverse case
        return memo[(n, m)]

    if m == 1 and n == 1:  # base case
        return 1

    if m == 0 or n == 0:  # base case if grid is invalid
        return 0

    memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)  # place in memo

    return memo[(m, n)]


if __name__ == '__main__':
    mem = {}
    start = time.time()
    for m in range(1, 3000):
        for n in range(m, 3000):
            print(gridTraveler(m, n, mem))
    print(f"end: {(time.time() - start):.4f}")
