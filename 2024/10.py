import functools


def main():
    with open('input.txt') as fp:
        s = [[int(d) for d in row.strip()] for row in fp.readlines()]

        def inside(x, y):
            return 0 <= x < len(s) and 0 <= y < len(s[x])

        @functools.cache
        def f(x, y):
            if s[x][y] == 9:
                return {(x, y)}

            ret = set()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                if not inside(nx, ny):
                    continue
                if s[nx][ny] != s[x][y] + 1:
                    continue
                ret = ret.union(f(nx, ny))
            return ret

        @functools.cache
        def g(x, y):
            if s[x][y] == 9:
                return 1

            ret = 0
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                if not inside(nx, ny):
                    continue
                if s[nx][ny] != s[x][y] + 1:
                    continue
                ret += g(nx, ny)
            return ret



        ans, ans2 = 0, 0
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == 0:
                    ans += len(f(i, j))
                    ans2 += g(i, j)
        print(ans)
        print(ans2)




if __name__ == '__main__':
    main()
