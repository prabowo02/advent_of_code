with open('input.txt') as fp:
    grid = [line.strip() for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    empty = 2  # Part 1
    empty = 10**6  # Part 2

    rowsum = [0 for _ in range(n)]
    for i in range(n):
        rowsum[i] = empty if all(grid[i][j] == '.' for j in range(m)) else 1
        rowsum[i] += rowsum[i - 1]

    colsum = [0 for _ in range(m)]
    for j in range(m):
        colsum[j] = empty if all(grid[i][j] == '.' for i in range(n)) else 1
        colsum[j] += colsum[j - 1]

    rowgalaxies, colgalaxies = [], []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                rowgalaxies.append(i)
                colgalaxies.append(j)

    colgalaxies.sort()

    ans, rowcum, colcum = 0, 0, 0
    for i in range(len(rowgalaxies)):
        R, C = rowsum[rowgalaxies[i]], colsum[colgalaxies[i]]
        ans += R * i - rowcum + C * i - colcum
        rowcum += R
        colcum += C

    print(ans)
