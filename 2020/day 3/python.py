try:
    with open('input.txt') as file:
        lines = file.readlines()
        l = [list(i.rstrip('\n')*73) for i in lines]
except:    
    with open('day 3\\input.txt') as file:
        lines = file.readlines()
        l = [list(i.rstrip('\n')*73) for i in lines]

line = [
    lambda y: y,
    lambda y: y*3,
    lambda y: y*5,
    lambda y: y*7
]
line5 = lambda y: y*(1/2)

print(line[0](323)/ len(l[0]))
print(line[1](323)/ len(l[0]))
print(line[2](323)/ len(l[0]))
print(line[3](323)/ len(l[0]))

# Right 1, down 1.
# Right 3, down 1.  (part 1)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


trees = 1   # 73392264
for e in line:
    tree = 0
    for i in range(0, 323):
        if l[i][e(i)] == '#':
            tree += 1
    else:
        trees *= tree
else:
    print(trees)
    tree = 0
    for i in range(0, 323, 2):
        if l[i][int(i*0.5)] == '#':
            tree += 1
    else:

        trees *= tree
print(trees)