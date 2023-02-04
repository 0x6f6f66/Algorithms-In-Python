from collections import deque


def cross_grid_traverse(grid, r, c):

    deltas = [
        (1, 0),
        (0, 1)
    ]

    to_visit = set()

    queue = deque([ (r, c) ])

    while queue:
        current = queue.pop()
        row, col = current

        print(grid[row][col])

        for delta in deltas:
            delta_row, delta_col = delta
            neighbour_row = row + delta_row
            neighbour_col = col + delta_col
            row_inbounds = 0 <= neighbour_row < len(grid)
            col_inbounds = 0 <= neighbour_col < len(grid[0])

            if not row_inbounds or not col_inbounds:
                continue

            pos = (neighbour_row, neighbour_col)

            if pos in to_visit:
                continue

            to_visit.add(pos)

            queue.appendleft(pos)


if __name__ == '__main__':
    grid = [
        ['0' , '2' , '5' , '9' , '14'],
        ['1' , '4' , '8' , '13', '18'],
        ['3' , '7' , '12', '17', '21'],
        ['6' , '11', '16', '20', '23'],
        ['10', '15', '19', '22', '24']
    ]

    grid2 = [
        ['0', '2'],
        ['1', '3']
    ]

    cross_grid_traverse(grid, 0, 0)