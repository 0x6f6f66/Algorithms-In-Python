def merge_sort(list_):
    """
    Sorts a list in scending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort of the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    print(f"LIST: {list_}")

    if len(list_) <= 1:
        print(f" LIST RETURNED: {list_}")
        return list_

    left_half, right_half = split(list_)
    print(f"    SPLIT: {left_half}, {right_half}")
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list_):
    middle = len(list_) // 2
    left = list_[:middle]
    right = list_[middle:]
    return left, right


def merge(left: list, right: list):
    l = []
    i = 0  # indexes of left list
    j = 0  # indexes of right list
    print(f"        MERGE: {left}, {right}")

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            print(f"\t\t\tA: left[{i}] < right[{j}]")
            print(f"\t\t\tA:     {left[i]} < {right[j]}")
            print(f"\t\t\tA: appending {left[i]}")
            print()
            l.append(left[i])
            i += 1
        else:
            print(f"\t\t\tB: left[{i}] > right[{j}]")
            print(f"\t\t\tB:     {left[i]} > {right[j]}")
            print(f"\t\t\tB: appending {right[j]}")
            print()
            l.append(right[j])
            j += 1

    while i < len(left):
        print(f"\t\t\tC: {left[i]}")
        l.append(left[i])
        i += 1

    while j < len(right):
        print(f"\t\t\tD: {right[j]}")
        l.append(right[j])
        j += 1

    print(f"        MERGE RETURNED: {l}")
    return l


def verify_sorted(list_: list):
    print(f"VERIFICATION: {list_}")
    if len(list_) <= 1:
        return True

    return list_[0] <= list_[1] and verify_sorted(list_[1:])


if __name__ == "__main__":
    alist = [5, 8, 5, 3, 2, 5, 8, 7, 1, 2, 3, 45, 6, 7, 784, 8, 65, 5, 456, 475, 2, 5, 674, 999, 4, 2, 5, 100000, 1, 624,
             50, 3, 41, 5, 264, 2, 5000, 153, 6, 47, 500, 2304, 13, 5, 666, 2, 473, 5, 62, 34, 6, 5, 63, 6, 4, 64, 250, 64,
             6, 3, 6, 3, 64, 6, 436, 4, 6, 4, 64, 3, 6, 4, 3, 6, 513, 67, 8, 978, 5, 5, 69, 5, 0, 0, 56, 9]

    sorted_list = merge_sort(alist)

    print(verify_sorted(sorted_list))
