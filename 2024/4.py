def main():
    with open('input.txt') as fp:
        words = [line.strip() for line in fp.readlines()]
        
        dxs, dys = [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]
        s = 'XMAS'

        ans = 0
        for i in range(len(words)):
            for j in range(len(words[i])):
                for dx, dy in zip(dxs, dys):
                    can = True
                    for k in range(len(s)):
                        nx, ny = i + dx * k, j + dy * k
                        if 0 <= nx < len(words) and 0 <= ny < len(words[nx]) and words[nx][ny] == s[k]:
                            continue
                        can = False
                        break

                    if can:
                        ans += 1

        print(ans)

        ans = 0
        for i in range(1, len(words) - 1):
            for j in range(1, len(words[i]) - 1):
                if words[i][j] != 'A':
                    continue
                if words[i - 1][j - 1] + words[i + 1][j + 1] not in ('MS', 'SM'):
                    continue
                if words[i - 1][j + 1] + words[i + 1][j - 1] not in ('MS', 'SM'):
                    continue
                ans += 1

        print(ans)


if __name__ == '__main__':
    main()
