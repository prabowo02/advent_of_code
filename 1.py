with open('input.txt') as fp:
    ans = 0
    ls = [(str(i), i) for i in range(1, 10)]

    # Comment the following line for solving part 1
    ls += [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

    for line in fp.readlines():
        i = 0
        firstdig, lastdig = None, None
        while i < len(line):
            found = False
            for s, dig in ls:
                if line[i:i+len(s)] == s:
                    firstdig = dig
                    break
            if firstdig is not None:
                break
            i += 1
        i = len(line)
        while i > 0:
            found = False
            for s, dig in ls:
                if line[i-len(s):i] == s:
                    lastdig = dig
                    break
            if lastdig is not None:
                break
            i -= 1

        print(firstdig, lastdig)
        ans += firstdig * 10 + lastdig

    print(ans)
