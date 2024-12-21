import heapq


def main():
    with open('input.txt') as fp:
        S = [line.strip() for line in fp.readlines()]
        
        for i, row in enumerate(S):
            for j, cell in enumerate(row):
                if cell == 'S':
                    s = (i, j)
                if cell == 'E':
                    e = (i, j)

        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        vis = {
            (s, 0): 0,
        }
        paths = {
            (s, 0): {s},
        }

        q = [(0, s, 0)]
        while q:
            dist, (x, y), d = heapq.heappop(q)
            if dist > vis[((x, y), d)]:
                continue

            if e == (x, y):
                print(dist)
                print(len(paths[((x, y), d)]))
                break

            for nx, ny, nd, ndist in [
                (x + dirs[d][0], y + dirs[d][1], d, dist + 1),
                (x, y, (d + 1) % 4, dist + 1000),
                (x, y, (d - 1) % 4, dist + 1000)]:

                nstate = ((nx, ny), nd)

                if S[nx][ny] == '#':
                    continue
                if vis.get(nstate, 10**9) <= ndist:
                    if vis[nstate] == ndist:
                        paths[nstate] = paths[nstate].union(paths[((x, y), d)])
                    continue
                vis[nstate] = ndist
                paths[nstate] = paths[((x, y), d)].union({(nx, ny)})
                heapq.heappush(q, (ndist, (nx, ny), nd))



if __name__ == '__main__':
    main()
