"""
1.3 pg. 90
"""


def urlify(s):
    word = s.strip().split(' ')
    return '%20'.join(word)


if __name__ == '__main__':
    s, true_length = ('Mr John Smith   ', 13)
    print(urlify(s))
