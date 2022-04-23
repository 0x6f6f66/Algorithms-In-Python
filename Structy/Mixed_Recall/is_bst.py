"""
https://structy.net/problems/premium/is-binary-search-tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_binary_search_tree(root):
    values = []
    explore_in_order(root, values)
    print(values)
    return is_sorted(values)


def is_sorted(values):
    for i in range(len(values) - 1):
        current = values[i]
        next = values[i + 1]
        if next < current:
            return False
    return True


def explore_in_order(root, values):
    if root is None:
        return

    explore_in_order(root.left, values)
    values.append(root.val)
    explore_in_order(root.right, values)


if __name__ == '__main__':
    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(9)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   9     19

    print(is_binary_search_tree(a))  # -> True

    a = Node(12)
    b = Node(5)
    c = Node(18)
    d = Node(3)
    e = Node(15)
    f = Node(19)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      12
    #    /   \
    #   5     18
    #  / \     \
    # 3   15     19

    print(is_binary_search_tree(a))  # -> False
