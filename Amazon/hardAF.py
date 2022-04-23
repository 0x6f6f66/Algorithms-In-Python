import time


def maxValue(n, rounds):
    portfolio = [0 for _ in range(n)]

    for i in range(1, n + 1):  # O(n)
        for round_ in rounds:  # O(l))
            if i in range(round_[0], round_[1] + 1):  # O(m)
                portfolio[i - 1] += round_[2]

    return max(portfolio)  # O(n)


# O(nlm + n)


def maxValueOld(n, rounds):
    portfolioG = [0] * n
    for round_ in rounds:  # O(l)
        left = round_[0] - 1
        right = round_[1] - 1
        investment = round_[2]
        for i in range(left, right + 1):  # O(m)
            portfolioG[i] += investment

    return max(portfolioG)  # O(n)


# O(lm + n)


def maxValueNew(n, rounds):
    portfolio = [0 for _ in range(n)]
    biggest = 0
    for round_ in rounds:
        if round_[2] > biggest:
            biggest = round_[2]
    print(biggest)


if __name__ == '__main__':
    """
        rounds = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]
    ]

    print(maxValue(n=5, rounds=rounds))
    """

    rounds = [
        [1, 9, 100],
        [2, 8, 90],
        [2, 8, 80],
        [3, 7, 90],
        [3, 7, 50],
    ]

    n = 10

    print(maxValueNew(n, rounds))
