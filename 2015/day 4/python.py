import hashlib

try:
    with open('input.txt') as file:
        key = file.read()
except:
    with open('day 4\\input.txt') as file:
        key = file.read()

# ckczppom
n = 0
while 1:
    key_ = key + str(n)

    out = hashlib.md5(key_.encode()).hexdigest()

    # part 2 : '000000'
    if out.startswith('00000'):
        print(out)
        print(key_)
        break
    print(n, end='\r')
    n += 1