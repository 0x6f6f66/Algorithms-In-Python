def fib(n, memo=None):
    if memo is None:
        memo = {}
    print(f"n: {n}")
    if n in memo:
        print(f"   accessed memo[{n}]")
        return memo[n]

    if n <= 2:
        print(f" base case n: {n}")
        return 1

    memo[n] = fib(n - 1, memo=memo) + fib(n - 2, memo=memo)
    print(f"stored memo for n: {n}")
    return memo[n]


if __name__ == '__main__':
    x = 7
    print(f"i: {x} | fib: {fib(x)}")


