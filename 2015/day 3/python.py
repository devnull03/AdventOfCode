try:
    with open('inputs.txt') as file:
        l = list(file.read())
except:
    with open('day 3\\inputs.txt') as file:
        l = list(file.read())
d = {
    '^': 1,
    'v': -1,
    '<': -1,
    '>': 1
}

# part 1 ---------------
x, y = 0, 0
history = {(0,0)}
for i in l:
    if i in ('^','v'):
        y += d[i]
    else:
        x += d[i]
    history.add((x,y))
# print(len(history))
# ----------------------

# part 2 

santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
history = {(0,0)}
n = 0
for i in l:
    if n == 0 :
        if i in ('^','v'):
            santa_y += d[i]
        else:
            santa_x += d[i]
        n = 1
        history.add((santa_x, santa_y))
    else:
        if i in ('^','v'):
            robo_y += d[i]
        else:
            robo_x += d[i]
        history.add((robo_x, robo_y))
        n = 0


print(len(history))