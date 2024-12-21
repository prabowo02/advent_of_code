import functools


def main():
    with open('input.txt') as fp:
        grid = [line.strip() for line in fp.readlines()]
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 'S':
                    s = (i, j)
                if cell == 'E':
                    e = (i, j)


        def bfs(s):
            q = [s]
            dist = {s: 0}
            for x, y in q:
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                    if grid[nx][ny] == '#' or (nx, ny) in dist:
                        continue
                    dist[(nx, ny)] = dist[(x, y)] + 1
                    q.append((nx, ny))
            return dist

        def neighs(x, y, d):
            for i in range(1, d + 1):
                for j in range(i):
                    yield (x + i - j, y + j)
                    yield (x - j, y + i - j)
                    yield (x - i + j, y - j)
                    yield (x + j, y - i + j)

        distS, distE = bfs(s), bfs(e)

        def countCheats(save, t):
            ans = 0
            noCheatDist = distS[e]
            for i in range(1, len(grid) - 1):
                for j in range(1, len(grid[i]) - 1):
                    if (i, j) not in distS:
                        continue
                    for ni, nj in neighs(i, j, t):
                        if (ni, nj) not in distE:
                            continue
                        if distE[(ni, nj)] + distS[(i, j)] + abs(i - ni) + abs(j - nj) <= noCheatDist - save:
                            ans += 1
            return ans

        print(countCheats(100, 2))
        print(countCheats(100, 20))


if __name__ == '__main__':
    main()
