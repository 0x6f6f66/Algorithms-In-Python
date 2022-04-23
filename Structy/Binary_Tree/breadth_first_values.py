"""
https://structy.net/problems/breadth-first-values
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def breadth_first_values(root):
    if root is None:
        return []

    queue = [root]
    values = []

    while queue:
        current = queue.pop(0)  # O(n) operation, since we have to shift an entire list
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values


# Using deque
def breadth_first_values2(root):
    if root is None:
        return []

    queue = deque([root])
    values = []

    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(breadth_first_values2(a))
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']
