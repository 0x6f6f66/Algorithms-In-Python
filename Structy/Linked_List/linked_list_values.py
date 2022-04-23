"""
https://structy.net/problems/linked-list-values/problem-index
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    result = []
    node = head

    while node is not None:
        result.append(node.val)
        node = node.next

    return result


# Recursive solution
def rec_linked_list_values(head):
    values = []
    fill_values(head, values)
    return values


def fill_values(head, values):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    print(linked_list_values(a))
