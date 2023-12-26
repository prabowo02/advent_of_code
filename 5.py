with open('input.txt') as fp:
    seeds = [int(s) for s in fp.readline().split(':')[-1].split()]
    fp.readline()

    def get_mappers():
        map_name = fp.readline().strip()
        maps = []
        while True:
            line = fp.readline().strip()
            if not line:
                break
            maps.append([int(s) for s in line.split()])
        return maps

    def intersect_range(a, b, c, d):
        return [max(a, c), max(0, min(a + b, c + d) - max(a, c))]

    def conv(seed, mapper):
        x, l = seed
        ret = []
        all_ranges = [[-1, 0], [10**12, 0]]
        for ranges in mapper:
            ret.append(intersect_range(x, l, ranges[1], ranges[2]))
            ret[-1][0] += ranges[0] - ranges[1]
            all_ranges.append([ranges[1], ranges[2]])
            if ret[-1][1] == 0:
                ret.pop()
        all_ranges.sort()

        for i in range(1, len(all_ranges)):
            st = all_ranges[i - 1][0] + all_ranges[i - 1][1]
            ret.append(intersect_range(x, l, st, all_ranges[i][0] - st))
            if ret[-1][1] == 0:
                ret.pop()

        return ret

    seeds_part2 = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    seeds = [(seed, 1) for seed in seeds]

    seeds = seeds_part2

    for _ in range(7):
        mapper = get_mappers()
        new_seeds = []
        for seed in seeds:
            new_seeds.extend(conv(seed, mapper))
        new_seeds.sort()
        seeds = new_seeds
    
    print(min(seeds)[0])
