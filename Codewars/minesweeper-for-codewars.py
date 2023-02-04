from collections import deque
from typing import Dict, List, Tuple, Set, Optional, Union
from copy import deepcopy
from preloaded import open


def increment(spaces_opened: List[int]) -> None:
    spaces_opened[0] += 1


def decrement(bombs_left: List[int]) -> None:
    bombs_left[0] -= 1


# This is a custom uncover method
def uncover(graph, row: int, col: int, spaces_opened: List[int]) -> int:
    increment(spaces_opened)

    # just need to replace reference[row][col] with str(open(row, col)) for codewars
    val = str(open(row, col))
    if val == 'x':
        raise ValueError("You just opened a bomb")
    graph[row][col] = val
    return int(val)


# Custom method for uncovering a bomb, as i need to keep track of
# spaces opened
def uncover_bomb(graph, row: int, col: int, bombs_left: List[int], spaces_opened: List[int]) -> None:
    increment(spaces_opened)
    decrement(bombs_left)
    graph[row][col] = 'x'


# Mark a potentially safe space, without opening it.
def mark_safe_space(graph, row: int, col: int, spaces_opened: List[int]) -> None:
    if graph[row][col] != '?':
        print(f"[ALERT] We aren't supposed to be marking this space!")
        print(f'row: {row} | col: {col}')
        print(f'Graph: {graph}')
        raise ValueError("You just marked an invalid space.")

    graph[row][col] = 'S'
    increment(spaces_opened)


# Main solution method
# n = bombs remaining
def solve_mine(map, n: int, spaces_opened: Optional[List[int]] = None):
    graph = make_graph(map)
    if spaces_opened is None:
        spaces_opened = [0]

    uncover_safe(graph, spaces_opened)

    bombs_left: List[int] = [n]

    # If the entire board is made of bombs. -> uncover it all, and return
    if (spaces_opened[0] == 0) and (len(graph) * len(graph[0])) == bombs_left[0]:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                uncover_bomb(graph, i, j, bombs_left, spaces_opened)
        return assemble_result(graph)

    use_tank = basic_strategy(graph, bombs_left, spaces_opened)

    # We solved the entire graph, and we don't need to use tank. Let's open all question marks
    if not use_tank:
        final_uncover(graph, spaces_opened)
        return assemble_result(graph)

    # TEMP TEMP TEMP
    # strategy works, but needs to be REALLY optimized!!!

    # Do while emulation
    while True:
        did_tank_work = tank_strategy(graph, bombs_left, spaces_opened, False, 0)

        # If Tank didn't work
        if not did_tank_work:
            # print(f'[DEBUG] Final Graph: | bombs_left: {bombs_left} | spaces opened: {spaces_opened}')
            # rprint(f'{assemble_pretty_result(graph)}')
            return '?'

        # TODO: Note that we're ignoring result of basic_strategy here
        result = basic_strategy(graph, bombs_left, spaces_opened)

        if bombs_left[0] <= 0:
            break

    final_uncover(graph, spaces_opened)
    # return assemble_result(graph) # for normal result
    return assemble_result(graph)


# Returns boolean value, whether we should use tank or not
def basic_strategy(graph, bombs_left: List[int], spaces_opened: List[int]) -> bool:
    n = bombs_left[0]
    prev_n = n
    tries = 3

    while n != 0:

        # print(f"Current n: {n}, tries: {tries}")
        # print(f'{graph}')
        solve(graph, bombs_left, spaces_opened)

        n = bombs_left[0]

        if prev_n == n:
            tries -= 1
        else:
            tries = 3

        # We have exhausted the basic strategy, time to bring out the big guns
        if tries == 0:
            # We always must update the number of bombs left after returning
            bombs_left[0] = n
            return True

        prev_n = n

    bombs_left[0] = n
    return False


