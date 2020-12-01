try:
    with open('inputs.txt') as file:
        l = [int(i.rstrip('\n')) for i in file.readlines()]
except:
    with open('day 1/inputs.txt') as file:
        l = [int(i.rstrip('\n')) for i in file.readlines()]

# part 1
for j,i in enumerate(l):
    for a,b in enumerate(l):
        if j != a:
            if i+b == 2020:
                print(i*b)

# part 2
for j,i in enumerate(l):
    for c,d in enumerate(l):
        for a,b in enumerate(l):
            if j != a and a != c:
                if i+b+d == 2020:
                    print(i*b*d)
