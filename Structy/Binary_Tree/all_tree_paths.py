"""
https://structy.net/problems/premium/all-tree-paths
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Unoptimized
def all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []

    left_sub_paths = all_tree_paths(root.left)

    for l_path in left_sub_paths:
        paths.append([root.val, *l_path])

    right_sub_paths = all_tree_paths(root.right)

    for r_path in right_sub_paths:
        paths.append([root.val, *r_path])

    return paths


# Optimized
def all_tree_paths2(root):
    result = _all_tree_paths(root)

    if result is []:
        return []
    else:
        final = []
        for res in result:
            final.append(res[::-1])
        return final



def _all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []

    left_sub_paths = _all_tree_paths(root.left)
    right_sub_paths = _all_tree_paths(root.right)

    for l_path in left_sub_paths:
        l_path.append(root.val)
        paths.append(l_path)

    for r_path in right_sub_paths:
        r_path.append(root.val)
        paths.append(r_path)

    return paths


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

    print(all_tree_paths2(a))  # ->
    # [
    #   [ 'a', 'b', 'd' ],
    #   [ 'a', 'b', 'e' ],
    #   [ 'a', 'c', 'f' ]
    # ]
