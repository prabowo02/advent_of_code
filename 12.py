import functools

with open('input.txt') as fp:
    ans = 0
    for line in fp.readlines():
        row, group = line.split()
        group = [int(s) for s in group.split(',')]

        row, group = (row + '?') * 4 + row, group * 5  # Part 2

        @functools.cache
        def dp(n, m, c):
            if m < len(group) and group[m] == c:
                if n >= len(row) or row[n] != '#':
                    return dp(n + 1, m + 1, 0)
                return 0

            if n >= len(row):
                return 1 if m == len(group) else 0

            res = 0
            if row[n] != '.' and m < len(group):
                res += dp(n + 1, m, c + 1)
            if c == 0 and row[n] != '#':
                res += dp(n + 1, m, c)
            return res

        ans += dp(0, 0, 0)

    print(ans)
