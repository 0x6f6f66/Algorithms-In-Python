def move_zeros(array):
    zeroes = []
    numbers = []
    for elem in array:
        zeroes.append(elem) if elem == 0 else numbers.append(elem)
    array = numbers + zeroes
    return array

array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

print(move_zeros(array))

