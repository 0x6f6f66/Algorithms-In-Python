"""
https://structy.net/problems/premium/quickest-concat
"""


def quickest_concat(s, words):
    result = _quickest_concat(s, words, {})
    if result == float('inf'):
        return -1
    else:
        return result


def _quickest_concat(s, words, memo):
    if s in memo:
        return memo[s]

    if s == '':
        return 0

    min_num = float('inf')

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            min_num = min(_quickest_concat(suffix, words, memo), min_num)

    memo[s] = 1 + min_num
    return 1 + min_num


if __name__ == '__main__':
    print(quickest_concat('caution', ['ion', 'caut', 'caution'])) # -> 1
