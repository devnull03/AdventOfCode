import re


try:
    with open('input.txt') as file:
        l = [(i.rstrip('\n')) for i in file.readlines()]
except FileNotFoundError:
    with open('day 1/input.txt') as file:
        l = [(i.rstrip('\n').split('')) for i in file.readlines()]

# part 1
# total = 0
# for line in l:
#     a = list(filter(lambda x: x.isnumeric(), line))
#     total += int(a[0] + a[len(a) - 1])

# print(total)


# part 2

# l = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for line in l:
    print(line)
    reg = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)

    for i in range(len(reg)):
        if reg[i] in digits:
            reg[i] = str(digits.index(reg[i]) + 1)

    print(reg)
    
    print(int(reg[0] + reg[len(reg) - 1]))
    total += int(reg[0] + reg[len(reg) - 1])

print(total)
