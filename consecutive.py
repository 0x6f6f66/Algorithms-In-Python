testArray = [2, 3, 4, 5, 7, 8, 9]


def first_non_consecutive(array):
    for x, i in enumerate(array, array[0]):
        print(f"x: {x} | i: {i}")  # testing
        if x != i:
            return i


print(first_non_consecutive(testArray))
