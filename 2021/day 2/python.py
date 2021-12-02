try:
    with open('input.txt') as file:
        l = [(i.rstrip('\n').split(' ')) for i in file.readlines()]
except FileNotFoundError:
    with open('day 2/input.txt') as file:
        l = [(i.rstrip('\n').split(' ')) for i in file.readlines()]


hPos:int = 0
depth:int = 0

for i in l:
    if i[0] == 'forward': hPos += int(i[1])
    elif i[0] == 'down': depth += int(i[1])
    elif i[0] == 'up': depth -= int(i[1])

print(f'Part 1:\n {hPos=} {depth=} {hPos*depth=} ')

# Part 2

aim:int = 0
depth:int = 0
hPos:int = 0

for i in l:
    if i[0] == 'forward': 
        hPos += int(i[1])
        depth += int(i[1]) * aim
    elif i[0] == 'down': aim += int(i[1])
    elif i[0] == 'up': aim -= int(i[1])


print(f'Part 2:\n {hPos=} {depth=} {hPos*depth=} ')
