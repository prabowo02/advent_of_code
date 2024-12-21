import string


def main():
    with open('input.txt') as fp:
        s = [line.strip() for line in fp.readlines()]
        nodes = {}

        for i, row in enumerate(s):
            for j, col in enumerate(row):
                if col in string.ascii_letters + string.digits:
                    nodes.setdefault(col, []).append((i, j))


        def inside(node):
            return 0 <= node[0] < len(s) and 0 <= node[1] < len(s[node[0]])

        def mul(scalar, node):
            return node[0] * scalar, node[1] * scalar

        def add(node1, node2):
            return node1[0] + node2[0], node1[1] + node2[1]



        antinodes = set()
        antinodes2 = set()
        for freq in nodes:
            for i in range(len(nodes[freq])):
                for j in range(i + 1, len(nodes[freq])):
                    antinodes.add(add(mul(2, nodes[freq][j]), mul(-1, nodes[freq][i])))
                    antinodes.add(add(mul(2, nodes[freq][i]), mul(-1, nodes[freq][j])))

                    k = 0
                    delta = add(nodes[freq][j], mul(-1, nodes[freq][i]))
                    while True:
                        tnode = add(nodes[freq][i], mul(k, delta))
                        if not inside(tnode):
                            break
                        antinodes2.add(tnode)
                        k += 1
                    k = -1
                    while True:
                        tnode = add(nodes[freq][i], mul(k, delta))
                        if not inside(tnode):
                            break
                        antinodes2.add(tnode)
                        k -= 1



        antinodes = {node for node in antinodes if inside(node)}
        print(len(antinodes))
        print(len(antinodes2))

if __name__ == '__main__':
    main()
