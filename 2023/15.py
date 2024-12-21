import collections

with open('input.txt') as fp:
    ss = fp.readline().strip().split(',')

    def h(s):
        res = 0
        for c in s:
            res = (res + ord(c)) * 17 % 256
        return res

    print(sum([h(s) for s in ss]))  # Part 1

    boxes = [collections.OrderedDict() for _ in range(256)]
    for s in ss:
        if '-' in s:
            k, _ = s.split('-')
            try:
                boxes[h(k)].move_to_end(k)
                boxes[h(k)].popitem()
            except KeyError:
                pass
        elif '=' in s:
            k, v = s.split('=')
            boxes[h(k)][k] = int(v)

    print(sum([(i + 1) * (j + 1) * v for i in range(256) for j, (k, v) in enumerate(boxes[i].items())]))
