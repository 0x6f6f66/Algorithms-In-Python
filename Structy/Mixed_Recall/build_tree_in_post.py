"""
https://structy.net/problems/premium/build-tree-in-post
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_in_post(in_order, post_order):
    if len(in_order) == 0:
        return None

    last_element = post_order[-1]
    root = Node(last_element)

    position = in_order.index(root.val)

    print(f"root: {root.val} | position in order: {position}") # Debug
    print(f"in order: {in_order}") # Debug
    print(f"post order: {post_order}") # Debug

    left_in_order = in_order[:position]
    right_in_order = in_order[position + 1:]
    print(f"left in: {left_in_order} | right in: {right_in_order}") # Debug

    left_post_order = post_order[0:position]
    right_post_order = post_order[position:-1]
    print(f"left post: {left_post_order} | right post: {right_post_order}") # Debug
    print() # Debug

    root.left = build_tree_in_post(left_in_order, left_post_order)
    root.right = build_tree_in_post(right_in_order, right_post_order)

    return root


if __name__ == '__main__':
    print(build_tree_in_post(
        ['y', 'x', 'z'],
        ['y', 'z', 'x']
    ))
    #       x
    #    /    \
    #   y      z
    
    print(build_tree_in_post(
        ['d', 'b', 'e', 'a', 'f', 'c', 'g'],
        ['d', 'e', 'b', 'f', 'g', 'c', 'a']
    ))
    #      a
    #    /    \
    #   b      c
    #  / \    / \
    # d   e  f   g

    print(build_tree_in_post(
        ['d', 'b', 'g', 'e', 'h', 'a', 'c', 'f'],
        ['d', 'g', 'h', 'e', 'b', 'f', 'c', 'a']
    ))
    #      a
    #    /    \
    #   b      c
    #  / \      \
    # d   e      f
    #    / \
    #    g  h

    print(build_tree_in_post(
        ['m', 'n'],
        ['m', 'n']
    ))
    #       n
    #     /
    #    m

    print(build_tree_in_post(
        ['n', 'm'],
        ['m', 'n']
    ))
    #     n
    #      \
    #       m
