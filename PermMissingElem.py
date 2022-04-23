# First solution i tried
def solution1(A: list):
    if 0 not in A:
        A.append(0)
    A.sort()
    pairs = enumerate(A)
    for pair in pairs:
        if pair[0] != pair[1]:
            return pair[1] - 1
    return None


# Second solution i tried
def solution(A: list):
    expected = sum([i for i in range(1, len(A) + 2)])
    actual = sum(A)
    missing_number = expected - actual
    return missing_number


if __name__ == '__main__':
    print(solution([1, 3, 5, 7, 9, 2, 4, 6]))
