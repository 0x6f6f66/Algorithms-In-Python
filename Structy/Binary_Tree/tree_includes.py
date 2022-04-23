"""
https://structy.net/problems/tree-includes
"""

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_includes_iter(root, target):
    if root is None:
        return False

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == target:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    print(tree_includes(a, "e"))
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
