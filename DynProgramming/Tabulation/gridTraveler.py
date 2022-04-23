def gridTraveler(m, n):
    grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    grid[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if j + 1 <= n:
                grid[i][j + 1] += grid[i][j]
            if i + 1 <= m:
                grid[i + 1][j] += grid[i][j]

    return grid[m][n]


if __name__ == '__main__':
    print(gridTraveler(1, 1))
    print(gridTraveler(2, 3))
    print(gridTraveler(3, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(18, 18))
