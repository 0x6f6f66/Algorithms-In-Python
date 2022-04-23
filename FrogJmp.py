import math
"""
X - Start
Y - Finish
D - Step
"""


def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance//D
    else:
        return distance//D + 1


if __name__ == '__main__':
    X = 213
    Y = 5231
    D = 35

    print(solution(X, Y, D))
