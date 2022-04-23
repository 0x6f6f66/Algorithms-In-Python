"""
https://structy.net/problems/premium/parenthetical-possibilities
"""


def parenthetical_possibilities(s: str) -> list:
    if len(s) == 0:
        return ['']

    chars, remaining = get_options(s)
    possibilities = []

    for char in chars:
        suffixes = parenthetical_possibilities(remaining)
        for suffix in suffixes:
            possibilities.append(char + suffix)

    return possibilities


def get_options(s: str) -> (str, str):
    if s[0] == '(':
        index = s.index(')')
        chars = s[1:index]
        remaining = s[index + 1:]
        return chars, remaining
    else:
        chars = s[0]
        remaining = s[1:]
        return chars, remaining




if __name__ == '__main__':
    print(parenthetical_possibilities('x(mn)yz'))  # ->
    # [ 'xmyz', 'xnyz' ]

    #print(get_options('(abc)de'))
    #print(get_options('ade'))