# Brute Force, multi-evalutaion strategy.
# Very complex. Very fancy.
def tank_strategy(graph, bombs_left: List[int], spaces_opened: List[int], recursive_call: bool, recursion_depth: int,
                  memo=None) -> bool:
    if recursion_depth > 5:
        return False

    # print(f'Calling tank on graph:')
    # rprint(assemble_pretty_result(graph))
    # print(f'recur depth: {recursion_depth}')

    if memo is None:
        memo = {}

    visited_borders: Set[Optional[Tuple[int, int]]] = set()

    all_islands = []
    island = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            island = explore_island(graph, i, j, visited_borders)
            if island:
                all_islands.append(island)

    if all_islands:
        # Investigate the smallest of all islands.
        smallest = float('inf')
        smallest_island = None
        for islnd in all_islands:
            if len(islnd) < smallest:
                smallest_island = islnd

        island = smallest_island

    # If we uncovered all bombs, and there are no remaining islands
    if bombs_left[0] == 0 and not island:
        return True

    # print(f'island: {island}')
    # print(f'all islands: {all_islands}')
    # print(f'bombs left: {n}')

    # Let's check, maybe the entire remaining island is made of bombs.
    spaces_left = (len(graph) * len(graph[0])) - spaces_opened[0]
    if (bombs_left[0] == len(island)) and (spaces_left == bombs_left[0]):
        for row, col in island:
            uncover_bomb(graph, row, col, bombs_left, spaces_opened)
        return True

    # Possible solution = Bomb locations for that island.
    # (There can be multiple, but most likely, there will also be spaces we can open safely
    bomb_limit = bombs_left[0]
    current_bombs = []
    possible_solutions: List[Optional[Set[Tuple[int, int]]]] = []
    # Minimum 1 bomb, maximum all bombs remaining
    # Populates possible_solutions with all valid bomb and safe placement combinations, for minimum and max
    # amount of bombs.
    # print(f'[DEBUG] Bomb limit: {bomb_limit} == {n}')

    # Performance improver. We don't need to check every place in a graph to find out if it's valid
    # We can just iterate over the places relevant to that particular island, and check their validity.
    check_only = find_places_to_check(graph, island)
    tank_solve_island(graph, island, bomb_limit, current_bombs, set(), check_only, possible_solutions, recursive_call)

    # If no possible solutions exist for this island, we can't answer with certainty.
    if not possible_solutions:
        # print('No possible solutions')
        return False

    safe_spaces: Set[Tuple[int, int]] = get_safe_spaces(island, possible_solutions)

    # If there are no safe spaces, there is one last check we can do,
    # to recursively find safe spaces.
    if not safe_spaces:
        # print(f'{bombs_left} possible_solutions: {possible_solutions}')
        # print(f'{bombs_left} island: {island}')
        evaluation_result = evaluate_all_solutions(graph, island, possible_solutions, bombs_left, spaces_opened,
                                                   recursion_depth, memo)

        # return False
        return evaluation_result

    # print(f'{bombs_left} safe_spaces: {safe_spaces}')
    # If this is a recursive call, opening "safe" spaces might open a bomb.
    if not recursive_call:
        for safe_space in safe_spaces:
            row, col = safe_space
            uncover(graph, row, col, spaces_opened)

    # We need to check how many bombs are left in the recursive call.
    # It could be, that i will give us a valid solution with 1 bomb uncovered.
    # If it's a recursive call, we need to update the number of bombs we uncovered.
    if recursive_call:
        # Mark safe spaces
        for safe_space in safe_spaces:
            row, col = safe_space
            mark_safe_space(graph, row, col, spaces_opened)

        for solution in possible_solutions:
            # Careful, this might contain an empty set as a solution.
            # When an empty set is contained, for pos in solution will not iterate over anything.
            # Doesn't hurt to check against it though.
            for pos in solution:
                row, col = pos
                uncover_bomb(graph, row, col, bombs_left, spaces_opened)
                # If we haven't uncovered all bombs, that means, we can run tank strategy recursively again.
            if bombs_left != 0:
                if tank_strategy(graph, bombs_left, spaces_opened, True, recursion_depth + 1, memo):
                    return True
        return False

    return True


# Simply uncover all '?'. This should only be used as a clean up, after all main algorithms have completed.
def final_uncover(graph, spaces_opened: List[int]) -> None:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '?':
                uncover(graph, i, j, spaces_opened)


# Make graph from raw string
def make_graph(map):
    rows = map.split("\n")
    graph = []
    for row in rows:
        graph.append(row.split())

    return graph


