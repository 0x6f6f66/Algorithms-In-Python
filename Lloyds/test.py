def solution(A):
    pairs = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            pairs.append((A[i], A[j]))
            if A[i] - A[j] == 1 or A[i] - A[j] == -1:
                return True, pairs
    return False, pairs


if __name__ == '__main__':
    arr = [5, -2, 7, -1, 3]
    print(solution(arr))


