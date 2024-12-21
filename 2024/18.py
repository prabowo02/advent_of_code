import heapq


def main():
    with open('input.txt') as fp:
        blocks = [[int(s) for s in line.split(',')] for line in fp.readlines()]

        def shortest(n, m):
            grid = [[None for _ in range(n)] for _ in range(n)]
            for i in range(m):
                grid[blocks[i][0]][blocks[i][1]] = True

            # print('\n'.join([''.join(['#' if grid[i][j] else '.' for j in range(n)]) for i in range(n)]))

            grid[0][0] = 0
            q = [(0, 0)]
            for x, y in q:
                for nx, ny in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if grid[nx][ny] is not None:
                        continue
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
            return grid[-1][-1]

        def blocked(n):
            l, r, ret = 0, len(blocks), None
            while l + 1 <= r:
                mid = (l + r) // 2
                if shortest(n, mid) is None:
                    ret, r = mid, mid
                else:
                    l= mid + 1
            return f'{blocks[ret - 1][0]},{blocks[ret - 1][1]}'


        # Sample
        # print(shortest(7, 12))
        # print(blocked(7))

        print(shortest(71, 1024))
        print(blocked(71))



if __name__ == '__main__':
    main()
