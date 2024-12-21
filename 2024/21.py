import functools
import itertools


def main():
    numpadLocs = {
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        'A': (3, 2),
    }
    keypadLocs = {
        '<': (1, 0),
        '^': (0, 1),
        '>': (1, 2),
        'v': (1, 1),
        'A': (0, 2),
    }


    def complexity(codes, robots):
        # Starting from `s`, press button `t` using `mid` intermediate robots
        # Assume all intermediate robots start and end at 'A'
        @functools.cache
        def cost(s, t, mid):
            locs = numpadLocs if mid == robots else keypadLocs
            s, t = locs[s], locs[t]

            if mid == 0:
                return abs(s[0] - t[0]) + abs(s[1] - t[1]) + 1
            if s == t:
                return 1

            # By right should use Dijkstra's, but these two cases are sufficient due to the grid shape
            lenX, lenY = abs(s[0] - t[0]), abs(s[1] - t[1])
            alignX, alignY = 'v' if s[0] < t[0] else '^', '>' if s[1] < t[1] else '<'
            seqs = []
            if (s[0], t[1]) in locs.values():
                seqs.append(alignY * lenY + alignX * lenX)
            if (t[0], s[1]) in locs.values():
                seqs.append(alignX * lenX + alignY * lenY)

            assert len(seqs) > 0
            return min(getShortestSeqLen(f'A{seq}A', mid - 1) for seq in seqs)

        def getShortestSeqLen(s, mid):
            return sum(cost(a, b, mid) for a, b in itertools.pairwise(s))

        def getNumericPart(s):
            return int(s.replace('A', ''))

        def complexity(code):
            return getShortestSeqLen('A' + code, robots) * getNumericPart(code)

        return sum(complexity(code) for code in codes)

    with open('input.txt') as fp:
        codes = [line.strip() for line in fp.readlines()]

    print(complexity(codes, 2))
    print(complexity(codes, 25))


if __name__ == '__main__':
    main()
