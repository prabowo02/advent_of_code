def main():
    with open('input.txt') as fp:
        a = int(fp.readline().split()[-1])
        b = int(fp.readline().split()[-1])
        c = int(fp.readline().split()[-1])
        program = [int(s) for s in fp.read().split()[-1].split(',')]

        def combo(n):
            if n <= 3:
                return n
            if n == 4:
                return a
            if n == 5:
                return b
            if n == 6:
                return c

        ptr = 0

        out = []
        while ptr < len(program):
            op = program[ptr]
            n = program[ptr + 1]

            if op == 0:
                a >>= combo(n)
            elif op == 1:
                b ^= n
            elif op == 2:
                b = combo(n) & 7
            elif op == 3:
                if a != 0:
                    ptr = n - 2
            elif op == 4:
                b ^= c
            elif op == 5:
                out.append(combo(n) & 7)
            elif op == 6:
                b = a >> combo(n)
            elif op == 7:
                c = a >> combo(n)
            else:
                assert False
            ptr += 2

        print(','.join([str(s) for s in out]))

        # b = (a & 7) ^ 3
        # c = a >> b
        # b = b ^ c
        # a = a >> 3
        # b = b ^ 5
        # print(b % 8)

        def dfs(a, program):
            if len(program) == 0:
                return a
            for a8 in range(8):
                b = a8 ^ 3
                c = (a * 8 + a8) >> b
                b ^= c ^ 5
                if b % 8 == program[-1]:
                    if (ans := dfs(a * 8 + a8, program[:-1])) is not None:
                        return ans
            return None

        print(dfs(0, program))


if __name__ == '__main__':
    main()
