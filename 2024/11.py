import functools


@functools.cache
def f(n, k):
    if k == 0:
        return 1
    if n == 0:
        return f(1, k - 1)

    s = str(n)
    if len(s) % 2 == 0:
        return f(int(s[:len(s)//2]), k - 1) + f(int(s[len(s)//2:]), k - 1)

    return f(n * 2024, k - 1)


def main():
    with open('input.txt') as fp:
        ls = [int(s) for s in fp.readline().split()]
        print(sum(f(n, 25) for n in ls))
        print(sum(f(n, 75) for n in ls))


if __name__ == '__main__':
    main()
