"""
https://structy.net/problems/premium/insert-node
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    if index == 0:
        node = Node(value)
        node.next = head
        return node

    current = head
    count = 0
    while current:
        if count == index - 1:
            node = Node(value)
            temp = current.next
            current.next = node
            node.next = temp
            break

        count += 1
        current = current.next
    return head


def insert_node_rec(head, value, index, count=0):
    if index == 0:
        node = Node(value)
        node.next = head
        return node

    if head is None:
        return None

    if count == index - 1:
        node = Node(value)
        temp = head.next
        head.next = node
        node.next = temp

    insert_node_rec(head.next, value, index, count + 1)
    return head