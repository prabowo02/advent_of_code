import itertools


def main():
    with open('input.txt') as fp:
        ans, ans2 = 0, 0
        for line in fp.readlines():
            res, nums = line.split(': ')
            res, nums = int(res), [int(s) for s in nums.split()]

            def results(nums, Ops):
                ret = set()
                for ops in itertools.product(Ops, repeat=len(nums)-1):
                    result = nums[0]
                    for i, op in enumerate(ops):
                        if op == '+':
                            result += nums[i + 1]
                        elif op == '*':
                            result *= nums[i + 1]
                        elif op == '|':
                            result = int(str(result) + str(nums[i + 1]))
                    ret.add(result)
                return ret

            if res in results(nums, '+*'):
                ans += res
            if res in results(nums, '+*|'):
                ans2 += res

        print(ans)
        print(ans2)


if __name__ == '__main__':
    main()
