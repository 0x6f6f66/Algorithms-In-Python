"""
https://structy.net/problems/premium/tree-value-count
"""

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def tree_value_count(root, target):
    if root is None:
        return 0

    count = 1 if root.val == target else 0
    return count + tree_value_count(root.left, target) + tree_value_count(root.right, target)
