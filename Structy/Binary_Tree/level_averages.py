"""
https://structy.net/problems/premium/level-averages
"""

from collections import deque
from statistics import mean


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_averages_iter(root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    values = []

    while queue:
        current, index = queue.popleft()

        if len(values) < index + 1:
            values.append([])
        values[index].append(current.val)

        if current.left is not None:
            queue.append((current.left, index + 1))

        if current.right is not None:
            queue.append((current.right, index + 1))

    return [mean(val) for val in values]


def level_averages(root):
    values = []
    fill_values(root, values)
    return [mean(val) for val in values]


def fill_values(root, values, index=0):
    if root is None:
        return []

    if len(values) < index + 1:
        values.append([])
    values[index].append(root.val)

    fill_values(root.left, values, index + 1)
    fill_values(root.right, values, index + 1)


if __name__ == '__main__':
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    print(level_averages(a))  # -> [ 3, 7.5, 1 ]
