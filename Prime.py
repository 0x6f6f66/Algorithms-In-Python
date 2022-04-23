import math
import time


def isPrime1(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def isPrime2(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    for x in range(2, n//2, 1):
        if n % x == 0:
            return False
    return True


if __name__ == '__main__':
    big_num = 10 ** 8
    for i in range(big_num, big_num * 10):
        first, second = False, False
        start1 = time.time()
        if isPrime1(i):
            end1 = time.time() - start1
            first = True

        start2 = time.time()
        if isPrime2(i):
            end2 = time.time() - start2
            second = True

        if first and second:
            print(f"i: {i} | first: {format(end1, '.10f')} | second: {format(end2, '.10f')}")