import math
import os

from PIL import Image, ImageDraw

def main():
    with open('input.txt') as fp:
        robots = []
        for line in fp.readlines():
            p, v = line.strip().split()
            p = [int(s) for s in p.split('=')[-1].split(',')]
            v = [int(s) for s in v.split('=')[-1].split(',')]
            robots.append((p, v))

        def solve(n, m, part2=False):
            assert n % 2 == 1 and m % 2 == 1
            def quadrant(x, y):
                if x == n // 2 or y == m // 2:
                    return None
                return (x < n // 2) * 2 + (y < m // 2)

            quadrants = {}
            for p, v in robots:
                x, y = (p[0] + v[0] * 100) % n, (p[1] + v[1] * 100) % m
                q = quadrant(x, y)
                quadrants[q] = quadrants.get(q, 0) + 1

            def draw(t):
                canvas = [[False for _ in range(m)] for _ in range(n)]
                quadrants = {}
                for p, v in robots:
                    x, y = (p[0] + v[0] * t) % n, (p[1] + v[1] * t) % m
                    q = quadrant(x, y)
                    canvas[x][y] = True
                    quadrants[q] = quadrants.get(q, 0) + 1

                if part2:
                    img = Image.new('1', (n, m))
                    draw = ImageDraw.Draw(img)
                    for i, row in enumerate(canvas):
                        for j, cell in enumerate(row):
                            if cell:
                                draw.point((i, j), fill=1)

                    path = os.path.join('img', f'{t}.png')
                    img.save(path)

                    # Find smallest file size, because of better compression
                    nonlocal ans
                    sz = os.path.getsize(path)
                    if ans is None or sz < ans[1]:
                        ans = (t, sz)


                return math.prod(quadrants.get(q, 0) for q in range(4))

            if part2:
                ans = None
                for t in range(10000):
                    draw(t)
                print(ans[0])

            return draw(100)

        # print(solve(11, 7)) # Sample
        print(solve(101, 103, part2=True))

        


if __name__ == '__main__':
    main()
