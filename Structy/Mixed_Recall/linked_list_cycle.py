"""
https://structy.net/problems/premium/linked-list-cycle
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Time: O(n)
# Space: O(n)
def linked_list_cycle(head):
    visited = set()
    return _linked_list_cycle(head, visited)


def _linked_list_cycle(node, visited):
    if node is None:
        return False

    if node in visited:
        return True

    visited.add(node)

    if _linked_list_cycle(node.next, visited):
        return True

    return False


# Time: O(n)
# Space: O(1)
def linked_list_cycle2(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d
    d.next = b  # cycle

    #         _______
    #       /        \
    # a -> b -> c -> d

    print(linked_list_cycle2(a))  # True