# Turn a graph back into a string
def assemble_result(graph) -> str:
    return '\n'.join(' '.join(col for col in row) for row in graph)


# Uncover all safe numbers (all numbers next to 0)
def uncover_safe(graph, spaces_opened: List[int]) -> None:
    visited = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "0":
                explore_tiles(graph, i, j, visited, spaces_opened)


# BFS Traverse all numbers next to 0, and open them
def explore_tiles(graph, row: int, col: int, visited: Set[Optional[Tuple[int, int]]], spaces_opened: List[int]) -> None:
    queue = deque([(row, col)])

    deltas: List[Tuple[int, int]] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    while queue:
        current = queue.pop()

        if current in visited:
            continue

        visited.add(current)

        current_row, current_col = current

        num_of_mines = uncover(graph, current_row, current_col, spaces_opened)
        graph[current_row][current_col] = str(num_of_mines)

        if num_of_mines != 0:
            continue

        for delta in deltas:
            delta_row, delta_col = delta
            neighbour_row = current_row + delta_row
            neighbour_col = current_col + delta_col
            neighbour_pos = (neighbour_row, neighbour_col)

            row_inbounds = 0 <= neighbour_row < len(graph)
            col_inbounds = 0 <= neighbour_col < len(graph[0])

            if not row_inbounds or not col_inbounds:
                continue

            queue.appendleft(neighbour_pos)


# Solve current graph
def solve(graph, bombs_left: List[int], spaces_opened: List[int]) -> None:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            analyze_position(graph, i, j, bombs_left, spaces_opened)


# Analyze current position, and get information from adjacent tiles
def analyze_position(graph, row: int, col: int, bombs_left: List[int], spaces_opened: List[int]) -> None:
    current_val: str = graph[row][col]
    # Early return if the value is unknown, or it's a bomb
    if current_val == '?' or current_val == 'x':
        return

    info: Dict[str, list] = get_info(graph, row, col)
    solve_position(graph, int(current_val), info, bombs_left, spaces_opened)

    return


# Get information from adjacent tiles
def get_info(graph, row: int, col: int):
    info = {
        "question_marks": [],
        "bombs": []
    }

    deltas: List[Tuple[int, int]] = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = row + delta_row
        neighbour_col = col + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        pos = (neighbour_row, neighbour_col)
        if graph[neighbour_row][neighbour_col] == '?':
            info["question_marks"].append(pos)
        elif graph[neighbour_row][neighbour_col] == 'x':
            info["bombs"].append(pos)

    return info


def solve_position(graph, current_val: int, info, bombs_left: List[int], spaces_opened: List[int]) -> None:
    """
    ? 2 x
    3 5 x -> 2 question marks, 3 bombs, 5 current val -> All question marks are bombs. 2 bombs uncovered
    ? x 2

    1 ? 1
    2 2 2 -> 2 question marks, 0 bombs, 2 current val -> All question marks are bombs. 2 bombs uncovered
    1 ? 1

    ? ? ?
    x 3 ? -> 5 question marks, 3 bombs, 3 current val -> All question marks are safe. 0 bombs uncovered
    x x ?

    ? ? ?
    ? 4 ? -> 8 question marks, 0 bombs, 4 current val -> Not enough information. 0 bombs uncovered
    ? ? ?

    1 ? ?
    ? 2 ? -> 6 question marks, 0 bombs, 2 current val -> Not enough information. 0 bombs uncovered
    ? ? 1

    if bombs_num + question marks num == current val -> all are bombs

    if question marks num > 0 and bombs num == current val -> all are safe

    if num of bombs < current val and question marks > current val - bombs -> too uncertain, skip
              0        2                6                 2 - 0
    """
    all_question_marks = info["question_marks"]
    all_bombs = info["bombs"]

    num_of_question_marks = len(all_question_marks)
    num_of_bombs = len(all_bombs)

    # Nothing left to discover
    if num_of_question_marks == 0:
        return

    # bombs_discovered = 0

    # All are bombs
    if (num_of_bombs + num_of_question_marks) == current_val:
        for question_mark_pos in all_question_marks:
            r, c = question_mark_pos
            uncover_bomb(graph, r, c, bombs_left, spaces_opened)
        #    bombs_discovered += 1
        # return bombs_discovered

    # All bombs discovered, but some question marks remain. That means they are all safe.
    if (num_of_question_marks > 0) and (num_of_bombs == current_val):
        for question_mark_pos in all_question_marks:
            r, c = question_mark_pos
            uncover(graph, r, c, spaces_opened)
        # return bombs_discovered

    # We haven't discovered all bombs, and there are more question marks available than bombs remaining
    if (num_of_bombs < current_val) and (num_of_question_marks > current_val - num_of_bombs):
        # print(f"Difficult edge case")
        # print(f"    current: {current_val}")
        # print(f"    info: {info}")
        # print()
        return

    # print("THIS ISNT SUPPOSED TO RETUUUURN, AAAAAAAAAAAA")


