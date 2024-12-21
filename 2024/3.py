import re

def main():
    with open('input.txt') as fp:
        instructions = re.findall(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', fp.read())
        
        ans1, ans2 = 0, 0
        enabled = True
        for instruction, x, y in instructions:
            if instruction.startswith('mul'):
                ans1 += int(x) * int(y)
                if enabled:
                    ans2 += int(x) * int(y)
            elif instruction == 'do()':
                enabled = True
            else:
                enabled = False

        print(ans1)
        print(ans2)

if __name__ == '__main__':
    main()
