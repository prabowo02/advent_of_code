def main():
    with open('input.txt') as fp:
        s = [int(d) for d in fp.readline().strip()]

        def expand(s):
            ls = []
            for i, d in enumerate(s):
                if i % 2 == 0:
                    ls.extend([i//2] * d)
                else:
                    ls.extend([None] * d)
            return ls

        ls, l = expand(s), 0
        while True:
            while ls[-1] is None:
                ls.pop()
            while l < len(ls) and ls[l] is not None:
                l += 1
            if l == len(ls):
                break
            ls[l] = ls[-1]
            ls.pop()

        print(sum(i * num for i, num in enumerate(ls)))

        ls = [[(None, d)] if i % 2 == 1 else [(i//2, d)] for i, d in enumerate(s)]
        for i in range(len(ls) - 1, -1, -2):
            for j in range(1, len(ls), 2):
                if j > i:
                    break
                if ls[j][-1][1] >= ls[i][-1][1]:
                    _, d = ls[j].pop()
                    ls[j].extend([ls[i][-1], (None, d - ls[i][-1][1])])
                    ls[i] = [(None, ls[i][-1][1])]
                    break

        idx, ans = 0, 0
        for items in ls:
            for i, cnt in items:
                for j in range(cnt):
                    if i is not None:
                        ans += idx * i
                    idx += 1
        print(ans)



if __name__ == '__main__':
    main()
