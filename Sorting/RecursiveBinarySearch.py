def recursive_binary_search(list, target):
    print(list)
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2  # It rounds it down

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


test = [i for i in range(0, 9000)]
target = 0

print(recursive_binary_search(test, target))