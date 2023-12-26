with open('input.txt') as fp:
    times = [int(s) for s in fp.readline().split(':')[1].split()]
    dists = [int(s) for s in fp.readline().split(':')[1].split()]

    # Part 2
    times = [int(''.join([str(s) for s in times]))]
    dists = [int(''.join([str(s) for s in dists]))]


    ans = 1
    for t, d in zip(times, dists):
        l, r, ways = 0, t // 2, None
        while l <= r:
            mid = (l + r) // 2
            if mid * (t - mid) > d:
                ways, r = mid, mid - 1
            else:
                l = mid + 1
        ways = t // 2 - ways + 1
        if t % 2 == 0:
            ways = ways * 2 - 1
        else:
            ways = ways * 2
        ans *= ways
    print(ans)
