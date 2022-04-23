"""
https://structy.net/problems/premium/nesting-score
"""


def nesting_score(string):
    stack = [0]

    for bracket in string:
        if bracket == '[':
            stack.append(0)

        elif bracket == ']':
            popped = stack.pop()
            if popped == 0:
                popped += 1
            else:
                popped *= 2
            stack[-1] += popped

    return stack[0]


if __name__ == '__main__':
    print(nesting_score("[]"))  # -> 1
    print(nesting_score("[][][]"))  # -> 3
    print(nesting_score("[[]]"))  # -> 2
    print(nesting_score("[[][]]"))  # -> 4
    print(nesting_score("[[][][]]"))  # -> 6
    print(nesting_score("[[][]][]"))  # -> 5
    print(nesting_score("[][[][]][[]]"))  # -> 7