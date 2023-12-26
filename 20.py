with open('input.txt') as fp:
    modules, inputs = {}, {}

    q, send_counter = [], [0, 0]
    last_received = {}
    def send(signal, src, dst):
        for d in dst:
            q.append((signal, src, d))
            send_counter[signal] += 1
            last_received.setdefault(d, {})[signal] = press_counter

    states = {}

    def create_flipflop(name, dst):
        states[name] = False
        def receive(signal, src):
            if signal:
                return
            states[name] = not states[name]
            send(states[name], name, dst)
        return receive

    def create_conjunction(name, dst):
        states[name] = {}
        def receive(signal, src):
            states[name][src] = signal
            if all(states[name].get(inp) for inp in inputs[name]):
                send(False, name, dst)
            else:
                send(True, name, dst)

        return receive

    def create_broadcaster(name, dst):
        def receive(signal, src):
            send(signal, name, dst)
        return receive


    def noop_receiver(signal, src):
        return

    for module in fp.readlines():
        src, dst = module.strip().split(' -> ')
        dst = dst.split(', ')

        # for d in dst:
        #     print(src[1:], d)

        if src.startswith('%'):
            src = src[1:]
            modules[src] = create_flipflop(src, dst)
        elif src.startswith('&'):
            src = src[1:]
            modules[src] = create_conjunction(src, dst)
        elif src == 'broadcaster':
            modules[src] = create_broadcaster(src, dst)
        for d in dst:
            inputs.setdefault(d, []).append(src)

    press_counter = 0
    def press():
        global press_counter
        press_counter += 1
        q.clear()
        send(False, 'button', ['broadcaster'])
        for signal, src, dst in q:
            modules.get(dst, noop_receiver)(signal, src)

    def part1():
        for _ in range(1000):
            press()
        return send_counter[0] * send_counter[1]

    def part2():
        rx_turned_on = False
        def rx_receive(signal, src):
            nonlocal rx_turned_on
            if not signal:
                rx_turned_on = True
        modules['rx'] = rx_receive

        ss = set()
        cycles = {}
        while not rx_turned_on:
            press()

            for name in inputs['qn']:
                if last_received[name].get(False, -1) == press_counter:
                    cycles.setdefault(name, press_counter)

            if len(cycles) == len(inputs['qn']):
                return __import__('math').prod(cycles.values())
        return press_counter

    print(part2())
