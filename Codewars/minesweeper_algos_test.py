"""
i: 0
j: 1, 2, 3, 4

i: 1
j: 2, 3, 4

i: 2
j: 3, 4

i: 3
j: 4

i: 4
j: None


"""
import copy
from typing import List, Tuple, Union

"""

test = [0, 1, 2, 3, 4]
for i in range(len(test)):
    for j in range(i + 1, len(test)):
        print(f"{i}: {j}")
"""

"""
test = [
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6', '7', '8']
]

res = '\n'.join(' '.join(col for col in row) for row in test)


# print(res)


# Explore all question marks, and assemble them into an island
def explore_island(graph, r, c, visited):
    island = []

    pos = (r, c)

    if pos in visited:
        return island

    if graph[r][c] != '?':
        return island


    Check if the current question mark is valid to be explored.
    Question mark is valid, when it is not surrounded by only question marks, but also by numbers.
        0 1 2
    0   ? ? ?
    1   ? ? ?
    2   ? ? 1
     
    (0, 0), (0, 1), (0, 2)
    (1, 0)
    (2, 0)
    Are all invalid.
     
    (2, 1), (1, 1), (1, 2)
    Are all valid. 
     
    (essentially, we're looking for question marks on the border of numbers, or bombs.)


    visited.add(pos)

    if not is_valid_for_explore(graph, r, c):
        return island

    island.append(pos)

    deltas = [
        (-2, -2), (-2, -1), (-2,  0), (-2,  1), (-2,  2),
        (-1, -2), (-1, -1), (-1,  0), (-1,  1), (-1,  2),
        ( 0, -2), ( 0, -1),           ( 0,  1), ( 0,  2),
        ( 1, -2), ( 1, -1), ( 1,  0), ( 1,  1), ( 1,  2),
        ( 2, -2), ( 2, -1), ( 2,  0), ( 2,  1), ( 2,  2)
    ]

    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = r + delta_row
        neighbour_col = c + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        result = explore_island(graph, neighbour_row, neighbour_col, visited)
        if result:
            island += result

    return island


# If there are no alpha numeric characters around a question mark, it should become part of an island (border)
def is_valid_for_explore(graph, r, c):
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    alnum_chars_count = 0

    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = r + delta_row
        neighbour_col = c + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        neighbour: str = graph[neighbour_row][neighbour_col]

        if neighbour.isalnum():
            alnum_chars_count += 1

    return alnum_chars_count != 0


test_graph = [
    ['0', '1', '1', '2', '2', '2', '3'],  # 0
    ['1', '2', 'x', '1', '0', '1', '2'],  # 1
    ['?', '?', '2', '1', '0', '1', 'x'],  # 2
    ['?', '?', '2', '1', '2', '2', '2'],  # 3
    ['?', '?', '2', 'x', '2', 'x', '1'],  # 4
    ['?', '?', '?', '2', '2', '1', '1'],  # 5
    ['?', '?', '?', '1', '0', '0', '0']  # 6
]

expl_island = explore_island(test_graph, 2, 0, set())


def tank_solve_island(graph, island, bomb_limit: int, current_bombs: List[Union[Tuple[int, int], None]], visited: set, output: List):
    key = make_key(bomb_limit, current_bombs)
    if key in visited:
        return

    print(current_bombs)
    modified_graph_with_bombs = make_modified_graph(copy.deepcopy(graph), current_bombs)
    # check if it's valid. If valid, append to output.
    output.append(modified_graph_with_bombs)

    visited.add(key)

    if bomb_limit == 0:
        return

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            current = graph[i][j]
            if current == '?':
                graph[i][j] = 'P'
                current_bombs.append( (i, j) )
                current_bombs.sort()
                tank_solve_island(graph, island, bomb_limit - 1, current_bombs, visited, output)
                current_bombs.remove( (i, j) )
                graph[i][j] = '?'
    return


def make_modified_graph(graph, current_bombs: List[Union[Tuple[int, int], None]]):
    for bomb in current_bombs:
        row, col = bomb
        graph[row][col] = 'P'

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '?':
                graph[i][j] = 'S'

    return graph


def make_key(number: int, arr: List[Tuple[int, int]]) -> str:
    if not arr:
        return 'NONE'

    key = [f'{number}']

    for elem in arr:
        suffix = str(elem)
        key.append(suffix)

    return '-'.join(key)

dummy_graph = [
    ['?', '?', '?', '?'],
    ['1', '2', '3', '4']
]

# dummy_island = {(0, 1), (0, 2), (0, 3), (0, 4)}
# current_bombs = []
# output = []
# tank_solve_island(copy.deepcopy(dummy_graph), dummy_island, 2, current_bombs, set(), output)


original = { (0, 1), (0, 2), (0, 3), (0, 4), (0, 5) }
set1 = { (0, 1), (0, 2), (0, 3) }
set2 = { (0, 1), (0, 3), (0, 4) }
set3 = { (0, 2), (0, 3), (0, 5) }

all_sets = [set1, set2, set3]

safe_space = { (0, 1), (0, 2), (0, 3), (0, 4), (0, 5) }
#for st in all_sets:
 #   safe_space = (original ^ st) & safe_space
  #  print(safe_space)

print(safe_space)
print()

print((original ^ set3) & safe_space)





[?, ?, ?, ?]
[P, S, S, S] 
    [P, P, S, S]
        [P, P, P, S] x
        [P, P, S, P]
    [P, S, P, S]
        [P, P, P, S] x
        [P, S, P, P]
[S, P, S, S]
    [P, P, S, S] x
        memo
    []

[S, S, P, S]


[S, S, S, P]
"""

