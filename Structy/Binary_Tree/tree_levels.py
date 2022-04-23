"""
https://structy.net/problems/premium/tree-levels
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_levels_iter(root):
    if root is None:
        return []

    queue = deque([(root, 0)])

    levels = []

    while queue:
        current, index = queue.popleft()

        if len(levels) < index + 1:
            levels.append([])
        levels[index].append(current.val)

        if current.left is not None:
            queue.append((current.left, index + 1))

        if current.right is not None:
            queue.append((current.right, index + 1))
    return levels


def tree_levels(root, level=0, levels=None):
    if root is None:
        return []

    if levels is None:
        levels = []

    if len(levels) < level + 1:
        levels.append([])
    levels[level].append(root.val)

    if root.left is not None:
        tree_levels(root.left, level + 1, levels)

    if root.right is not None:
        tree_levels(root.right, level + 1, levels)









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
    # [_,   _,   _]
    #  0    1    2

    print(tree_levels(a))  # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]
