"""
https://structy.net/problems/premium/befitting-brackets
"""

def befitting_brackets(string):
    table = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for s in string:
        if s in table:
            stack.append(s)
        else:
            if len(stack) == 0 or table[stack.pop()] != s:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    pass