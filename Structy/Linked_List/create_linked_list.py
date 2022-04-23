"""
https://structy.net/problems/premium/create-linked-list
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# first solution (using prev pointer strat)
def create_linked_list(values):
    if len(values) == 0:
        return None

    prev = None
    head = None
    for val in values:
        node = Node(val)
        if prev:
            prev.next = node
        prev = node
        if head is None:
            head = node
    return head


# Structy Solution (Using dummy head strat)
def create_linked_list2(values):
    dummy_head = Node(None)
    tail = dummy_head

    for val in values:
        tail.next = Node(val)
        tail = tail.next

    return dummy_head.next


# Recursive Solution
def create_linked_list_rec(values):
    if len(values) == 0:
        return None

    head = Node(values[0])
    head.next = create_linked_list_rec(values[1:])  # expensive operation
    return head


# Recursive Optimized
def create_linked_list_rec2(values, i=0):
    if i == len(values):
        return None

    head = Node(values[i])
    head.next = create_linked_list_rec2(values, i)
    return head
