with open('input.txt') as fp:
    grid = [list(line.strip()) for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    def fall(grid):
        n, m = len(grid), len(grid[0])
        for j in range(m):
            empty = 0
            for i in range(n):
                if grid[i][j] == 'O':
                    grid[i][j] = '.'
                    grid[empty][j] = 'O'
                    empty += 1
                elif grid[i][j] == '#':
                    empty = i + 1

    def rotate(grid):
        n, m = len(grid), len(grid[0])
        res = [[grid[i][j] for i in range(n - 1, -1, -1)] for j in range(m)]
        grid.clear()
        grid.extend(res)

    def cycle(grid):
        for _ in range(4):
            fall(grid)
            rotate(grid)

    def hare_tortoise(grid):
        grid1 = [[grid[i][j] for j in range(m)] for i in range(n)]
        grid2 = [[grid[i][j] for j in range(m)] for i in range(n)]
        cnt = 0
        while True:
            cycle(grid1)
            cycle(grid2)
            cycle(grid2)
            cnt += 1

            if all(grid1[i][j] == grid2[i][j] for i in range(n) for j in range(m)):
                break
        return cnt

    def ncycle(n, grid):
        l = hare_tortoise(grid)
        if n < l:
            for _ in range(n):
                cycle(grid)
            return

        for _ in range(l):
            cycle(grid)
        n -= l
        n %= l
        for _ in range(n):
            cycle(grid)

    # fall(grid)  # Part 1
    ncycle(1000000000, grid)  # Part 2


    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                ans += n - i

    print(ans)
