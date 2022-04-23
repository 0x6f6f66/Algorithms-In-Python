"""
https://structy.net/problems/premium/best-bridge
"""

from collections import deque


def best_bridge(grid):
    main_island = None

    for r in range(len(grid)):
        for c in range((len(grid[0]))):
            potential_island = traverse_island(grid, r, c, set())
            print(f'pot island: {potential_island}')
            if len(potential_island) > 0:
                main_island = potential_island
                break  # We could be breaking out of a loop, but not out of the nested loop.
                # We could break out once we find an island, and do bfs on that island, since order of finding
                # islands doesn't matter

    visited = set(main_island)
    queue = deque([])
    for pos in main_island:
        row, col = pos
        queue.append((row, col, 0))

    clear_grid = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]

    while queue:
        row, col, distance = queue.popleft()
        print_visual(row, col, clear_grid)  # temp func to visualize

        if grid[row][col] == 'L' and (row, col) not in main_island:
            return distance - 1

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta in deltas:
            delta_row, delta_col = delta
            neighbour_row = row + delta_row
            neighbour_col = col + delta_col
            neighbour_pos = (neighbour_row, neighbour_col)
            if is_inbounds(grid, neighbour_row, neighbour_col) and neighbour_pos not in visited:
                visited.add((neighbour_row, neighbour_col))
                queue.append((neighbour_row, neighbour_col, distance + 1))


def is_inbounds(grid, row, col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds


def traverse_island(grid, row, col, visited):
    if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
        return visited

    pos = (row, col)
    if pos in visited:
        return visited

    visited.add(pos)

    traverse_island(grid, row - 1, col, visited)
    traverse_island(grid, row + 1, col, visited)
    traverse_island(grid, row, col - 1, visited)
    traverse_island(grid, row, col + 1, visited)

    return visited


def print_visual(row, col, clear_grid):
    clear_grid[row][col] = 'X'

    for r in clear_grid:
        print(r)
    print()

    clear_grid[row][col] = 'v'


if __name__ == '__main__':
    grid = [
        ["W", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "L"],
        ["L", "L", "L", "W", "L"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
    ]
    print(best_bridge(grid))  # -> 1