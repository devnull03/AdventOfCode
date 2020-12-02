import numpy

try:
    with open('input.txt') as file:
        l = file.readlines()
except:
    with open('day 6\\input.txt') as file:
        l = file.readlines()

a = numpy.zeros((1000,1000), dtype=int)

# example: "turn on 753,664 through 970,926"
#           012345678901234567890123456789
#                     11111111112222222222
# 
# 0,0   ....... 0,999
# .               .
# .               .
# .               .
# 999,0 ....... 999,999

for line in l:
    if line.startswith('toggle'):
        start = list(map(int, line.split()[1].split(',')))
        end = list(map(int, line.split()[3].split(',')))
        func = lambda x: x+2

    else:
        start = list(map(int, line.split()[2].split(',')))
        end = list(map(int, line.split()[4].split(',')))
        if line.startswith('turn on'):
            # part 1: func = lambda x: 1
            func = lambda x: x+1
        else:
            # part 1: func = lambda x: 0
            func = lambda x: [0,x-1][x>0]

    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            a[i,j] = func(a[i,j])
    
    print(f'{numpy.sum(a)}        ', end='\r')
 