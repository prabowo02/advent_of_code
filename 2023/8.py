import math

with open('input.txt') as fp:
    lr = fp.readline().strip()
    fp.readline()

    instr = dict()
    for line in fp.readlines():
        src, dst = line.strip().split(' = ')
        instr[src] = dict()
        instr[src]['L'], instr[src]['R'] = dst[1:-1].split(', ')

    src, dst = [], []
    for node in instr:
        if node.endswith('A'):
            src.append(node)
        elif node.endswith('Z'):
            dst.append(node)

    # src, dst = ['AAA'], ['ZZZ']  # Part 1

    steps = []
    for node in src:
        cur, step = node, 0
        while cur not in dst:
            cur = instr[cur][lr[step % len(lr)]]
            step += 1
        steps.append(step)
    print(math.lcm(*steps))
