"""
https://structy.net/problems/premium/closest-carrot
"""

from collections import deque


# My solution
def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, index = queue.popleft()
        rowInbounds = 0 <= row < len(grid)
        colInbounds = 0 <= col < len(grid[0])

        if not rowInbounds or not colInbounds:
            continue

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if grid[row][col] == 'C':
            return index

        if grid[row][col] == 'X':
            continue

        queue.append((row + 1, col, index + 1))
        queue.append((row, col + 1, index + 1))
        queue.append((row - 1, col, index + 1))
        queue.append((row, col - 1, index + 1))

    return -1


# Structy Solution
def closest_carrot2(grid, starting_row, starting_col):
    queue = deque([(starting_row, starting_col, 0)])
    visited = set([(starting_row, starting_col)])
    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == 'C':
            return distance

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbour_row = row + delta_row
            neighbour_col = col + delta_col
            row_inbounds = 0 <= neighbour_row < len(grid)
            col_inbounds = 0 <= neighbour_col < len(grid[0])
            if row_inbounds and col_inbounds and grid[neighbour_row][neighbour_col] != 'X' and (neighbour_row, neighbour_col) not in visited:
                queue.append((neighbour_row, neighbour_col, distance + 1))
                visited.add((neighbour_row, neighbour_col))


if __name__ == '__main__':
    grid = [
        ['O', 'O', 'X', 'X', 'X'],
        ['O', 'X', 'X', 'X', 'C'],
        ['O', 'X', 'O', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'X'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'C', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot2(grid, 3, 4))  # -> 9
