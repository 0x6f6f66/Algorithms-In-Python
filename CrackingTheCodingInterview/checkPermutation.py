"""
1.2 pg. 90
"""


def checkPermutation(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first = ''.join(sorted(first_string))
    second = ''.join(sorted(second_string))

    if first != second:
        return False
    return True


if __name__ == '__main__':
    print(checkPermutation("akab", "baak"))
