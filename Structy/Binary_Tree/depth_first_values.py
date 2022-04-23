"""
https://structy.net/problems/depth-first-values
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# My Solution
def depth_first_values(root, values=None):
    if values is None:
        values = []
    if root is None:
        return []

    values.append(root.val)

    depth_first_values(root.left, values)
    depth_first_values(root.right, values)

    return values


# Structy Solution:
def depth_first_values2(root):
    if root is None:
        return []

    left_values = depth_first_values2(root.left) # [b, d, e]
    right_values = depth_first_values2(root.right) # [c, f]

    return [root.val, *left_values, *right_values]


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

    print(depth_first_values2(a))
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
