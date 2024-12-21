
def main():
    with open('input.txt') as fp:
        s = [list(line.strip()) for line in fp.readlines()]
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        init_guard = None
        for i, row in enumerate(s):
            for j, col in enumerate(row):
                if col == '^':
                    init_guard = (i, j)
                    break


        def is_inside(guard):
            if not (0 <= guard[0] < len(s)):
                return False
            if not (0 <= guard[1] < len(s[guard[0]])):
                return False
            return True

        def steps_until_out():
            curStep = 0
            guard = init_guard
            pos = set()
            vis = set()
            while True:
                pos.add(guard)
                if (guard, curStep) in vis:
                    return None
                vis.add((guard, curStep))
                nguard = (guard[0] + steps[curStep][0], guard[1] + steps[curStep][1])
                if not is_inside(nguard):
                    break
                if s[nguard[0]][nguard[1]] == '#':
                    curStep = (curStep + 1) % len(steps)
                else:
                    guard = nguard

            return len(pos)

        # Part 1
        print(steps_until_out())

        # Part 2
        ans = 0
        for i, row in enumerate(s):
            for j, col in enumerate(row):
                if col == '.':
                    s[i][j] = '#'
                    if steps_until_out() is None:
                        ans += 1
                    s[i][j] = '.'
        print(ans)



if __name__ == '__main__':
    main()
