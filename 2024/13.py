import functools
import re


def main():
    with open('input.txt') as fp:
        ans, ans2 = 0, 0
        for block in fp.read().split('\n\n'):
            a, b, c = block.split('\n')

            a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', a)
            b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', b)
            c = re.match(r'Prize: X=(\d+), Y=(\d+)', c)

            a = int(a.group(1)), int(a.group(2))
            b = int(b.group(1)), int(b.group(2))
            c = int(c.group(1)), int(c.group(2))

            # All cases are linearly independent
            def solve(a, b, c):
                i = divmod(c[0] * b[1] - c[1] * b[0], a[0] * b[1] - a[1] * b[0])
                j = divmod(c[0] * a[1] - c[1] * a[0], a[1] * b[0] - a[0] * b[1])
                if i[1] == 0 and j[1] == 0:
                    return 3 * i[0] + j[0]
                return 0

            ans += solve(a, b, c)
            ans2 += solve(a, b, (c[0] + 10000000000000, c[1] + 10000000000000))

        print(ans)
        print(ans2)

if __name__ == '__main__':
    main()
