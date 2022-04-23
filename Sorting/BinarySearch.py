import time
import numpy as np


# Iterative approach to binary search
def binary_search(list: list, target: int):
    first = 0
    last = len(list) - 1
    while first <= last:

        print(list[first:last+1]) # temp
        print(f"First: {first}")
        print(f"Last: {last}")

        midpoint = (first + last) // 2

        if list[midpoint] == target:
            print(f"[INTERNAL] returned: {midpoint}")
            return midpoint

        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    print(f"[INTERNAL] reached None")
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list.")


"""
Tests below. 
(I was testing how fast the algorithm performs and how fast default array creation is compared to numpy array creation)
"""

size = 10
maxSize = 1000000000
maxSize = 109999999

while size <= maxSize:
    # Numpy
    start = time.time()
    testNumpy = np.arange(0, size, 1)
    time_it_took_to_create1 = time.time() - start

    start = time.time()
    verify(binary_search(testNumpy, 5))
    time_it_took_to_compute1 = time.time() - start

    """
    # inRange
    start = time.time()
    testRange = [i for i in range(0, size)]
    time_it_took_to_create2 = time.time() - start

    start = time.time()
    binary_search(testRange, 0)
    time_it_took_to_compute2 = time.time() - start
    """

    print(f"\nNumpy:\nArray creation time: {time_it_took_to_create1}\nSearch time: {time_it_took_to_compute1}\n\n")
          #f"inRange:\nArray creation time: {time_it_took_to_create2}\nSearch time: {time_it_took_to_compute2}\n"

    size *= 10
