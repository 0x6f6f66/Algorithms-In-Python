def fibonacci(n, memo=None):
    if memo is None:
        memo = {
            0: 0,
            1: 0,
            2: 1
        }

    if n in memo:
        return memo[n]

    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    #print(f'n: {n} | result: {result}')
    memo[n] = result
    return result


if __name__ == '__main__':
    memo = {
        0: 0,
        1: 0,
        2: 1
    }
    for i in range(0, 300001, 100):
        fibonacci(i, memo)

    print(fibonacci(300000, memo))
    # 0 1 1 2 3 5 8 13 21 34
    # 1 2 3 4 5 6 7 8  9  10
