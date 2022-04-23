"""
Postorder (Left, Right, Root)
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

    # [d, e, b, f, g, c, a]


def post_order(root):
    values = []
    post_order_explore(root, values)
    return values


def post_order_explore(root, values):
    if root is None:
        return

    post_order_explore(root.left, values)
    post_order_explore(root.right, values)
    values.append(root.val)


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

    print(post_order(a))