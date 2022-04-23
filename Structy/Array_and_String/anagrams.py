"""
https://structy.net/problems/premium/anagrams
"""

# My solution, since i did this in CTCI


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    first = sorted(s1)
    second = sorted(s2)

    if first != second:
        return False
    return True


# Structy solution
def anagrams2(s1, s2):
    return char_count(s1) == char_count(s2)


def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count


# Structy 2nd solution python specific, using import Counter
from collections import Counter
def anagrams3(s1, s2):
    return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    print(anagrams3('restful', 'fluster'))  # -> True
    print(anagrams3('cats', 'tocs'))  # -> False
    print(anagrams3('monkeyswrite', 'newyorktimes'))  # -> True
