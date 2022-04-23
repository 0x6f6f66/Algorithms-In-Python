"""
https://structy.net/problems/premium/permutations
"""


def permutations(items: list) -> list:
    if len(items) == 0:
        return [[]]

    first = items[0]
    full_permutations = []
    for perm in permutations(items[1:]):
        for i in range(0, len(perm) + 1):
            full_permutations.append(perm[:i] + [first] + perm[i:])

    return full_permutations


if __name__ == '__main__':
    print(permutations(['a', 'b', 'c']))  # ->
    # [
    #   [ 'a', 'b', 'c' ],
    #   [ 'b', 'a', 'c' ],
    #   [ 'b', 'c', 'a' ],
    #   [ 'a', 'c', 'b' ],
    #   [ 'c', 'a', 'b' ],
    #   [ 'c', 'b', 'a' ]
    # ]
