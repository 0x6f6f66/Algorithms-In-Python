"""
https://structy.net/problems/premium/linked-palindrome
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_palindrome(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]


if __name__ == '__main__':
    a = Node(3)
    b = Node(2)
    c = Node(7)
    d = Node(7)
    e = Node(2)
    f = Node(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 3 -> 2 -> 7 -> 7 -> 2 -> 3
    linked_palindrome(a)  # True