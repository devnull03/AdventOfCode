try:
    with open('input.txt') as file:
        l = file.readlines()
except:    
    with open('day 5\\input.txt') as file:
        l = file.readlines()

# row range = (0,127)
# seat range = (0,8)

seatIDs = []

values = {
    'F': lambda row: (row[0], row[0]+abs(row[1]-row[0])//2),
    'B': lambda row: (row[1]-abs(row[1]-row[0])//2, row[1]),
    'L': lambda seat: (seat[0], seat[0]+abs(seat[1]-seat[0])//2),
    'R': lambda seat: (seat[1]-abs(seat[1]-seat[0])//2, seat[1]),
}

# part 1
for i in l:
    row, seat = (0,127),(0,7)
    for e in i.rstrip('\n'):
        if e in ('F', 'B'):
            row = values[e](row)
        else:
            seat = values[e](seat)
    else:
        seatIDs.append(row[0]*8+seat[0])
else:
    print(max(seatIDs))

# print(sorted(seatIDs))
# print(max(seatIDs), min(seatIDs))
# for i,j in zip(sorted(seatIDs), range(6,934)):
#     print(i,j, i==j)

# part 2
for i in range(6,934):
    if i not in seatIDs:
        print(i)
