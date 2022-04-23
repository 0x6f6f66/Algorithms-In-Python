def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


if __name__ == '__main__':
        print(canSum(7, [9, 3, 4, 5]))

