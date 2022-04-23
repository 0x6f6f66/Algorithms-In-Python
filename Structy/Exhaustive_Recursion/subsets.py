"""
https://structy.net/problems/premium/subsets
"""


def subsets(elements):
    if len(elements) == 0:
        return [[]]

    first = elements[0] # a
    subsets_without_first = subsets(elements[1:]) # [ [], [c], [b], [b, c] ]

    subsets_with_first = [] # [ [a], [a, c], [a, b], [a, b, c]]
    for sub in subsets_without_first:
        subsets_with_first.append([first, *sub])

    return subsets_without_first + subsets_with_first # [ [], [c], [b], [b, c], [a], [a, c], [a, b], [a, b, c] ]


if __name__ == '__main__':
    print(subsets(['a', 'b', 'c']))  # ->
    # [
    #   [],
    #   [ 'c' ],
    #   [ 'b' ],
    #   [ 'b', 'c' ],
    #   [ 'a' ],
    #   [ 'a', 'c' ],
    #   [ 'a', 'b' ],
    #   [ 'a', 'b', 'c' ]
    # ]