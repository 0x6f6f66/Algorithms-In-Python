"""
        0    1    2    3    4    5
0    [['?', '?', '?', '?', '?', '?'], 
1     ['?', '?', '?', '?', '?', '?'], 
2     ['?', '?', '?', '0', '?', '?'], 
3     ['?', '?', '?', '?', '?', '?'],  
4     ['?', '?', '?', '?', '?', '?'],  
5     ['0', '0', '0', '?', '?', '?']] 
"""

"""
    [['?', '?', '?', '?', '?', '?'],
     ['?', '?', '2', '1', '2', '?'],
     ['?', 'x', '2', '0', '1', '?'],
     ['?', 'x', '2', '1', '2', '?'], 
     ['1', '1', '1', '1', 'x', '?'], 
     ['0', '0', '0', '1', '?', '?']]
"""

"""
    [['?', '?', '?', '?', '?', '?'],
     ['?', '?', '2', '1', '2', '?'], 
     ['?', '?', '2', '0', '1', '?'],
     ['?', '?', '2', '1', '2', '?'], 
     ['1', '1', '1', '1', '?', '1'],
     ['0', '0', '0', '1', '?', '1']]
"""

"""
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
"""

from collections import deque
from typing import Dict, List, Tuple, Set, Optional
from copy import deepcopy
from rich import print as rprint

spaces_opened = 0


# This is a custom uncover method
def uncover(graph, row, col):
    global spaces_opened
    spaces_opened += 1

    # just need to replace reference[row][col] with str(open(row, col)) for codewars
    val = reference[row][col]
    if val == 'x':
        raise ValueError("You just opened a bomb")
    graph[row][col] = val
    return int(val)


# Custom method for uncovering a bomb, as i need to keep track of
# spaces opened
def uncover_bomb(graph, row, col):
    global spaces_opened
    spaces_opened += 1
    graph[row][col] = 'x'


# Main solution method
# n = bombs remaining
def solve_mine(graph, n):
    # graph = make_graph(map)
    uncover_safe(graph)

    use_tank, n = basic_strategy(graph, n)

    # We solved the entire graph, and we don't need to use tank. Let's open all question marks
    if not use_tank:
        final_uncover(graph)
        return assemble_result(graph)

    # TEMP TEMP TEMP
    # strategy works, but needs to be REALLY optimized!!!

    # Do while emulation
    while True:
        did_tank_work = tank_strategy(graph, n)

        # If Tank didn't work
        if not did_tank_work:
            print(f'[DEBUG] Final Graph: | n: {n} | spaces opened: {spaces_opened}')
            rprint(f'{assemble_pretty_result(graph)}')
            return '?'

        result, n = basic_strategy(graph, n)

        if n <= 0:
            break

    final_uncover(graph)
    # return assemble_result(graph) # for normal result
    return assemble_pretty_result(graph)


# Returns boolean value, whether we should use tank or not
# And returns number of bombs left
def basic_strategy(graph, n) -> (bool, int):
    prev_n = n
    tries = 3
    while n != 0:

        # print(f"Current n: {n}, tries: {tries}")
        # print(f'{graph}')
        n -= solve(graph)

        if prev_n == n:
            tries -= 1
        else:
            tries = 3

        # We have exhausted the basic strategy, time to bring out the big guns
        if tries == 0:
            return (True, n)

        prev_n = n

    return (False, n)


# Brute Force, multi-evalutaion strategy.
# Very complex. Very fancy.
def tank_strategy(graph, n):
    visited_borders = set()

    island = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            island = explore_island(graph, i, j, visited_borders)
            if island:
                break
        else:
            continue
        break

    # print(f'island: {island}')
    # print(f'all islands: {all_islands}')
    # print(f'bombs left: {n}')

    # Possible solution = Bomb locations for that island.
    # (There can be multiple, but most likely, there will also be spaces we can open safely
    bomb_limit = n
    current_bombs = []
    possible_solutions = []
    # Minimum 1 bomb, maximum all bombs remaining
    # Populates possible_solutions with all valid bomb and safe placement combinations, for minimum and max
    # amount of bombs.
    # print(f'[DEBUG] Bomb limit: {bomb_limit} == {n}')

    # Performance improver. We don't need to check every place in a graph to find out if it's valid
    # We can just iterate over the places relevant to that particular island, and check their validity.
    check_only = find_places_to_check(graph, island)
    tank_solve_island(graph, island, bomb_limit, current_bombs, set(), check_only, possible_solutions)
    # If no possible solutions exist for this island, we can't answer with certainty.
    if not possible_solutions:
        # print('No possible solutions')
        return False

    safe_spaces = get_safe_spaces(island, possible_solutions)

    # I suppose, if there are no safe spaces, program will not open anything.
    # I'll temporarily place a print statement to catch that behaviour when it happens.
    if not safe_spaces:
        # This is not a for sure behaviour, we need to add another branch of logic here, as not having all safe
        # spaces doens't necessarily mean this code has failed.
        # TODO:
        #  Write evaluation function to cover safe_spaces edge cases.
        """
        for solution in possible_solutions:
            # Evaluate this solution
            evaluate(graph, solution)
        """

        print('No safe spaces')
        # We have no safe_spaces to open. Tank strategy failed. Result depends on probability.
        # Just return False in this case, which will then evaluate to '?'
        return False

    # print(f'safe_spaces: {safe_spaces}')
    for safe_space in safe_spaces:
        row, col = safe_space
        uncover(graph, row, col)

    return True


