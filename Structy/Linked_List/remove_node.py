"""
https://structy.net/problems/premium/remove-node
"""


def remove_node(head, target_val):
    if head.val == target_val:
        return head.next

    current = head
    prev = None

    while current:
        if current.val == target_val:
            prev.next = current.next
            current.next = None
            break

        prev = current
        current = current.next
    return head


def remove_node_rec(head, target_val):
    if head is None:
        return None
    if head.val == target_val:
        return head.next

    head.next = remove_node_rec(head.next, target_val)
    return head

