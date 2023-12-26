with open('input.txt') as fp:
    red, green, blue = 12, 13, 14
    ans = 0
    ans2 = 0
    for game_id, line in enumerate(fp.readlines()):
        min_red, min_green, min_blue = 0, 0, 0
        game = line.split(':')[-1]
        possible = True
        for balls in game.split(';'):
            for colors in balls.split(','):
                count, color = colors.split()
                count = int(count)

                if color == 'blue' and count > blue:
                    possible = False
                if color == 'green' and count > green:
                    possible = False
                if color == 'red' and count > red:
                    possible = False

                if color == 'blue':
                    min_blue = max(min_blue, count)
                if color == 'green':
                    min_green = max(min_green, count)
                if color == 'red':
                    min_red = max(min_red, count)

        if possible:
            ans += game_id + 1
        ans2 += min_blue * min_green * min_red

    print(ans)
    print(ans2)
