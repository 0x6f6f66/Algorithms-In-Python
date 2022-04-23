from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        current_row, current_col, distance = queue.popleft()

        if grid[current_row][current_col] == 'C':
            return distance

        visited.add((current_row, current_col))

        deltas = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for delta in deltas:
            delta_row, delta_col = delta
            neighbour_row = current_row + delta_row
            neighbour_col = current_col + delta_col
            rowInbounds = 0 <= neighbour_row < len(grid)
            colInbounds = 0 <= neighbour_col < len(grid[0])
            if rowInbounds and colInbounds and grid[neighbour_row][neighbour_col] != 'X' and (neighbour_row, neighbour_col) not in visited:
                queue.append((neighbour_row, neighbour_col, distance + 1))

    return -1


def closest_carrot2(grid, starting_row, starting_col):
    queue = deque([(starting_row, starting_col, 0)])
    visited = set()

    while queue:
        current_row, current_col, distance = queue.popleft()
        rowInbounds = 0 <= current_row < len(grid)
        colInbounds = 0 <= current_col < len(grid[0])

        if not rowInbounds or not colInbounds:
            continue

        if grid[current_row][current_col] == 'X':
            continue

        if (current_row, current_col) in visited:
            continue

        if grid[current_row][current_col] == 'C':
            return distance

        visited.add((current_row, current_col))

        queue.append((current_row + 1, current_col, distance + 1))
        queue.append((current_row, current_col + 1, distance + 1))
        queue.append((current_row - 1, current_col, distance + 1))
        queue.append((current_row, current_col - 1, distance + 1))

    return -1


if __name__ == '__main__':
    grid = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'C', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['C', 'O', 'O', 'O', 'O'],
    ]

    print(closest_carrot2(grid, 1, 2))  # -> 4