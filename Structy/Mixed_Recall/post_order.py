"""
https://structy.net/problems/premium/post-order
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
    x = Node('x')
    y = Node('y')
    z = Node('z')

    x.left = y
    x.right = z

    #       x
    #    /    \
    #   y      z

    print(post_order(x))
    # ['y', 'z', 'x']

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
    # [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ]
