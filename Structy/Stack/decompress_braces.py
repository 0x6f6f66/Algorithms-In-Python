"""
https://structy.net/problems/premium/decompress-braces
"""
from collections import deque


def decompress_braces(string):
    stack = []

    for char in string:
        print(f'char: {char} | stack: {stack}')
        if char.isalpha() or char.isnumeric():
            stack.append(char)
        if char == '}':
            popped = ''
            popped_chars = deque([])
            while not popped.isnumeric():
                popped = stack.pop()
                popped_chars.appendleft(popped)
            assembled_string = assemble_string(popped_chars)
            stack.append(assembled_string)

    return ''.join(stack)


def assemble_string(chars: deque):
    num = int(chars.popleft())
    return ''.join(chars) * num


if __name__ == '__main__':
    print(decompress_braces("2{q}3{tu}v"))
    # -> qqtututuv
    print(decompress_braces("2{y3{o}}s"))
    # -> yoooyooos