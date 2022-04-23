"""
https://structy.net/problems/premium/add-lists
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists_iter(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head

    carry = 0
    current_1 = head_1
    current_2 = head_2

    while current_1 or current_2 or carry == 1:
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val

        sum_ = val_1 + val_2 + carry
        carry = 1 if sum_ > 9 else 0
        digit = sum_ % 10
        tail.next = Node(digit)
        tail = tail.next

        if current_1 is not None:
            current_1 = current_1.next

        if current_2 is not None:
            current_2 = current_2.next

    return dummy_head.next


def add_lists_rec(head_1, head_2, carry=0):
    if head_1 is None and head_2 is None and carry == 0:
        return None

    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val

    sum_ = val_1 + val_2 + carry
    next_carry = 1 if sum_ > 9 else 0

    digit = sum_ % 10
    result_node = Node(digit)

    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    result_node.next = add_lists_rec(next_1, next_2, next_carry)
    return result_node


# Helper function i made
def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)


if __name__ == '__main__':
    a1 = Node(9)
    a2 = Node(3)
    a1.next = a2
    # 9 -> 3

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2
    # 7 -> 4

    # 6 -> 8

    print_list(add_lists_rec(a1, b1))
