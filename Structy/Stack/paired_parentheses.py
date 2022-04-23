"""
https://structy.net/problems/premium/paired-parentheses
"""


# First solution
def paired_parentheses(string):
    if len(string) == 0:
        return True

    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    return len(stack) == 0


# Solution utilising count
def paired_parentheses2(string):
    if len(string) == 0:
        return True

    count = 0

    for s in string:
        if s == '(':
            count += 1
        if s == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0







if __name__ == '__main__':
    print(paired_parentheses2(")))((("))