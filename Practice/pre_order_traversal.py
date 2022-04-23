"""
Preorder (Root, Left, Right)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    #      a
    #    /    \
    #   b      c
    #  / \    / \
    # d   e  f   g

    # [a, b, d, e, c, f, g]


def pre_order(root):
    values = []
    pre_order_explore(root, values)
    return values


def pre_order_explore(root, values):
    if root is None:
        return
    values.append(root.val)
    pre_order_explore(root.left, values)
    pre_order_explore(root.right, values)


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
    c.left = f
    c.right = g

    #      a
    #    /    \
    #   b      c
    #  / \    / \
    # d   e  f   g

    print(pre_order(a))
