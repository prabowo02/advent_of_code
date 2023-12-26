import collections

with open('input.txt') as fp:
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    grid = [line.strip() for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    def bfs(x, y, d):
        q = [(x, y, d)]
        vis = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
        vis[x][y][d] = True

        def try_push(x, y, d):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny][d]:
                vis[nx][ny][d] = True
                q.append((nx, ny, d))

        for x, y, d in q:
            if grid[x][y] == '.' or (grid[x][y] == '-' and d in (0, 2)) or (grid[x][y] == '|' and d in (1, 3)):
                # Go straight
                try_push(x, y, d)
            elif grid[x][y] == '/':
                try_push(x, y, d ^ 1)
            elif grid[x][y] == '\\':
                try_push(x, y, d ^ 3)
            elif grid[x][y] == '-' and d in (1, 3):
                try_push(x, y, 0)
                try_push(x, y, 2)
            elif grid[x][y] == '|' and d in (0, 2):
                try_push(x, y, 1)
                try_push(x, y, 3)
            else:
                assert False

        return sum([1 for x in range(n) for y in range(m) if any(vis[x][y])])

    print(bfs(0, 0, 0))  # Part 1
    print(max(max(max(bfs(0, y, 3), bfs(n - 1, y, 1)) for y in range(m)), max(max(bfs(x, 0, 0), bfs(x, m - 1, 2)) for x in range(n))))  # Part 2
