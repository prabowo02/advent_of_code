import itertools


def main():
    def const_factory(c):
        return lambda: c

    def ops_factory(a, op, b):
        return {
            'AND': lambda: globals()[a]() & globals()[b](),
            'OR': lambda: globals()[a]() | globals()[b](),
            'XOR': lambda: globals()[a]() ^ globals()[b](),
        }[op]

    outs = []
    with open('input.txt') as fp:
        vals, gates = fp.read().split('\n\n')
        for leaf in vals.split('\n'):
            k, v = leaf.split(': ')
            globals()[k] = const_factory(int(v))

        gates = [gate.strip().split() for gate in gates.split('\n')]
        for gate in gates:
            globals()[gate[-1]] = ops_factory(gate[0], gate[1], gate[2])

    def get_value(var):
        return int(''.join(str(globals()[k]()) for k in sorted(k for k in globals() if k.startswith(var))[::-1]), 2)

    # Part 1
    print(get_value('z'))

    swapped = {}
    def gen_dot_graphviz():
        # Use graphviz: `dot -Tvsg test.dot > test.svg`
        with open('test.dot', 'w') as fp:
            fp.write('digraph {{\n')
            for gate in gates:
                col = {
                    'AND': 'blue',
                    'XOR': 'red',
                    'OR': 'black' 
                }[gate[1]]
                x, y, z = gate[0], gate[2], swapped.get(gate[-1], gate[-1])
                fp.write('{}_{} -> {}_{} [color={}]\n'.format(x, globals()[x](), z, globals()[z](), col))
                fp.write('{}_{} -> {}_{} [color={}]\n'.format(y, globals()[y](), z, globals()[z](), col))
            fp.write('}}\n')

    def swap(o1, o2):
        assert o1 not in swapped and o2 not in swapped
        swapped[o1], swapped[o2] = o2, o1
        globals()[o1], globals()[o2] = globals()[o2], globals()[o1]

    swap('cmv', 'z17')
    swap('btb', 'mwp')
    swap('rmj', 'z23')
    swap('z30', 'rdg')
    gen_dot_graphviz()

    x, y, z = get_value('x'), get_value('y'), get_value('z')
    # print(len(bin(z ^ x + y)) - len(bin(z ^ x + y).rstrip('0')))
    print(','.join(sorted(swapped.values())))


if __name__ == '__main__':
    main()
