with open('input.txt') as fp:
    ans = 0
    for grid in fp.read().split('\n\n'):
        grid = grid.split()
        gridt = [''.join([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]

        def get_mirrors(grid):
            mirrors = {(i, 0) for i in range(1, len(grid[0]))}
            for row in grid:
                nmirrors = set()
                for mirror, err in mirrors:
                    l, r = row[:mirror][::-1], row[mirror:]
                    error = 0

                    for i in range(min(len(l), len(r))):
                        if l[i] != r[i]:
                            error += 1

                    if err + error <= 1:
                        nmirrors.add((mirror, err + error))

                mirrors = nmirrors
            return mirrors

        desired_error = 1  # Part 2
        # desired_error = 0  # Part 1
        ans += sum([mirror for mirror, err in get_mirrors(grid) if err == desired_error]) + \
               sum([mirror for mirror, err in get_mirrors(gridt) if err == desired_error]) * 100

    print(ans)
