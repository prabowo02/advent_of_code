import copy
import math

with open('input.txt') as fp:
    flows, parts = fp.read().split('\n\n')

    def parse_flow(flow):
        name, rules = flow.split('{')
        rules = rules[:-1].split(',')

        def func(xmas):
            for rule in rules:
                if ':' in rule:
                    cond, res = rule.split(':')
                    if '<' in cond:
                        l, r = cond.split('<')
                        if xmas[l] < int(r):
                            return res
                    elif '>' in cond:
                        l, r = cond.split('>')
                        if xmas[l] > int(r):
                            return res
                else:
                    return rule

        return name, func

    nodes = {'A': [], 'R': []}
    def parse_flow2(flow):
        name, rules = flow.split('{')
        rules = rules[:-1].split(',')

        def func(xmas):
            for rule in rules:
                if ':' in rule:
                    cond, res = rule.split(':')
                    if '<' in cond:
                        l, r = cond.split('<')
                        if xmas[l][0] < int(r):
                            nxmas = copy.deepcopy(xmas)
                            nxmas[l][1] = min(nxmas[l][1], int(r) - 1)
                            nodes[res].append(nxmas)
                        if xmas[l][1] >= int(r):
                            xmas[l][0] = max(xmas[l][0], int(r))
                        else:
                            break
                    elif '>' in cond:
                        l, r = cond.split('>')
                        if xmas[l][1] > int(r):
                            nxmas = copy.deepcopy(xmas)
                            nxmas[l][0] = max(nxmas[l][0], int(r) + 1)
                            nodes[res].append(nxmas)
                        if xmas[l][0] <= int(r):
                            xmas[l][1] = min(xmas[l][1], int(r))
                        else:
                            break
                else:
                    nodes[rule].append(copy.deepcopy(xmas))

        return name, func

    funcs = {}
    funcs2 = {}
    for flow in flows.split():
        k, v = parse_flow(flow.strip())
        funcs[k] = v
        k2, v2 = parse_flow2(flow.strip())
        funcs2[k2] = v2
        nodes[k2] = []

    ans = 0
    for part in parts.split():
        xmas = {}
        for x in part.strip()[1:-1].split(','):
            k, v = x.split('=')
            xmas[k] = int(v)

        cur = 'in'
        while cur not in ('A', 'R'):
            cur = funcs[cur](xmas)

        if cur == 'A':
            ans += sum(xmas.values())

    print(ans)  # Part 1

    nodes['in'] = [{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}]

    while True:
        okay = True
        for k in funcs2:
            if len(nodes[k]) > 0:
                for xmas in nodes[k]:
                    funcs2[k](xmas)
                nodes[k] = []
                okay = False
        if okay:
            break

    ans2 = sum([math.prod([v[1] - v[0] + 1 for v in xmas.values()]) for xmas in nodes['A']])
    print(ans2)
