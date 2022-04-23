def rotate(A, K):
    return [*arr[-K:], *arr[0:-K]]


if __name__ == '__main__':
    arr = [3, 8, 9, 7, 6]
    for i in range(len(arr)):
        print(rotate(arr, i))
