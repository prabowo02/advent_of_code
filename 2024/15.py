import math
import os

from PIL import Image, ImageDraw

def main():
    with open('input.txt') as fp:
        s, moves = fp.read().split('\n\n')
        s = [list(row.strip()) for row in s.split()]
        moves = ''.join(row.strip() for row in moves.split())

        s2 = [list(''.join([{'@': '@.', '#': '##', 'O': '[]', '.': '..'}[cell]for cell in row])) for row in s]

        def solve(s, moves):
            robot = None
            for i, row in enumerate(s):
                for j, cell in enumerate(row):
                    if cell == '@':
                        robot = (i, j)

            dirs = {
                '^': (-1, 0),
                '<': (0, -1),
                '>': (0, 1),
                'v': (1, 0),
            }
            for move in moves:
                nx, ny = robot
                can = True
                moved = {
                    robot: '@',
                }
                q = [robot]
                for x, y in q:
                    nx, ny = x + dirs[move][0], y + dirs[move][1]
                    if (nx, ny) in moved:
                        continue
                    if s[nx][ny] == '.':
                        continue
                    if s[nx][ny] == '#':
                        can = False
                        break

                    for nnx, nny in {
                        'O': ((nx, ny),),
                        '[': ((nx, ny), (nx, ny + 1)),
                        ']': ((nx, ny - 1), (nx, ny)),
                    }[s[nx][ny]]:
                        q.append((nnx, nny))
                        moved[(nnx, nny)] = s[nnx][nny]

                if not can:
                    continue

                for x, y in moved:
                    s[x][y] = '.'
                for (x, y), m in moved.items():
                    s[x + dirs[move][0]][y + dirs[move][1]] = m
                robot = (robot[0] + dirs[move][0], robot[1] + dirs[move][1])

            return sum(i*100 + j for i, row in enumerate(s) for j, cell in enumerate(row) if cell in 'O[')

        print(solve(s, moves))
        print(solve(s2, moves))


if __name__ == '__main__':
    main()
