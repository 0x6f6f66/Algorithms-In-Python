"""
https://structy.net/problems/premium/flip-tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Helper Visualization function
def print_tree(root):
    if root is None:
        return None

    print(root.val)

    print_tree(root.left)
    print_tree(root.right)


def flip_tree(root):
    if root is None:
        return None

    root.left, root.right = flip_tree(root.right), flip_tree(root.left)

    return root


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

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

    print_tree(flip_tree(a))

    #       a
    #    /    \
    #   c      b
    #  /     /   \
    # f     e    d
    #     /  \
    #    h    g
