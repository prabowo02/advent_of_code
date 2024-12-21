import collections

def main():
    with open('input.txt') as fp:
        a, b = zip(*[[int(s) for s in line.split()] for line in fp.readlines()])

        # Part 1
        ans = 0
        for x, y in zip(sorted(a), sorted(b)):
            ans += abs(x - y)
        print(ans)
        
        
        # Part 2
        ans = 0
        a, b = collections.Counter(a), collections.Counter(b)
        for k in a:
            ans += k * a[k] * b[k]
        print(ans)


if __name__ == '__main__':
    main()