# Explore all question marks, and assemble them into an island
def explore_island(graph, r: int, c: int, visited: Set[Optional[Tuple[int, int]]]) -> Set[Optional[Tuple[int, int]]]:
    island = set()

    pos = (r, c)

    if pos in visited:
        return island

    if graph[r][c] != '?':
        return island

    """
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
    """

    visited.add(pos)

    if not is_valid_for_explore(graph, r, c):
        return island

    # print(f'[EXPLORING] {pos}')

    island.add(pos)

    deltas = [
        (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
        (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
        (0, -2), (0, -1), (0, 1), (0, 2),
        (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
        (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)
    ]

    """
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    """
    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = r + delta_row
        neighbour_col = c + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        result: Set[Optional[Tuple[int, int]]] = explore_island(graph, neighbour_row, neighbour_col, visited)
        if result:
            island = island | result

    return island


# If there are no alphanumeric characters around a question mark, it should become part of an island (border)
def is_valid_for_explore(graph, r: int, c: int) -> bool:
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

    # Return True if there is at least one alphanumeric character around the '?'
    # OR If the question mark is on the border.
    return (alnum_chars_count != 0) or (border_question_mark(graph, r, c))


# Is this question mark on a border of the graph?
def border_question_mark(graph, row: int, col: int) -> bool:
    # We need to only check question marks
    if graph[row][col] != '?':
        return False

    if ((row == 0) or (row == len(graph) - 1)) and ((col == 0) or (col == len(graph[0]) - 1)):
        # print(f'[ATTENTION] Border question mark! {row} {col}')
        return True

    return False


# Find places to check around an island. We need this in tank_solve_island
# and in try_tank_solution inside that.
# This is a performance improver, as we don't need to iterate over the entire graph in try_tank_solution.
def find_places_to_check(graph, island: Set[Optional[Tuple[int, int]]]) -> Set[Optional[Tuple[int, int]]]:
    # print(f'Checking this island: {island}')
    check_only = set()

    # We can receive an empty island, so we early return.
    if not island:
        return set()

    for pos in island:
        row, col = pos

        # this HAS to be a question mark. If it isn't, something is seriously wrong
        if graph[row][col] != '?':
            print(f"[ERROR] Island doesn't contain a question mark. | island: {island}")

        # Now we just need to find all alphanumeric characters around this question mark
        result = find_all_alphanum(graph, row, col)
        if result:
            check_only = check_only | result

    return check_only


# Helper function for finding all alphanumeric characters.
def find_all_alphanum(graph, row: int, col: int) -> Set[Optional[Tuple[int, int]]]:
    result = set()

    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = row + delta_row
        neighbour_col = col + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        neighbour: str = graph[neighbour_row][neighbour_col]

        if neighbour.isalnum():
            result.add((neighbour_row, neighbour_col))

    return result


# Brute-forcish algorithm to solve for N number of bombs in an island (recursive)
def tank_solve_island(graph, island: Set[Optional[Tuple[int, int]]],
                      bomb_limit: int, current_bombs: List[Tuple[int, int]],
                      visited: Set[Optional[str]], check_only: Set[Tuple[int, int]],
                      output: List[Optional[Set[Tuple[int, int]]]], recursive_call: bool):
    """
    ['?', '?', '?', '?', '?', '?']
    ['2', '2', '2', '1', '2', '2']
    ['2', 'x', '2', '0', '1', 'x']
    ['2', 'x', '2', '1', '2', '2']
    ['1', '1', '1', '1', 'x', '1']
    ['0', '0', '0', '1', '1', '1']

    island = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
    (All coords are question marks)

    Brute Force:
    Case 1:
        ['P', 'P', '?', '?', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 2:
        ['P', '?', 'P', '?', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 3:
        ['P', '?', '?', 'P', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 4:
        ['P', '?', '?', '?', 'P', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 5:
        ['P', '?', '?', '?', '?', 'P']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 6:
        ['?', 'P', 'P', '?', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 7:
        ['?', 'P', '?', 'P', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 8:
        ['?', 'P', '?', '?', 'P', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> Yes.

    Case 9:
        ['?', 'P', '?', '?', '?', 'P']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.

    Case 10:
        ['?', '?', 'P', 'P', '?', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    Is valid? -> Check -> No.
    .
    .
    .
    All subsequent cases will be invalid, as the first square's condition cannot be satisfied.

    Therefore, tank solver figured out one possible solution:
        ['?', 'P', '?', '?', 'P', '?']
        ['2', '2', '2', '1', '2', '2']
        ['2', 'x', '2', '0', '1', 'x']
    """

    # This is just for safety, but code beforehand has been designed in a way, that this WILL have an island.
    # However, doesn't hurt to make extra checks.
    if not island:
        return

    # Make key requires two arguments, so I'm placing 111111 as a nice placeholder.
    key = make_key(bomb_limit, 111111, current_bombs)
    if key in visited:
        return

    modified_graph_with_bombs = make_modified_graph(deepcopy(graph), current_bombs, island)

    """
    This part can be improved.
    We're iterating over the part of the graph we have already assembled, but are still checking it N^2 times.

    Example:
    0 1 2 3 4
  0 T T T T T
  1 T T T T T
  2 T T T ? ?
  3 T T ? ? ?

    Bombs = 1

    Case 1:
    T T T T T
    T T T T T
    T T T P S
    T T S S S

    We don't really need to check again the positions for values, not immidiately next to the border.


    We probably need to place this outside of function's scope, as i will just get called every time the functon runs.
    (And values of the places we need to check around won't change.) 
    # places_to_check = find_places_to_check(island)
    """

    if try_tank_solution(modified_graph_with_bombs, check_only):
        # We're returning a List[Set[Tuple[int, int]]] here, by appending all current bombs
        # after they had been checked through the try_tank_solution() algorithm
        # We must not append an empty set of current bombs.
        if current_bombs:
            output.append(set(current_bombs))

        # TODO:
        #  Alright. A conflict. During recursion, we ARE allowed to output an empty set of bombs, sigifying that we're
        #  accepting the currect configuration of the board.
        if recursive_call and not current_bombs:
            output.append(set())

    visited.add(key)

    if bomb_limit == 0:
        return

    for pos in island:
        row, col = pos
        current = graph[row][col]
        if current == '?':
            graph[row][col] = 'P'
            current_bombs.append(pos)
            current_bombs.sort()
            # This was hard as ?&^% to write.
            tank_solve_island(graph, island, bomb_limit - 1, current_bombs, visited, check_only, output, recursive_call)
            current_bombs.remove(pos)
            graph[row][col] = '?'

    return


def make_modified_graph(graph, current_bombs: List[Tuple[int, int]], island: Set[Optional[Tuple[int, int]]]):
    for bomb in current_bombs:
        row, col = bomb
        graph[row][col] = 'P'

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if ((i, j) in island) and (graph[i][j] == '?'):
                graph[i][j] = 'S'

    return graph


# Make a custom string key to use in visited set
def make_key(first_number: int, second_number: int, arr: Union[List[Tuple[int, int]], Set[Tuple[int, int]]]) -> str:
    key = [f'{first_number}-{second_number}']

    if not arr:
        suffix = '[EMPTY]'
        key.append(suffix)

    for elem in arr:
        suffix = str(elem)
        key.append(suffix)

    return '-'.join(key)


def try_tank_solution(graph, check_only: Set[Tuple[int, int]]) -> bool:
    # Now check the graph, assuming all other question_marks are not bombs
    for pos in check_only:
        row, col = pos
        result: int = check_tank_position(graph, row, col)

        # -1 -> We hit an invalid element. (P, S or x)
        if result == -1:
            continue

        # Early return, as this position is invalid
        if result == 0:
            return False

    return True


# Check current Tank position variation, is it valid? If yes, return 1, if not, return 0,
# if we're at an invalid symbol, return -1
def check_tank_position(graph, row: int, col: int) -> int:
    """
    ['P', 'P', 'S', 'S', 'S', 'S']
    ['2', '2', '2', '1', '2', '2']
    ['2', 'x', '2', '0', '1', 'x']
    ['2', 'x', '2', '1', '2', '2']
    ['1', '1', '1', '1', 'x', '1']
    ['0', '0', '0', '1', '1', '1']
    """
    current_val: str = graph[row][col]

    # Skip checking, if we're at an invalid element
    if current_val == 'P' or current_val == 'S' or current_val == 'x' or current_val == '?':
        return -1

    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    neighbours = {
        'bombs': 0,
        'safe': 0,
        'tiles': 0
    }

    for delta in deltas:
        delta_row, delta_col = delta
        neighbour_row = row + delta_row
        neighbour_col = col + delta_col

        row_inbounds = 0 <= neighbour_row < len(graph)
        col_inbounds = 0 <= neighbour_col < len(graph[0])

        if not row_inbounds or not col_inbounds:
            continue

        neighbour = graph[neighbour_row][neighbour_col]
        neighbours['tiles'] += 1
        # If neighbour is a bomb
        if neighbour == 'P' or neighbour == 'x':
            neighbours['bombs'] += 1
        # If neighbour is safe. (Number, or temp S symbol) (We're just assuming S is safe)
        if neighbour.isnumeric() or neighbour == 'S':
            neighbours['safe'] += 1

    bombs_found: int = neighbours['bombs']
    # Current val is a lower number than we are supposed to find bombs. This position is invalid
    if int(current_val) < bombs_found:
        return 0

    # Current val is bigger than we found bombs, we didn't find enough. This position is invalid
    if int(current_val) > bombs_found:
        return 0

    # We aren't doing any other safety check (though, we could)
    # We just assume that everything else is correct. Return 1.
    return 1


def get_safe_spaces(island: Set[Tuple[int, int]],
                    possible_solutions: List[Optional[Set[Tuple[int, int]]]]) -> Set[Tuple[int, int]]:
    if not possible_solutions:
        return set()

    # All spaces found in island, but not in possible solution (aka, safe spaces)
    # This code is about to get f&#*@ing confusing.
    original: Set[Tuple[int, int]] = set(island)
    safe_spaces: Set[Tuple[int, int]] = set(island)
    for solution in possible_solutions:
        safe_spaces = (original ^ solution) & safe_spaces  # I'm pretty proud of this bad boy.

    return safe_spaces


def evaluate_all_solutions(graph, island: Set[Optional[Tuple[int, int]]],
                           possible_solutions: List[Optional[Set[Tuple[int, int]]]], bombs_left: List[int],
                           spaces_opened: List[int], recursion_depth: int,
                           memo: Dict[str, Tuple[bool, List[int]]]) -> bool:
    all_results = {}
    for index in range(len(possible_solutions)):
        # Keys of all_results relate to indecies of solutions in possible solutions
        solution = possible_solutions[index]
        # Evaluate individual solution.
        # This will return if the solution is valid, and how many bombs it has left open.
        """
        This is an expensive function, we need to memoize it.
        The key is made out of bombs_left and a solution.
        Luckily, i already have a function to assemble memo key.
        """

        solution_result, solution_bombs_left = evaluate(graph, island, solution, bombs_left, spaces_opened,
                                                        recursion_depth, memo)

        all_results[index] = {}
        all_results[index]['result'] = solution_result
        # Save how many bombs were left from the solution result
        all_results[index]['bombs_left'] = solution_bombs_left
        # We save solution for debugging and convenience purposes. We can probably drop it from this dictionary
        all_results[index]['solution'] = solution

    # Now we need to only analyze valid results.
    new_possible_solutions: List[Optional[Set[Tuple[int, int]]]] = []
    # print(f'Call from eval all solutions ({bombs_left} | {possible_solutions}):')
    for index in all_results:
        current = all_results[index]
        # print(f'current solution: {current}')
        result = current['result']
        solution = current['solution']
        if result:
            # print(f'   returned true')
            # print()
            new_possible_solutions.append(solution)

    # TODO: if not new_possible_solutions:
    #  what should we return?
    #  this check exists before another get_safe_spaces, but not before this one.

    # [DEBUG]
    # if new_possible_solutions:
    # print(f'   possible solutions:')
    #    for sol in new_possible_solutions:
    # print(f'    sol: {sol}')

    # Get revised safe spaces from new possible solutions.
    safe_spaces: Set[Tuple[int, int]] = get_safe_spaces(island, new_possible_solutions)

    if not safe_spaces:
        # TODO:
        #  It could be, that we have a possible solution, where an entire island is made of bombs,
        #  hence, no safe spaces.

        """
        Is this a situation, where our entire island is made of bombs?
        SOME LOGIC HERE
        If this is an island made entirely of bombs -> uncover all bombs, return True
        """

        for solution in new_possible_solutions:
            if island_of_bombs(island, solution, bombs_left):
                for pos in island:
                    row, col = pos
                    uncover_bomb(graph, row, col, bombs_left, spaces_opened)
                return True

        # We have no safe_spaces to open. Tank strategy failed. Result depends on probability.
        # Just return False in this case, which will then evaluate to '?'
        # TODO: This result can probably me memoized. Need to think about how though.
        # print(f'{possible_solutions}')
        # print(f'{bombs_left} No safe spaces')
        return False

    for safe_space in safe_spaces:
        row, col = safe_space
        uncover(graph, row, col, spaces_opened)

    return True


# Evaluate validity of individual solution.
def evaluate(graph, island: Set[Optional[Tuple[int, int]]], solution: Set[Tuple[int, int]],
             bombs_left: List[int], spaces_opened: List[int], recursion_depth: int,
             memo: Dict[str, Tuple[bool, List[int]]]) -> Tuple[bool, List[int]]:
    # print(f'[==============]')
    # print(f'[DEBUG] Evaluating {solution} as an edge case solution')
    # print(f'    spaces_left: {spaces_left}')
    # print(f'    bombs_left: {bombs_left}')

    # We could need to decrement the amount of bombs we use for our key,
    # As the return value will relate to the decremented amount of bombs.
    # TODO: Check what is the value of this key supposed to be.
    key = make_key((bombs_left[0] - len(solution)), (spaces_opened[0] + len(solution)), solution)

    if key in memo:
        # print(f'[ALERT] MEMO USED!!! YAY: {key}')
        # print(f'{memo[key]}')
        return memo[key]

    temp_graph = deepcopy(graph)
    temp_bombs_left: List[int] = [bombs_left[0]]
    temp_spaces_opened: List[int] = [spaces_opened[0]]

    for pos in solution:
        row, col = pos
        uncover_bomb(temp_graph, row, col, temp_bombs_left, temp_spaces_opened)

    # If this is an "empty" solution. (Aka, solution which accepts the island as it is)
    # It assumes that the rest of the fields in the island are safe. Therefore, mark them as safe.
    if not solution:
        for row, col in island:
            mark_safe_space(temp_graph, row, col, temp_spaces_opened)

    # print(f'    starting recursive tank strategy with arg: {temp_bombs_left[0]}')
    # if temp_bombs_left[0] == 0:
    # print(f'    SOLUTION WITH 0 BOMBS LEFT!!!!')
    # rprint(f'{assemble_pretty_result(temp_graph)}')
    recursive_call = True
    result = tank_strategy(temp_graph, temp_bombs_left, temp_spaces_opened, recursive_call, recursion_depth + 1, memo)

    memo[key] = (result, temp_bombs_left)
    return result, temp_bombs_left


# Is this an island of bombs?
def island_of_bombs(island: Set[Optional[Tuple[int, int]]],
                    solution: [Set[Tuple[int, int]]],
                    bombs_left: List[int]) -> bool:
    if len(solution) != len(island):
        return False

    if bombs_left[0] != len(island):
        return False

    # print(f'island: {island}')
    # print(f'island of bombs? : {solution} | bombs_left: {bombs_left}')
    # print()

    return True
