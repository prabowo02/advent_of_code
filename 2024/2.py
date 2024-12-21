def main():
    with open('input.txt') as fp:
        ls = [[int(s) for s in line.split()] for line in fp.readlines()]

        def is_safe(ls):
            if all(1 <= ls[i] - ls[i - 1] <= 3 for i in range(1, len(ls))):
                return True
            if all(1 <= ls[i - 1] - ls[i] <= 3 for i in range(1, len(ls))):
                return True
            return False

        def is_safe2(ls):
            if is_safe(ls):
                return True
            return any(is_safe(ls[:i] + ls[i+1:]) for i in range(len(ls)))

        # Part 1
        print(sum([1 for row in ls if is_safe(row)]))

        # Part 2
        print(sum([1 for row in ls if is_safe2(row)]))


if __name__ == '__main__':
    main()
