with open('input.txt') as fp:
    grid = [line.strip() for line in fp.readlines()]
    n = len(grid)

    dx, dy = [0, -1, 0, 1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, -1, 1]

    def get_dist(x, y):
        dist = [[None for _ in range(n)] for _ in range(n)]
        dist[x][y] = 0
        q = [(x, y)]
        for x, y in q:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#' and dist[nx][ny] is None:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        return dist

    def arith(start, step, n):
        # start + (start + step) + ... + (start + step * (n - 1))
        return (start + start + step * (n - 1)) * n // 2

    sdist = get_dist(n//2, n//2)

    L = 26501365

    # L = 64  # Part 1
    ans = sum([1 for i in range(n) for j in range(n) if sdist[i][j] is not None and sdist[i][j] <= L and (L - sdist[i][j]) % 2 == 0])
    print(ans)

    for d in range(8):
        x, y = n//2 + n//2 * dx[d], n//2 + n//2 * dy[d]
        dist = get_dist((x + dx[d]) % n, (y + dy[d]) % n)

        for i in range(n):
            for j in range(n):
                if sdist[i][j] is None:
                    continue
                base_dist = sdist[x][y] + abs(dx[d]) + abs(dy[d]) + dist[i][j]

                if abs(dx[d] + dy[d]) == 1:
                    if n % 2 == 1:
                        ans += len(range(base_dist + (L - base_dist) % 2 * n, L + 1, n * 2))
                    elif (L - base_dist) % 2 == 0:
                        ans += len(range(base_dist, L + 1, n))
                else:
                    if n % 2 == 1:
                        if (L - base_dist) % 2 == 1:
                            ans += arith(2, 2, len(range(base_dist + n, L + 1, n * 2)))
                        else:
                            ans += arith(1, 2, len(range(base_dist, L + 1, n * 2)))
                    elif (L - base_dist) % 2 == 0:
                        ans += arith(1, 1, len(range(base_dist, L + 1, n)))

    print(ans)
