"""
https://structy.net/problems/premium/leaf-list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leaf_list_iter(root):
    if root is None:
        return []

    stack = [root]
    leaves = []

    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            leaves.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return leaves


def leaf_list(root):
    leaves = []
    fill_leaves(root, leaves)
    return leaves


def fill_leaves(root, leaves):
    if root is None:
        return

    if root.left is None and root.right is None:
        leaves.append(root.val)

    fill_leaves(root.left, leaves)
    fill_leaves(root.right, leaves)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

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

    print(leaf_list_iter(a))  # -> [ 'd', 'e', 'f' ]
