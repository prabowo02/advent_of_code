with open('input.txt') as fp:
    grid = [line.strip() for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    connects = {
        '|': {1, 3},
        '-': {0, 2},
        'L': {0, 1},
        'J': {1, 2},
        '7': {2, 3},
        'F': {0, 3},
        '.': set(),
        'S': {0, 1, 2, 3},
    }

    print(n, m)

    par = [[(i, j) for j in range(m)] for i in range(n)]
    sizes = [[1 for j in range(m)] for i in range(n)]
    def root(x, y):
        a, b = x, y
        while par[x][y] != (x, y):
            x, y = par[x][y]
        while (a, b) != (x, y):
            (a, b), par[a][b] = par[a][b], (x, y)
        return x, y

    def has_edge(x, y, d):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and d in connects[grid[x][y]] and (d + 2) % 4 in connects[grid[nx][ny]]:
            return True
        return False

    s = None
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 'S':
                s = x, y
            for d in range(4):
                if not has_edge(x, y, d):
                    continue
                p, q = root(x, y), root(x + dx[d], y + dy[d])
                if p == q:
                    continue
                sizes[p[0]][p[1]] += sizes[q[0]][q[1]]
                par[q[0]][q[1]] = p

    s = root(*s)
    print(sizes[s[0]][s[1]] // 2)  # Part 1

    ans = 0
    vis = [[False for y in range(m)] for x in range(n)]
    for x in range(n):
        for y in range(m):
            if vis[x][y] or root(x, y) == s:
                continue
            def flood(x, y):
                q = [(x, y)]
                vis[x][y] = True
                area = 0
                for x, y in q:
                    area += 1
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and root(nx, ny) != s and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                return area
            def is_inside(x, y):
                inside = False
                for j in range(y + 1, m):
                    if root(x, j) == s and grid[x][j] in '|LJ':
                        inside = not inside
                return inside

            area = flood(x, y)
            if is_inside(x, y):
                ans += area

    print(ans)
