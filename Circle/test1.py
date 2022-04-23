def solution(a, l, r):
    b = [False for _ in range(len(a))]
    for i in range(len(a)):
        x = a[i] / (i + 1)
        print(x)
        if (x % 1 == 0) and (l <= x <= r):
            b[i] = True
    return b


if __name__ == '__main__':
    print(solution([8, 5, 6, 16 ,5], 1, 3))