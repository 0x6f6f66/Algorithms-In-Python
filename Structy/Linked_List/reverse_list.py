"""
https://structy.net/problems/reverse-list
"""


def reverse_list_iter(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def reverse_list_rec(current, prev=None):
    if current is None:
        return prev

    next = current.next
    current.next = prev

    return reverse_list_rec(next, current)


if __name__ == '__main__':
    pass