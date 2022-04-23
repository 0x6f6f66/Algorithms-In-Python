"""
https://structy.net/problems/premium/lowest-common-ancestor
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, val1, val2):
    first_path = find_path(root, val1)
    second_path = find_path(root, val2)
    set2 = set(second_path)

    for val in first_path:
        if val in set2:
            return val

    return None


def find_path(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    left_path = find_path(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = find_path(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None


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

    print(lowest_common_ancestor(a, 'd', 'h'))  # b
    print(lowest_common_ancestor(a, 'd', 'g'))  # b
    print(lowest_common_ancestor(a, 'g', 'c'))  # a
    print(lowest_common_ancestor(a, 'b', 'g'))  # b
    print(lowest_common_ancestor(a, 'f', 'c'))  # c