def groupSort(arr):
    result = []
    hmap = {}

    # Count unique integers using an hmap
    for i in arr:
        if i in hmap:
            hmap[i] += 1
        else:
            hmap[i] = 1

    # Place elements in a 2D array
    for k in hmap.keys():
        result.append([k, hmap[k]])

    temp = result.copy()

    # Sort the 2D array again
    print(f"result before sorting: {result}")
    result.sort(key=lambda y: (-y[1], y[0]))
    print(f"-y[1], y[0]: \t{result}\n")

    test = lambda x: (-x[1], x[0])

    for t in temp:
        print(f"t: {t} | test: {test(t)}")

    # result.sort(key=lambda y: (y[0], y[1]))
    # print(f" y[0], y[1]: \t{result}")

    return hmap


if __name__ == '__main__':
    example = [7, 12, 3, 12, 14]
    groupSort(example)