# Simply uncover all '?'. This should only be used as a clean up, after all main algorithms have completed.
def final_uncover(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == '?':
                uncover(graph, i, j)


# Make graph from raw string
def make_graph(map):
    rows = map.split("\n")
    graph = []
    for row in rows:
        graph.append(row.split())

    return graph


# Turn a graph back into a string
def assemble_result(graph):
    return '\n'.join(' '.join(col for col in row) for row in graph)


# Could be temp, but also very inefficient function
# Make pretty result from graph
def assemble_pretty_result(graph):
    bomb_color = '[bright_red]'
    default_color = '[grey93]'
    qcolor = '[green1]'

    final = f'{default_color}'
    for row in graph:
        for letter in row:
            if letter == 'x':
                final += bomb_color
            elif letter == '?':
                final += qcolor

            final += f'{letter} '

            if letter == 'x':
                final += default_color
            elif letter == '?':
                final += default_color

        final += '\n'
    return final

# Uncover all safe numbers (all numbers next to 0)
def uncover_safe(graph):
    visited = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "0":
                explore_tiles(graph, i, j, visited)


# BFS Traverse all numbers next to 0, and open them
def explore_tiles(graph, row, col, visited):
    queue = deque([(row, col)])

    deltas = [
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

        num_of_mines = uncover(graph, current_row, current_col)
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
def solve(graph):
    bombs_discovered = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            bombs_discovered += analyze_position(graph, i, j)

    return bombs_discovered


# Analyze current position, and get information from adjacent tiles
def analyze_position(graph, row, col):
    current_val: str = graph[row][col]
    # Early return if the value is unknown, or it's a bomb
    if current_val == '?' or current_val == 'x':
        return 0

    info: Dict[str, list] = get_info(graph, row, col)
    bombs_discovered = solve_position(graph, int(current_val), info)

    return bombs_discovered


# Get information from adjacent tiles
def get_info(graph, row, col):
    info = {
        "question_marks": [],
        "bombs": []
    }

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

        pos = (neighbour_row, neighbour_col)
        if graph[neighbour_row][neighbour_col] == '?':
            info["question_marks"].append(pos)
        elif graph[neighbour_row][neighbour_col] == 'x':
            info["bombs"].append(pos)

    return info


def solve_position(graph, current_val: int, info):
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
        return 0

    bombs_discovered = 0

    # All are bombs
    if (num_of_bombs + num_of_question_marks) == current_val:
        for question_mark_pos in all_question_marks:
            r, c = question_mark_pos
            uncover_bomb(graph, r, c)
            bombs_discovered += 1
        return bombs_discovered

    # All bombs discovered, but some question marks remain. That means they are all safe.
    if (num_of_question_marks > 0) and (num_of_bombs == current_val):
        for question_mark_pos in all_question_marks:
            r, c = question_mark_pos
            uncover(graph, r, c)
        return bombs_discovered

    # We haven't discovered all bombs, and there are more question marks available than bombs remaining
    if (num_of_bombs < current_val) and (num_of_question_marks > current_val - num_of_bombs):
        # print(f"Difficult edge case")
        # print(f"    current: {current_val}")
        # print(f"    info: {info}")
        # print()
        return 0

    # print("THIS ISNT SUPPOSED TO RETUUUURN, AAAAAAAAAAAA")


# Explore all question marks, and assemble them into an island
def explore_island(graph, r, c, visited) -> Set[Optional[Tuple[int, int]]]:
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

    # TODO: remember to change back
    # TEMP MODIFIED, WAS ORIGINALY: 'not is_valid_for_explore'
    if not is_valid_for_explore(graph, r, c):
        return island

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


# Find places to check around an island. We need this in tank_solve_island
# and in try_tank_solution inside that.
# This is a performance improver, as we don't need to iterate over the entire graph in try_tank_solution.
def find_places_to_check(graph, island: Set[Optional[Tuple[int, int]]]) -> Set[Optional[Tuple[int, int]]]:
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
def find_all_alphanum(graph, row, col) -> Set[Optional[Tuple[int, int]]]:
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
                      output: List[Set[Tuple[int, int]]]):
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

    key = make_key(bomb_limit, current_bombs)
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
        output.append(set(current_bombs))

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
            tank_solve_island(graph, island, bomb_limit - 1, current_bombs, visited, check_only, output)
            current_bombs.remove(pos)
            graph[row][col] = '?'

    return


def make_modified_graph(graph, current_bombs: List[Tuple[int, int]], island):
    for bomb in current_bombs:
        row, col = bomb
        graph[row][col] = 'P'

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if ((i, j) in island) and (graph[i][j] == '?'):
                graph[i][j] = 'S'

    return graph


# Make a custom string key to use in visited set
def make_key(number: int, arr: List[Tuple[int, int]]) -> str:
    if not arr:
        return 'NONE'

    key = [f'{number}']

    for elem in arr:
        suffix = str(elem)
        key.append(suffix)

    return '-'.join(key)


def try_tank_solution(graph, check_only):
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
def check_tank_position(graph, row, col):
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


def get_safe_spaces(island: Set[Optional[Tuple[int, int]]],
                    possible_solutions: List[Optional[Set[Tuple[int, int]]]]) -> Set[Optional[Tuple[int, int]]]:
    # All spaces found in island, but not in possible solution (aka, safe spaces)
    # This code is about to get f&#*@ing confusing.
    original: Set[Tuple[int, int]] = set(island)
    safe_spaces: Set[Tuple[int, int]] = set(island)
    # print(f'possible solutions: {possible_solutions}')
    for solution in possible_solutions:
        safe_spaces = (original ^ solution) & safe_spaces  # I'm pretty proud of this bad boy.

    return safe_spaces


if __name__ == '__main__':
    # 43 bombs
    reference1 = """1 1 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0
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

    graph1 = """? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? 0
    ? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ?
    ? ? 0 ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ?
    0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
    0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
    0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0 0 0 0 0
    0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? 0 0 0 0 0
    0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0
    0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
    0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
    0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
    0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
    0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
    0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ?
    0 0 0 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ?
    0 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ?
    0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
    0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
    0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
    0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
    0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?"""

    # 45 bombs
    reference2 = """0 0 0 0 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0
    0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 0 0 0 2 x 2 1 x 1 0
    1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 1 2 x 1 0 0 0 0 2 x 2 1 1 1 0
    1 x 1 1 1 1 0 1 x 2 1 1 0 0 1 x 2 1 1 0 0 0 0 1 1 1 0 0 0 0
    1 2 2 3 x 2 0 1 1 2 x 1 0 0 1 2 2 1 0 0 0 0 0 1 1 1 0 0 1 1
    0 1 x 3 x 2 0 0 0 1 1 1 0 1 2 3 x 1 0 0 0 0 0 1 x 1 0 0 1 x
    0 1 1 3 3 3 2 1 1 1 1 2 1 2 x x 2 2 1 1 0 0 0 1 1 1 1 1 2 1
    0 0 0 1 x x 2 x 1 1 x 2 x 2 3 3 3 2 x 1 0 1 1 1 0 0 2 x 2 0
    0 1 1 2 2 2 3 2 2 1 1 2 1 1 1 x 2 x 2 1 0 1 x 1 0 0 2 x 2 0
    1 2 x 1 0 1 2 x 1 0 0 0 1 1 2 2 3 2 1 0 0 1 1 1 0 0 1 1 1 0
    1 x 2 1 0 1 x 3 2 1 0 0 1 x 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 0
    1 1 2 1 2 2 2 2 x 1 0 0 1 1 1 1 2 x 1 0 0 0 1 x 2 1 0 0 0 0
    1 1 2 x 2 x 1 1 1 1 0 0 0 0 1 1 2 1 1 0 0 0 1 2 x 1 0 0 0 0
    1 x 3 2 2 1 1 0 0 1 1 1 0 0 1 x 1 0 0 0 0 0 1 2 2 1 0 0 0 0
    1 2 x 1 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 x 1 0 0 0 0 0"""

    graph2 = """0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0
    0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
    ? ? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
    ? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 0 0
    ? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
    0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
    0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ?
    0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
    0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
    ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0
    ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
    ? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
    ? ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
    ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? ? 0 0 0 0
    ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0 0"""

    expected2 = """0 0 0 0 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0
    0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 0 0 0 2 x 2 1 x 1 0
    1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 1 2 x 1 0 0 0 0 2 x 2 1 1 1 0
    1 x 1 1 1 1 0 1 x 2 1 1 0 0 1 x 2 1 1 0 0 0 0 1 1 1 0 0 0 0
    1 2 2 3 x 2 0 1 1 2 x 1 0 0 1 2 2 1 0 0 0 0 0 1 1 1 0 0 1 1
    0 1 x 3 x 2 0 0 0 1 1 1 0 1 2 3 x 1 0 0 0 0 0 1 x 1 0 0 1 x
    0 1 1 3 3 3 2 1 1 1 1 2 1 2 x x 2 2 1 1 0 0 0 1 1 1 1 1 2 1
    0 0 0 1 x x 2 x 1 1 x 2 x 2 3 3 3 2 x 1 0 1 1 1 0 0 2 x 2 0
    0 1 1 2 2 2 3 2 2 1 1 2 1 1 1 x 2 x 2 1 0 1 x 1 0 0 2 x 2 0
    1 2 x 1 0 1 2 x 1 0 0 0 1 1 2 2 3 2 1 0 0 1 1 1 0 0 1 1 1 0
    1 x 2 1 0 1 x 3 2 1 0 0 1 x 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 0
    1 1 2 1 2 2 2 2 x 1 0 0 1 1 1 1 2 x 1 0 0 0 1 x 2 1 0 0 0 0
    1 1 2 x 2 x 1 1 1 1 0 0 0 0 1 1 2 1 1 0 0 0 1 2 x 1 0 0 0 0
    1 x 3 2 2 1 1 0 0 1 1 1 0 0 1 x 1 0 0 0 0 0 1 2 2 1 0 0 0 0
    1 2 x 1 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 x 1 0 0 0 0 0"""

    # 44 bombs
    reference3 = """0 0 0 1 2 3 x 1 0 0 0 0 0 0 1 x 1 0 0 0 1 1 1 1 1 1
    0 0 0 1 x x 2 1 0 0 0 1 1 1 1 1 1 0 0 1 2 x 1 1 x 1
    0 1 2 3 4 3 3 1 1 1 1 2 x 1 0 0 0 0 0 2 x 3 1 1 1 1
    0 1 x x 2 x 2 x 1 1 x 2 1 1 0 0 0 0 0 2 x 2 0 0 0 0
    0 1 2 2 2 1 2 1 1 1 1 1 0 0 0 0 0 0 0 1 2 2 1 0 0 0
    0 0 1 2 2 1 0 0 0 1 1 1 0 0 0 1 1 1 1 1 2 x 1 0 0 0
    0 0 1 x x 1 0 0 0 1 x 1 0 0 0 1 x 1 1 x 2 1 1 0 0 0
    1 1 2 3 3 2 0 0 0 1 1 1 1 1 2 2 2 1 1 1 1 0 0 0 0 0
    1 x 2 2 x 1 0 0 0 0 0 0 1 x 2 x 1 0 0 1 1 1 0 0 0 0
    1 2 x 2 1 1 0 0 0 0 0 0 1 1 2 2 2 1 1 3 x 2 0 0 0 0
    0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 2 x 1 1 x x 2 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 1 x 2 1 2 2 3 2 2 1 1 0 0
    0 0 0 0 0 1 1 1 0 0 0 0 0 1 1 1 1 2 x 1 0 1 x 1 1 1
    0 0 0 0 0 1 x 1 0 1 1 1 0 0 0 0 1 x 3 2 1 1 1 1 1 x
    0 1 1 2 1 2 1 1 0 1 x 1 0 0 0 0 1 1 2 x 1 0 0 0 1 1
    0 2 x 3 x 1 0 0 1 2 2 1 0 0 0 1 1 1 2 2 2 0 0 0 1 1
    0 2 x 3 1 1 0 0 1 x 1 0 0 0 0 1 x 1 1 x 1 0 0 0 1 x"""

    graph3 = """0 0 0 ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ?
    0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ?
    0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ?
    0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0
    0 ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 0
    0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ? ? 0 0 0
    0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ? ? 0 0 0
    ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0
    ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? 0 0 ? ? ? 0 0 0 0
    ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0
    0 ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? 0 0
    0 0 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? 0 ? ? ? ? ?
    0 0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? ? ? ? ?
    0 ? ? ? ? ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 ? ?
    0 ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? 0 0 0 ? ?
    0 ? ? ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? 0 0 0 ? ?"""

    # 4 Bombs
    reference4 = """0 0 0 0
    0 0 0 0
    1 1 0 0
    x 2 1 1
    x 3 1 x
    x 2 1 1
    1 1 0 0
    0 0 0 0
    0 0 0 0
    0 0 0 0"""

    graph4 = """0 0 0 0
    0 0 0 0
    ? ? 0 0
    ? ? ? ?
    ? ? ? ?
    ? ? ? ?
    ? ? 0 0
    0 0 0 0
    0 0 0 0
    0 0 0 0"""

    # 18 Bombs
    reference5 = """0 0 0 0 0 0 0 0 1 x x 2 1 0 1 x 1 0 1 2 x
    0 0 0 0 0 0 0 0 1 2 3 x 1 0 2 2 2 1 2 x 2
    0 0 0 0 0 0 0 0 0 0 2 2 2 0 1 x 1 1 x 2 1
    0 0 0 0 0 1 1 1 0 0 1 x 1 0 1 2 2 2 1 1 0
    1 1 0 0 0 1 x 1 0 1 2 2 1 0 0 1 x 1 1 1 1
    x 1 0 0 0 1 1 1 0 1 x 1 0 0 0 1 1 1 1 x 1
    2 2 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1
    1 x 1 0 0 0 0 0 0 0 1 2 2 1 0 0 1 1 1 0 0
    1 1 1 0 0 0 0 0 0 0 1 x x 1 0 0 1 x 1 0 0"""

    graph5 = """0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? 0 ? ? ?
    0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ?
    0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ?
    0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 ? ? ? ? ? ? 0
    ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ?
    ? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ?
    ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ?
    ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
    ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0"""

    # 23 Bombs
    reference6 = """0 0 0 0 0 0 0 1 1 1
    1 1 1 1 1 1 0 2 x 2
    1 x 2 2 x 1 0 2 x 2
    1 1 2 x 2 1 0 1 1 1
    0 0 2 2 2 1 1 1 0 0
    0 0 1 x 1 1 x 2 1 1
    0 0 1 1 2 2 2 3 x 2
    0 0 0 0 1 x 1 2 x 2
    0 0 0 0 1 1 1 1 1 1
    0 0 0 1 2 2 1 0 0 0
    0 0 0 1 x x 1 0 0 0
    0 0 0 1 2 2 1 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    1 1 0 1 1 1 0 0 0 0
    x 1 0 1 x 1 0 0 0 0
    2 3 1 3 2 2 1 1 1 0
    x 2 x 2 x 1 1 x 2 1
    1 2 1 2 1 1 1 2 x 1
    0 0 1 1 1 0 0 1 1 1
    0 0 1 x 1 1 1 2 2 2
    0 0 1 1 1 1 x 2 x x
    0 0 0 0 0 1 1 2 2 2"""

    graph6 = """0 0 0 0 0 0 0 ? ? ?
    ? ? ? ? ? ? 0 ? ? ?
    ? ? ? ? ? ? 0 ? ? ?
    ? ? ? ? ? ? 0 ? ? ?
    0 0 ? ? ? ? ? ? 0 0
    0 0 ? ? ? ? ? ? ? ?
    0 0 ? ? ? ? ? ? ? ?
    0 0 0 0 ? ? ? ? ? ?
    0 0 0 0 ? ? ? ? ? ?
    0 0 0 ? ? ? ? 0 0 0
    0 0 0 ? ? ? ? 0 0 0
    0 0 0 ? ? ? ? 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    ? ? 0 ? ? ? 0 0 0 0
    ? ? 0 ? ? ? 0 0 0 0
    ? ? ? ? ? ? ? ? ? 0
    ? ? ? ? ? ? ? ? ? ?
    ? ? ? ? ? ? ? ? ? ?
    0 0 ? ? ? 0 0 ? ? ?
    0 0 ? ? ? ? ? ? ? ?
    0 0 ? ? ? ? ? ? ? ?
    0 0 0 0 0 ? ? ? ? ?"""

    tiny_graph = "?"
    tiny_reference = "x"

    tiny_graph2 = "0 ? ?"
    tiny_reference2 = "0 1 x"

    reference = make_graph(reference5)
    graph = make_graph(graph5)

    print('Result:')
    rprint(solve_mine(graph, 18))
    print()
    print('Expected:')
    rprint(assemble_pretty_result(reference))