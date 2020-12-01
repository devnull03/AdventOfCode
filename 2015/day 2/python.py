try:
    with open('inputs.txt') as file:
        l = [
            list(map(int, i.rstrip('\n').split('x'))) for i in file.readlines()
        ]
except:
    with open('day 2\\inputs.txt') as file:
        l = [
            list(map(int, i.rstrip('\n').split('x'))) for i in file.readlines()
        ]

surfaceArea = lambda l,w,h: 2*l*w + 2*w*h + 2*h*l
smallestSide = lambda l,w,h: min(( l*w, l*h, w*h ))
totalArea = 0

# part 2 ------
volume = lambda l,w,h: l*w*h
smallestPerimeter = lambda l,w,h: min(( 2*(l+w), 2*(l+h), 2*(h+w) ))
totalRibbon = 0
# -------------

for present in l:
    totalArea += surfaceArea(*present) + smallestSide(*present)
    totalRibbon += volume(*present) + smallestPerimeter(*present)

print(totalArea, totalRibbon)