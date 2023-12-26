import heapq

with open('input.txt') as fp:
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
    grid = [[int(s) for s in line.strip()] for line in fp.readlines()]
    n, m = len(grid), len(grid[0])

    min_consecutive, max_consecutive = 1, 3  # Part 1
    min_consecutive, max_consecutive = 4, 10  # Part 2

    def bfs(x, y, d, c):
        q = [(0, x, y, d, c)]
        vis = { (x, y, d, c): 0 }

        def try_push(dist, x, y, d, c):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                return
            ndist = dist + grid[nx][ny]
            if ndist < vis.get((nx, ny, d, c), 10**9):
                vis[(nx, ny, d, c)] = ndist
                heapq.heappush(q, (ndist, nx, ny, d, c))

        while q:
            dist, x, y, d, c = heapq.heappop(q)
            if (x, y) == (n - 1, m - 1) and max_consecutive - c >= min_consecutive:
                return dist
            if vis.get((x, y, d, c)) != dist:
                continue
            if c > 0:
                try_push(dist, x, y, d, c - 1)
            if max_consecutive - c >= min_consecutive:
                try_push(dist, x, y, (d + 1) % 4, max_consecutive - 1)
                try_push(dist, x, y, (d - 1) % 4, max_consecutive - 1)

        return None

    print(min(bfs(0, 0, 0, max_consecutive), bfs(0, 0, 3, max_consecutive)))
