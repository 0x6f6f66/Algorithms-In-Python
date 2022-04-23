"""
https://structy.net/problems/premium/most-frequent-char
"""


def most_frequent_char(s):
    count = char_count(s)

    most_frequent = 0
    most_fr_char = ''
    for k in count:
        if count[k] > most_frequent:
            most_frequent = count[k]
            most_fr_char = k

    return most_fr_char


def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


# Structy Solution
from collections import Counter
def most_frequent_char2(s):
    """
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    """

    count = Counter(s)

    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best


if __name__ == '__main__':
    print(most_frequent_char2("baaabcb"))