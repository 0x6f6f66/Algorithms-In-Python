import itertools


def solution(A):
    pairs = []
    result_final = {}

    # assemble pairs
    for i in range(len(A)):
        range_ = (i - A[i], i + A[i])
        pairs.append(range_)

    # print pairs
    for pair in pairs:
        print(pair)

    print()
    print("Intersections")
    for i in range(len(pairs)):
        temp = []
        for x in range(len(pairs)):
            if overlap(pairs[i], pairs[x]) and i != x:
                temp.append(x)
        result_final[i] = temp

    print(result_final)


def overlap(a, b):
    """
    print(f"internal")
    print(f"a: {a} | b: {b}")
    print()
    print(f"a[0] <= b[0] <= a[1]: {a[0] <= b[0] <= a[1]}")
    print(f"{a[0]} <= {b[0]} <= {a[1]}: {a[0] <= b[0] <= a[1]}")
    print(f"a[0]: {a[0]}")
    print(f"b[0]: {b[0]}")
    print(f"a[1]: {a[1]}")
    print()

    print(f"{b[0]} <= {a[0]} <= {b[1]}: {b[0] <= a[0] <= b[1]}")
    print(f"b[0]: {b[0]}")
    print(f"a[0]: {a[0]}")
    print(f"b[1]: {b[1]}")
    print()
    """

    # print(f"RETURNED OVERLAP VALUE: {a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]}")
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]


if __name__ == '__main__':
    A = [1, 5, 2, 1, 4, 0]

    print(solution(A))
