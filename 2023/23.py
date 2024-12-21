with open('input.txt') as fp:
    grid = [line.strip() for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    dsu = [[(i, j) for j in range(m)] for i in range(n)]
    sz = [[1 for j in range(m)] for i in range(n)]
    def root(x, y):
        a, b = x, y
        while dsu[x][y] != (x, y):
            x, y = dsu[x][y]
        while (a, b) != (x, y):
            (a, b), dsu[a][b] = dsu[a][b], (x, y)
        return x, y

    def join(x, y, a, b):
        (x, y), (a, b) = root(x, y), root(a, b)
        if (x, y) == (a, b):
            return

        sz[x][y] += sz[a][b]
        dsu[a][b] = (x, y)

    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    for x in range(n):
        for y in range(m):
            if grid[x][y] != '.':
                continue
            pending = []
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if grid[nx][ny] != '.':
                    continue
                join(x, y, nx, ny)

    nodes = [(x, y) for x in range(n) for y in range(m) if grid[x][y] == '.' and root(x, y) == (x, y)]
    adj = { node: set() for node in nodes }
    radj = { node: set() for node in nodes }
    weights = { node: {} for node in nodes }

    def add_edge(u, v):
        adj[u].add(v)
        radj[v].add(u)

    for x in range(n):
        for y in range(m):
            if grid[x][y] == '>':
                add_edge(root(x, y - 1), root(x, y + 1))
                weights[root(x, y - 1)][root(x, y + 1)] = 1
            if grid[x][y] == 'v':
                add_edge(root(x - 1, y), root(x + 1, y))
                weights[root(x - 1, y)][root(x + 1, y)] = 1

    def part1():
        def rtopo(x, y):
            deg = {node: len(adj[node]) for node in nodes}
            q = [(x, y)]

            for u in q:
                for v in radj[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
            return q

        longest = {}
        for u in rtopo(*root(n - 1, m - 2)):
            longest[u] = 0
            for v in adj[u]:
                longest[u] = max(longest[u], longest[v] + weights[u].get(v, 0))
            longest[u] += sz[u[0]][u[1]]

        return longest[root(0, 1)] - 1

    def part2():
        global nodes
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '>':
                    add_edge(root(x, y + 1), root(x, y - 1))
                    weights[root(x, y + 1)][root(x, y - 1)] = 1
                if grid[x][y] == 'v':
                    add_edge(root(x + 1, y), root(x - 1, y))
                    weights[root(x + 1, y)][root(x - 1, y)] = 1

        # Compress
        for node in nodes:
            if node == root(0, 1) or node == root(n - 1, m - 2):
                continue
            if len(adj[node]) == 2:
                u, v = adj[node].pop(), adj[node].pop()
                adj[u].remove(node)
                adj[v].remove(node)
                add_edge(u, v)
                add_edge(v, u)
                weights[u][v] = weights[node].get(u, 0) + weights[node].get(v, 0) + sz[node[0]][node[1]]
                weights[v][u] = weights[u][v]
                del adj[node]
                del weights[node]
        nodes = [node for node in adj]

        def dfs(u, t, adj):
            ret, vis = 0, {u}
            def _dfs(u, dist):
                nonlocal ret
                dist += sz[u[0]][u[1]]
                if u == t:
                    ret = max(ret, dist)
                    return
                for v in adj[u]:
                    if v in vis:
                        continue
                    vis.add(v)
                    _dfs(v, dist + weights[u].get(v, 0))
                    vis.remove(v)
            _dfs(u, 0)
            return ret - 1

        return dfs(root(0, 1), root(n - 1, m - 2), adj)

    print(part1())
    print(part2())
