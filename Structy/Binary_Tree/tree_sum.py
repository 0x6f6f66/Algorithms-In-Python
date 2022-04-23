"""
https://structy.net/problems/tree-sum
"""

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def tree_sum(root):
    if root is None:
        return 0

    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)

    return root.val + left_sum + right_sum