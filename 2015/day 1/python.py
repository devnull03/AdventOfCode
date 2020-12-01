
try:
    with open('inputs.txt') as file:
        l = list(file.read())
except:
    with open('day 1\\inputs.txt') as file:
        l = list(file.read())

d = {
    ')': -1,
    '(': 1
}
result = 0

for j,i in enumerate(l):
    try:
        result += d[i]
        # part 2 ------
        if result == -1:
            print(j+1)
        # -------------
    except KeyError:
        print(i)
else:
    print('------')
    print(result)