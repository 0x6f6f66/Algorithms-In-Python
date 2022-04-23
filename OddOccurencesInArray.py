# First Solution
def solution1(A):
    pairs = []
    for elem in A:
        if elem not in pairs:
            #print(f"ELEM NOT IN PAIRS: {elem}")
            pairs.append(elem)
            #print(f"Pairs: {pairs}\n")
        elif elem in pairs:
            #print(f"ELEM IN PAIRS: {elem}")
            pairs.remove(elem)
            #print(f"Pairs: {pairs}\n")
    return pairs[0]


# Second Solution
def solution(A):
    result = {}
    for elem in A:
        print(f"elem: {elem}")
        if elem in result:
            print(f'{elem} in result')
            print(f"test? {result.pop(elem, None)}")
        else:
            result[elem] = '_'
        print(f"result: {result}\n")

    return result


if __name__ == '__main__':
    arr = [9, 3, 9, 3, 9, 7, 9]
    print(solution1(arr))
