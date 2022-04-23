"""
https://structy.net/problems/premium/can-concat
"""


def can_concat(s, words):
    return _can_concat(s, words, {})


def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]

    if len(s) == 0:
        return True

    for word in words:
        prefix = s[0:len(word)]
        if prefix == word:  # we can also use str.startswith() built-in method
            suffix = s[len(word):]
            if _can_concat(suffix, words, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False


if __name__ == '__main__':
    print(can_concat("foodisgood", ["f", "ood", "foo", "is", "g"]))