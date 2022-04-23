# Doesn't work, as i didnt solve this

def solution(arr, k, s):
    num = s
    streak = 0
    count = 0
    start = 0
    i = 0

    while i < len(arr):
        num = num - arr[i]
        if num == 0:
            num = s
            streak = 0
            count += 1 # the only difference between two blocks of code
            start += 1
            i = start
        elif num < 0 or streak > k:
            num = s
            streak = 0
            start += 1
            i = start
        else:
            i += 1
            streak += 1

    return count


if __name__ == '__main__':
    """
    arr = [1, 2, 4, -1, 7, 6, 1,]
    k = 3
    s = 6
    """
    arr = [1, 0]
    k = 2
    s = 1

    print(solution(arr, k, s))
