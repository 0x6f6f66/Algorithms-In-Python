"""
https://structy.net/problems/premium/build-tree-in-pre
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Solved using slicing
def build_tree_in_pre1(in_order, pre_order):
    if len(in_order) == 0:
        return None

    val = pre_order[0]
    root = Node(val)
    pos = in_order.index(val)

    left_in_order = in_order[:pos]
    right_in_order = in_order[pos + 1:]

    left_pre_order = pre_order[1:pos + 1]
    right_pre_order = pre_order[pos + 1:]

    print(f"root: {root.val} | pos: {pos}") # Debug
    print(f"in order: {in_order}") # Debug
    print(f"pre order: {pre_order}") # Debug
    print(f"left in: {left_in_order} | right in: {right_in_order}") # Debug
    print(f"left pre: {left_pre_order} | right pre: {right_pre_order}") # Debug
    print() # Debug

    root.left = build_tree_in_pre1(left_in_order, left_pre_order)
    root.right = build_tree_in_pre1(right_in_order, right_pre_order)

    return root


# Using indices and no slicing
def build_tree_in_pre(in_order, pre_order):
    end_in = len(in_order) - 1
    end_pre = len(pre_order) - 1

    return _build_tree_in_pre(in_order, pre_order, 0, end_in, 0, end_pre)


# Helper function
def _build_tree_in_pre(in_order, pre_order, start_in, end_in, start_pre, end_pre):
    if end_in < start_in:
        return None

    val = pre_order[start_pre]
    root = Node(val)

    pos = in_order.index(val) # 5

    left_size = pos - start_in
    root.left = _build_tree_in_pre(
        in_order,
        pre_order,
        start_in,
        pos - 1,
        start_pre + 1,
        start_pre + left_size
    )

    root.right = _build_tree_in_pre(
        in_order,
        pre_order,
        pos + 1,
        end_in,
        start_pre + left_size + 1,
        end_pre
    )

    return root


if __name__ == '__main__':
    build_tree_in_pre(
        ['z', 'y', 'x'],
        ['y', 'z', 'x']
    )
    #       y
    #    /    \
    #   z      x

