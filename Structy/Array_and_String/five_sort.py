"""
https://structy.net/problems/premium/five-sort
"""


# My solution after approach
def five_sort(a):
    i = 0
    j = len(a) - 1
    while i <= j:
        if a[i] == 5 and a[j] != 5:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
        if a[i] != 5:
            i += 1
        if a[j] == 5:
            j -= 1
    return a


# Structy Solution
def five_sort1(a):
    i = 0
    j = len(a) - 1
    while i <= j:
        if a[j] == 5:
            j -= 1
        elif a[i] == 5:
            a[i], a[j] = a[j], a[i]
            i += 1
        else:
            i += 1


if __name__ == '__main__':
    print(five_sort([12, 5, 1, 5, 12, 7])) # -> [12, 7, 1, 12, 5, 5]
    print(five_sort([5, 5, 5, 1, 1, 1, 4])) # -> [4, 1, 1, 1, 5, 5, 5]