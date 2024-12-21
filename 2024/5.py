def main():
    with open('input.txt') as fp:
        nodes = set()
        adj = {}
        while line := fp.readline().strip():
            u, v = line.split('|')
            nodes.add(u)
            nodes.add(v)
            adj.setdefault(u, set()).add(v)


        def ordered(ls):
            for i in range(len(ls)):
                for j in range(i + 1, len(ls)):
                    if ls[i] in adj.get(ls[j], set()):
                        return False
            return True


        def order(ls):
            iadj = {}
            for u in ls:
                iadj[u] = adj.get(u, set()).intersection(ls)
            deg = {u: 0 for u in ls}

            for u in iadj:
                for v in iadj[u]:
                    deg[v] += 1
            q = [u for u in ls if deg[u] == 0]
            for u in q:
                for v in iadj[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.append(v)
            assert(len(ls) == len(q))
            return q


        ans, ans2 = 0, 0
        for line in fp.readlines():
            ls = line.strip().split(',')
            if ordered(ls):
                ans += int(ls[len(ls) // 2])
            else:
                ans2 += int(order(ls)[len(ls) // 2])

        print(ans)
        print(ans2)


if __name__ == '__main__':
    main()
