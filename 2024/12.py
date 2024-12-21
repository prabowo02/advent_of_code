import functools


def main():
    with open('input.txt') as fp:
        s = [line.strip() for line in fp.readlines()]

        def inside(x, y):
            return 0 <= x < len(s) and 0 <= y < len(s[x])

        def neighs(x, y):
            return (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)

        ans, ans2 = 0, 0
        vis = set()
        for i, row in enumerate(s):
            for j, col in enumerate(row):
                x, y = i, j
                if (x, y) in vis:
                    continue
                q = [(x, y)]
                vis.add((x, y))
                for x, y in q:
                    for nx, ny in neighs(x, y):
                        if not inside(nx, ny):
                            continue
                        if (nx, ny) in vis:
                            continue
                        if s[nx][ny] != s[x][y]:
                            continue
                        vis.add((nx, ny))
                        q.append((nx, ny))

                q = set(q)
                peri = 0
                for x, y in q:
                    for nx, ny in neighs(x, y):
                        if (nx, ny) not in q:
                            peri += 1

                peri2 = 0
                for x, y in q:
                    if (x, y - 1) not in q and not((x - 1, y) in q and (x - 1, y - 1) not in q):
                        peri2 += 1
                    if (x, y + 1) not in q and not((x - 1, y) in q and (x - 1, y + 1) not in q):
                        peri2 += 1
                    if (x - 1, y) not in q and not((x, y - 1) in q and (x - 1, y - 1) not in q):
                        peri2 += 1
                    if (x + 1, y) not in q and not((x, y - 1) in q and (x + 1, y - 1) not in q):
                        peri2 += 1

                ans2 += len(q) * peri2
                ans += len(q) * peri

        print(ans)
        print(ans2)

if __name__ == '__main__':
    main()
