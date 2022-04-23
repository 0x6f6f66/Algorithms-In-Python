def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSum(remainder, numbers, memo)
        if result is not None:
            memo[targetSum] = [*result, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


if __name__ == '__main__':
    print(howSum(7, [5, 2, 4, 3, 6]))
    print(howSum(0, [1, 4]))
    print(howSum(10, [1, 5]))
    print(howSum(300, [7, 14]))
    print(howSum(7, [2, 4]))
