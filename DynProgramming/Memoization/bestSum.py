import sys
sys.setrecursionlimit(10000)

def bestSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = [*remainderCombination, num]
            if (shortestCombination is None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return memo[targetSum]


if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7]))