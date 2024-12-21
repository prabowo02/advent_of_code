import functools


def main():
    with open('input.txt') as fp:
        patterns = fp.readline().strip().split(', ')

        @functools.cache
        def f(s):
            if len(s) == 0:
                return 1
            return sum(f(s[len(pattern):]) for pattern in patterns if s.startswith(pattern))

        towels = [line.strip() for line in fp.read().split()]

        print(sum(1 for towel in towels if f(towel) > 0))
        print(sum(f(towel) for towel in towels))


if __name__ == '__main__':
    main()
