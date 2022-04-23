def solution(A):
    A = sorted(A)
    b = range(1, max(A))
    difference = set(b) - set(A)
    if difference:
        result = min(set(b) - set(A))
    else:
        result = A[-1] + 1
    return result


if __name__ == '__main__':
    A = [2]
    print(solution(A))
