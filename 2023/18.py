with open('input.txt') as fp:
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

    instr = []
    x, y = 0, 0
    xs, ys = [0], [0]
    for line in fp.readlines():
        d, s, c = line.strip().split()
        d, s = {
            'R': 0,
            'U': 1,
            'L': 2,
            'D': 3,
        }[d], int(s)

        s, d = int(c[2:-2], 16), -int(c[-2]) % 4  # Part 2

        instr.append((d, int(s)))
        x, y = x + dx[d] * s, y + dy[d] * s
        xs.append(x)
        ys.append(y)

    xs, ys = [min(xs) - 5] + sorted(set(xs)) + [max(xs) + 5], [min(ys) - 5] + sorted(set(ys)) + [max(ys) + 5]

    wx, wy = [], []
    for i in range(1, len(xs)):
        wx.append(xs[i] - xs[i - 1] - 1)
        wx.append(1)
    for i in range(1, len(ys)):
        wy.append(ys[i] - ys[i - 1] - 1)
        wy.append(1)

    n, m = len(wx), len(wy)
    grid = [[False for _ in range(m)] for _ in range(n)]

    x, y = xs.index(0) * 2 - 1, ys.index(0) * 2 - 1
    grid[x][y] = True
    for d, s in instr:
        while s > 0:
            x, y = x + dx[d], y + dy[d]
            s -= wx[x] if d in (1, 3) else wy[y]
            grid[x][y] = True

    def bfs(x, y):
        if grid[x][y]:
            return 0

        q = [(x, y)]
        grid[x][y] = True

        def try_push(x, y, d):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                return
            if grid[nx][ny]:
                return
            grid[nx][ny] = True
            q.append((nx, ny))

        for x, y in q:
            for i in range(4):
                try_push(x, y, i)

        return sum([wx[x] * wy[y] for x, y in q])

    print(sum(wx) * sum(wy) - bfs(0, 0))
