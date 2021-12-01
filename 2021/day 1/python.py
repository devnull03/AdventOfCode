try:
    with open('input.txt') as file:
        l = [int(i.rstrip('\n')) for i in file.readlines()]
except FileNotFoundError:
    with open('day 1/input.txt') as file:
        l = [int(i.rstrip('\n')) for i in file.readlines()]

totalLines:int = 0
for i in range(1,len(l)):
    totalLines += l[i] > l[i-1]

print(f'Part one: {totalLines}')

# part2

total2:int = 0
newL:list = [
    l[i]+l[i+1]+l[i+2] for i in range(len(l)-2)
]
for i in range(1,len(newL)):
    try: 
        total2 += newL[i] > newL[i-1]
    except IndexError:
        print(i)


print(f'Part 2: {total2}')