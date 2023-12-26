import collections

with open('input.txt') as fp:
    bids = [line.strip().split() for line in fp.readlines()]

    def hand_type(cards):
        counts = sorted(collections.Counter(cards).values(), reverse=True)

        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts == [3, 2]:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0:2] == [2, 2]:
            return 2
        if counts[0] == 2:
            return 1
        return 0

    def hand_str(bid):
        cards, _ = bid

        strength = 'AKQJT98765432'
        hand = hand_type(cards)

        solving_part2 = True
        if solving_part2:
            strength = 'AKQT98765432J'
            hand = max([hand_type(cards.replace('J', t)) for t in strength])

        return [hand] + [-strength.find(card) for card in cards]

    bids.sort(key=hand_str)

    ans = 0
    for rank, bid in enumerate(bids):
        ans += (rank + 1) * int(bid[1])
    print(ans)
