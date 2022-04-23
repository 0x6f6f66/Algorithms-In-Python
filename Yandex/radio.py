def build_map(size, company_1, company_2):
    row = int(size.split(" ")[0])
    col = int(size.split(" ")[1])

    print(f'row col {row, col}')
    city_map = [['_' for _ in range(col)] for _ in range(row)]

    for loc in company_1:
        r, c = loc
        city_map[r][c] = '1'

    for loc in company_2:
        r, c = loc
        city_map[r][c] = '2'

    for row in city_map:
        print(row)


if __name__ == '__main__':
    size = input()
    company_1 = []
    for _ in range(8):
        loc = input()
        formatted = loc.split(" ")
        company_1.append((int(formatted[0]), int(formatted[1])))
    company_2 = []
    for _ in range(8):
        loc = input()
        formatted = loc.split(" ")
        company_2.append((int(formatted[0]), int(formatted[1])))
    print(company_1)
    print(company_2)

    print(build_map(size, company_1, company_2))

    """
15 15
-1 0
0 13
-4 3
7 2
0 -10
1 -2
-10 8
-1 9
3 4
-2 -10
-4 7
-4 -8
3 11
-8 6
-6 8
0 7
    """

