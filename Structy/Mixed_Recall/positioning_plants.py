"""
https://structy.net/problems/premium/positioning-plants
"""


def positioning_plants(costs):
    min_cost = float('inf')
    memo = {}
    for j in range(len(costs[0])):
        cost = _positioning_plants(costs, 0, j, memo)
        min_cost = min(cost, min_cost)

    return min_cost


def _positioning_plants(costs, i, j, memo):
    if i == len(costs):
        return 0

    key = (i, j)
    if key in memo:
        return memo[key]

    options = []
    for x in range(0, len(costs[i])):
        if x != j:
            cost = costs[i][x] + _positioning_plants(costs, i + 1, x, memo)
            options.append(cost)

    memo[key] = min(options)
    return memo[key]

"""
    [9, 3, 7]
    [6, 1, 9]
    [2, 5, 3]

    9 - 3 - 7
    0   1   2
    
    6 - 1 - 9
    0   1   2
    
    2 - 5 - 3
    0   1   2  
                                                  9 - 3 - 7
                                                  0   1   2
                                                     root
                              /                       |                    \
         0                  9 (0)                    3 (1)                 7 (2)
                         /        \               /         \            /      \
         1             1(1)        9(2)         6(0)        9(2)        6(0)     1(1)
                     /    \        / \         /   \        /  \        /  \      /   \
         2         2(0)    3(2)  2(0) 5(1)    5(1) 3(2)   2(0) 5(1)   5(1) 3(2) 2(0) 3(2) 
"""


if __name__ == '__main__':
    print(positioning_plants([
        [4, 3, 7],
        [6, 1, 9],
        [2, 5, 3]
    ]))  # -> 7, by doing 4 + 1 + 2.

    print(positioning_plants([
        [12, 14, 5],
        [6, 3, 2]
    ]))  # -> 8

    print(positioning_plants([
        [12, 14, 5],
        [6, 3, 2],
        [4, 2, 7],
        [4, 8, 4],
        [1, 13, 5],
        [8, 6, 7],
    ]))  # -> 23

