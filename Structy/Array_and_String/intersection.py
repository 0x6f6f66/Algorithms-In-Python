"""
https://structy.net/problems/premium/intersection
"""


# First solution
def intersection(a, b):
    result = []
    for elem in a:
        if elem in b:
            result.append(elem)
    return result


# Solution after Approach
def intersection1(a, b):
    set_a = {*a}
    result = []
    for elem in b:
        if elem in set_a:
            result.append(elem)
    return result


# Structy solution
def intersection2(a, b):
    set_a = {*a}
    return [ele for ele in b if ele in set_a]



if __name__ == '__main__':
    print(intersection2([4, 2, 1, 6], [3, 6, 9, 2, 10]))
    # print(intersection([1, 2, 3, 4], [9, 8, 6, 2, 5, 4, 0]))