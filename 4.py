with open('input.txt') as fp:
    ans, total = 0, 0
    copies = [1 for _ in range(1000)]
    for i, line in enumerate(fp.readlines()):
        numbers = line.split(':')[-1]
        cards, yours = numbers.split('|')
        cards = set([int(c) for c in cards.split()])
        yours = [int(y) for y in yours.split()]

        match = 0
        for your in yours:
            if your in cards:
                match += 1
        if match > 0:
            ans += 2**(match - 1)

        for j in range(i, i + match):
            copies[j + 1] += copies[i]

        total += copies[i]

    print(ans)
    print(total)
