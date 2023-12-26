def small():
    with open('input.txt') as fp:
        grid = [line.strip() for line in fp.readlines()]
        N, M = len(grid), len(grid[0])
        vis = [[False for _ in range(M)] for _ in range(N)]
        for row in range(N):
            for col in range(M):
                if vis[row][col]:
                    continue
                if '0' <= grid[row][col] <= '9' or grid[row][col] == '.':
                    continue

                q = [(row, col)]
                vis[row][col] = True
                for x, y in q:
                    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '.' and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))

        ans = 0
        for row in range(N):
            s = ''
            for col in range(M):
                if '0' <= grid[row][col] <= '9' and vis[row][col]:
                    s += grid[row][col]
                else:
                    if s:
                        ans += int(s)
                    s = '' 
            if s:
                ans += int(s)

        print(ans)

def large():
    with open('input.txt') as fp:
        grid = [line.strip() for line in fp.readlines()]
        N, M = len(grid), len(grid[0])
        vis = [[False for _ in range(M)] for _ in range(N)]
        for row in range(N):
            for col in range(M):
                if vis[row][col]:
                    continue
                if '0' <= grid[row][col] <= '9' or grid[row][col] == '.':
                    continue

                q = [(row, col)]
                vis[row][col] = True
                for x, y in q:
                    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '.' and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))

        numbers = [[None for _ in range(M)] for _ in range(N)]
        ans = 0
        for row in range(N):
            s = ''
            for col in range(M):
                if '0' <= grid[row][col] <= '9' and vis[row][col]:
                    s += grid[row][col]
                else:
                    if s:
                        for j in range(col - len(s), col):
                            numbers[row][j] = (int(s), (row, col))
                    s = '' 
            if s:
                for j in range(M - len(s), M):
                    numbers[row][j] = (int(s), (row, M))

        ans = 0
        for x in range(N):
            for y in range(M):
                if grid[x][y] == '*':
                    p, added = 1, set()
                    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and numbers[nx][ny] is not None:
                            val, key = numbers[nx][ny]
                            if key not in added:
                                added.add(key)
                                p *= val
                    if len(added) == 2:
                        ans += p

        print(ans)

large()


      