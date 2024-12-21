with open('input.txt') as fp:
    ans = 0
    for line in fp.readlines():
        seq = [int(s) for s in line.split()]

        vals = [seq]
        while any(val != 0 for val in vals[-1]):
            diff = [vals[-1][i] - vals[-1][i - 1] for i in range(1, len(vals[-1]))]
            vals.append(diff)

        # Part 1
        # vals[-1].append(0)
        # for i in range(len(vals) - 2, -1, -1):
        #     vals[i].append(vals[i][-1] + vals[i + 1][-1])
        # ans += vals[0][-1]

        vals[-1] = [0] + vals[-1]
        for i in range(len(vals) - 2, -1, -1):
            vals[i] = [vals[i][0] - vals[i + 1][0]] + vals[i]
        ans += vals[0][0]

    print(ans)
