"""
https://structy.net/problems/premium/string-search
"""

# My Solution
def string_search1(grid, s):
    coordinates = assemble_coords(grid)
    start = s[0]
    locations = coordinates[start]
    for loc in locations:
        visited = set()
        r, c = loc
        if string_explore(grid, s, r, c, visited) == True:
            "(5, 3) -> (5, 4) -> (5, 5) -> (6, 5) -> (7, 5) -> (7, 6) -> (6, 6)"
            print(loc, visited)
            return True
    return False


def assemble_coords(grid):
    graph = {}
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            letter = grid[r][c]
            if letter not in graph:
                graph[letter] = []
            coordinate = (r, c)
            graph[letter].append(coordinate)
    return graph


def string_explore(grid, string, row, col, visited):
    if len(string) == 0:
        return True

    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False

    if grid[row][col] != string[0]:
        return False

    pos = (row, col)
    if pos in visited:
        return False

    visited.add(pos)

    deltas = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    for delta in deltas:
        deltaRow, deltaCol = delta
        neighbourRow = row + deltaRow
        neighbourCol = col + deltaCol
        if string_explore(grid, string[1:], neighbourRow, neighbourCol, visited) == True:
            return True

    return False


# Structy Solution + my spin on it
def string_search(grid, s):
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if dfs(grid, s, r, c, 0):
                print(grid)
                return True
    return False


def dfs(grid, s, row, col, index):
    if index == len(s): # empty
        return True

    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False

    if grid[row][col] != s[index]:
        return False

    # char = grid[row][col] # Uncomment if we want to restore grid
    grid[row][col] = '*' # Keep track of our visited
    result = dfs(grid, s, row + 1, col, index + 1) or dfs(grid, s, row - 1, col, index + 1) or dfs(grid, s, row, col + 1, index + 1) or dfs(grid, s, row, col - 1, index + 1)
    # grid[row][col] = char # Not really necesary to restore, unless we will be reusing this grid
    return result


"""
           0    1    2    3    4    5    6    7    8    9   10   11
    0    ['f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p'],
    1    ['o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v'],
    2    ['g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n'],
    3    ['a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm'],
    4    ['m', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c'],
    5    ['q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z'],
    6    ['d', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k'],
    7    ['f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w'],
    8    ['p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i'],
    9    ['l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q']


        (5, 3) -> (5, 4) -> (5, 5) -> (6, 5) -> (7, 5) -> (7, 6) -> (6, 6)
"""


if __name__ == '__main__':
    grid = [
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x'],
        ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h'],
    ]
    print(string_search(grid, 'ssssssssssh'))  # -> False

    """
    grid = [
        ['f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p'],
        ['o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v'],
        ['g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n'],
        ['a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm'],
        ['m', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c'],
        ['q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z'],
        ['d', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k'],
        ['f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w'],
        ['p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i'],
        ['l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q']
    ]
    print(string_search(grid, 'paprika'))  # -> True
    """

