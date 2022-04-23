def merge_sort(list_):
    current_size = 1

    while current_size < len(list_):
        left = 0

        while left < len(list_) - 1:
            mid = left + current_size - 1
            test_val1 = 2 * current_size + left - 1
            test_val2 = len(list_) - 1
            test_val3 = 2 * current_size + left - 1
            test_val4 = test_val3 > test_val1
            right = ((2 * current_size + left - 1, len(list_) - 1)[2 * current_size + left - 1 > len(list_) - 1])
            print(right)




