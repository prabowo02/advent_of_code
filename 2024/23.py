import functools
import itertools


def main():
    with open('input.txt') as fp:
        edges = [line.strip().split('-') for line in fp.readlines()]
    nodes = sorted(set(itertools.chain(*edges)))
    adj = {}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)

    triples = set()
    for u, v in edges:
        for w in adj[u].intersection(adj[v]):
            triples.add(tuple(sorted([u, v, w])))

    def maxclique():
        @functools.cache
        def dfs(i, clique):
            if i == len(nodes):
                return clique
            ret = dfs(i + 1, clique)
            if adj[nodes[i]].issuperset(set(clique)):
                nclique = dfs(i + 1, tuple(list(clique) + [nodes[i]]))
                if len(nclique) > len(ret):
                    ret = nclique
            return ret

        return dfs(0, ())

    print(sum(1 for u, v, w, in triples if u.startswith('t') or v.startswith('t') or w.startswith('t')))
    print(','.join(maxclique()))


if __name__ == '__main__':
    main()
