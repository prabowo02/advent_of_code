import itertools

with open('input.txt') as fp:
    adj = {}

    for line in fp.readlines():
        u, vs = line.strip().split(': ')
        for v in vs.split():
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
    root = u

    def maxflow(adj, s, t):
        cap = {u: {v: 1 for v in adj[u]} for u in adj}
        def bfs():
            q, par = [s], {s: None}
            for u in q:
                for v in adj[u]:
                    if v not in par and cap[u][v] > 0:
                        par[v] = u
                        q.append(v)
            return par

        flow = 0
        while t in (par := bfs()):
            flow, u = flow + 1, t
            while u != s:
                cap[par[u]][u] -= 1
                cap[u][par[u]] += 1
                u = par[u]
        return flow, len(par)

    ans = None
    for s, t in itertools.combinations(adj, 2):
        flow, sz = maxflow(adj, s, t)
        if flow == 3:
            ans = sz * (len(adj) - sz)
            break
    print(ans)
