"""
https://structy.net/problems/premium/compress
"""


def compress(s):
    s += '!'  # to cover the edge case where we can't count last char, we add '!' because it's not an alphabetic char
    result = []
    i = 0

    for j in range(len(s)):
        if s[i] != s[j]:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num) + s[i])
            i = j

    return ''.join(result)


if __name__ == '__main__':
    print(compress('ccaaatsss'))  # -> '2c3at3s'
