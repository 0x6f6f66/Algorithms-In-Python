"""
https://structy.net/problems/premium/lefty-nodes
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lefty_nodes(root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    indexes = set()
    result = []

    while queue:
        current, index = queue.popleft()

        if index not in indexes:
            result.append(current.val)
            indexes.add(index)

        if current.left is not None:
            queue.append((current.left, index + 1))

        if current.right is not None:
            queue.append((current.right, index + 1))

    return result


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h

    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

    print(lefty_nodes(a))  # [ 'a', 'b', 'd', 'g' ]
