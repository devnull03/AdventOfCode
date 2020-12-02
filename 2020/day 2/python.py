try:
    with open('input.txt') as file:
        l = (i.rstrip('\n').split(': ') for i in file.readlines())

except:    
    with open('day 2\\input.txt') as file:
        l = (i.rstrip('\n').split(': ') for i in file.readlines())

# part 1
def check1(x:list):
    password:str = x[1]
    policy = (list(map(int,(a:=x[0].split())[0].split('-'))), a[1])
    return policy[0][0] <= password.count(policy[1]) <= policy[0][1]

# result = 0
# for i in l:
#     result += check1(i)
# else:
#     print(result)

# part 2
def check2(x:list):
    password:str = x[1]
    policy = (list(map(int,(a:=x[0].split())[0].split('-'))), a[1])
    first = password[policy[0][0]-1] == policy[1]
    last = password[policy[0][1]-1] == policy[1]
    return first ^ last

result = 0
for e in l:
    result += check2(e)
else:
    print(result)