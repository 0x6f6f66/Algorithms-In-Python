"""
https://structy.net/problems/premium/create-combinations
"""


def create_combinations(items, k):
    if k == 0:
        return [[]]

    if len(items) < k:
        return []

    first = items[0] # a

    combined_with_first = [] # [ [a, b] [a, c] ]
    for comb in create_combinations(items[1:], k - 1): # [ [b], [c] ]
        combined_with_first.append([first] + comb)

    combined_without_first = create_combinations(items[1:], k) # [ [b, c] ]

    return combined_with_first + combined_without_first


if __name__ == '__main__':
    print(create_combinations(["a", "b", "c"], 2))  # ->
    # [
    #   [ 'a', 'b' ],
    #   [ 'a', 'c' ],
    #   [ 'b', 'c' ]
    # ]