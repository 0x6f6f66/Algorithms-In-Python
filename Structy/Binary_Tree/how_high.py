"""
https://structy.net/problems/premium/how-high
"""

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def how_high(node):
    if node is None:
        return -1

    next_level = max(how_high(node.left), how_high(node.right))

    return next_level + 1