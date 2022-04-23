"""
n = 8

indent = " "
for x in range(n, 0, -1):
    print(f"{indent * (n * 2 - x * 2)}{'*   ' * x}")
"""


def solution(S):
    S = S.strip()
    match = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    stack = []

    for s in S:
        if s in match:
            stack.append(s)
        else:
            if stack:
                if match[stack.pop()] != s:
                    return 0
            else:
                return 0
    if len(stack) > 0:
        return 0
    return 1



if __name__ == '__main__':
    S = "{{{{"
    print(solution(S))
