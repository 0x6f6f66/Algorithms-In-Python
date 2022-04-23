"""
https://structy.net/problems/premium/is-univalue-list
"""


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def is_univalue_list(head):
#  value = head.val
#  current = head
#  while current is not None:
#    if current.val != value:
#      return False
#    current = current.next
#  return True


def is_univalue_list(head):
    value = head.val
    return recursion(head, value)


def recursion(node, value):
    if node is None:
        return True
    if node.val != value:
        return False
    return recursion(node.next, value)