# Very interesting design pattern
for i in range(10):
    for j in range(10):
        print(i, j)
        if i == 6:
            break
    else:
        continue
    break


reference_raw = """1 1 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0
    x 1 0 1 x 1 0 0 2 x 2 0 0 0 0 1 x 2 1
    1 1 0 2 3 3 1 1 3 x 2 0 0 0 0 1 2 x 1
    0 1 1 2 x x 1 2 x 3 1 0 0 0 0 0 1 1 1
    0 1 x 2 2 2 1 3 x 3 0 0 0 0 0 0 0 0 0
    0 1 1 1 0 0 0 2 x 2 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 1 1 1 1 2 2 1 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 1 x x 1 0 0 0 0 0
    0 0 1 1 1 0 1 1 1 0 1 2 2 1 0 0 0 0 0
    0 0 1 x 2 1 3 x 2 0 0 0 0 0 0 1 1 1 0
    0 0 1 1 2 x 3 x 3 1 1 0 0 0 0 1 x 1 0
    0 0 0 0 1 2 3 2 2 x 1 0 0 0 0 1 1 1 0
    0 0 0 0 0 1 x 1 1 1 1 0 0 0 0 0 1 1 1
    0 0 1 1 2 2 2 1 0 0 0 0 0 0 0 0 1 x 1
    0 0 1 x 2 x 2 1 1 0 0 0 0 0 0 0 1 1 1
    0 0 1 1 2 1 3 x 3 1 0 0 0 0 0 0 0 1 1
    0 0 0 0 0 0 2 x x 1 0 0 0 1 1 1 0 1 x
    0 0 0 1 1 1 1 2 2 1 0 0 0 1 x 1 1 2 2
    0 0 0 1 x 3 2 1 0 0 0 1 1 2 1 1 1 x 2
    0 0 0 1 2 x x 1 0 0 0 1 x 1 0 1 2 3 x
    0 0 0 0 1 2 2 1 1 1 1 1 1 1 0 1 x 3 2
    0 0 0 0 1 1 1 1 2 x 1 1 1 1 0 2 3 x 2
    0 0 0 0 1 x 1 1 x 2 1 1 x 1 0 1 x 3 x"""

count = 0
for let in reference_raw:
    if let == 'x':
        print(let)
        count += 1
print(count)