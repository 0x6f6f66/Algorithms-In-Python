"""
https://structy.net/problems/premium/middle-value
"""


class Node:
    def __init__(self, val):
       self.val = val
       self.next = None


# Array Solution
def middle_value(head):
    current = head
    values = []

    while current:
        values.append(current.val)
        current = current.next

    return values[len(values)//2]


# Fast and Slow pointers Solution
def middle_value1(head):
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.val


# test function to test behavior of different ways to find the mid point
def test(values):
    length = len(values)
    floor_middle = length // 2
    raw_middle = length / 2
    round_middle = round(length/2)
    print(f'values: {values}')
    print(f'length: {length}')
    print(f'floor: {floor_middle}')
    print(f'raw: {raw_middle}')
    print(f'round: {round_middle}')


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # a -> b -> c -> d -> e
    print(middle_value1(a)) # c

    """
    print('Test 1')
    values1 = ['a', 'b', 'c', 'd', 'e']
    test(values1)
    print()

    print('Test 2')
    values2 = ['a', 'b', 'c']
    test(values2)
    print()

    print('Test 3')
    values3 = ['a', 'b', 'c', 'd']
    test(values3)
    print()

    print('Test 4')
    values4 = ['a', 'b', 'c', 'd', 'e', 'f']
    test(values4)
    print()
    """








