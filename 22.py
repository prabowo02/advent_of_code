with open('input.txt') as fp:
    bricks = []
    grid = [[[None if z > 0 else -1 for z in range(1000)] for _ in range(10)] for _ in range(10)]
    for i, line in enumerate(fp.readlines()):
        brick = line.strip().split('~')
        brick = [int(s) for s in brick[0].split(',') + brick[1].split(',')]
        bricks.append(brick)

        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                for z in range(brick[2], brick[5] + 1):
                    grid[x][y][z] = i

    falling = True
    while falling:
        falling = False

        for brick in bricks:
            if brick[2] == 1:
                continue
            if not all(grid[x][y][brick[2] - 1] is None for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1)):
                continue

            falling = True
            for x in range(brick[0], brick[3] + 1):
                for y in range(brick[1], brick[4] + 1):
                    grid[x][y][brick[2] - 1] = grid[x][y][brick[2]]
                    grid[x][y][brick[5]] = None
            brick[2] -= 1
            brick[5] -= 1

    adj = {u: set() for u in range(len(bricks))}
    for z in range(1, 999):
        for x in range(10):
            for y in range(10):
                if grid[x][y][z] is not None and grid[x][y][z + 1] is not None and grid[x][y][z] != grid[x][y][z + 1]:
                    adj[grid[x][y][z]].add(grid[x][y][z + 1])

    deg = [0 for _ in bricks]
    for u in adj:
        for v in adj[u]:
            deg[v] += 1

    ans = 0
    for u in range(len(bricks)):
        if all(deg[v] > 1 for v in adj[u]):
            ans += 1
    print(ans)  # Part 1

    def topo(q):
        degcopy = deg[:]
        for u in q:
            for v in adj[u]:
                degcopy[v] -= 1
                if degcopy[v] == 0:
                    q.append(v)
        return q

    ans = 0
    subs = [{i} for i in range(len(bricks))]
    for u in topo([i for i in range(len(bricks)) if deg[i] == 0])[::-1]:
        falls = []
        for v in adj[u]:
            subs[u] |= subs[v]
            if deg[v] == 1:
                falls.append(v)
        ans += len(topo(falls))
    print(ans)
