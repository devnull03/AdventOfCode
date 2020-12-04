from typing import get_origin


try:
    with open('input.txt') as file:
        l = file.read().split('\n\n')
except:    
    with open('day 4\\input.txt') as file:
        l = file.read().split('\n\n')


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

fields = [
    "byr:",
    "iyr:",
    "eyr:",
    "hgt:",
    "hcl:",
    "ecl:",
    "pid:",
    # "cid:"
]
sp = lambda a: [e.split(':') for e in a.split()]
# part 1
test = lambda x: all((field in x for field in fields))
result = 0
for i in l:
    if test(i):
        result +=1
        print(sp(i))
else:
    print(result)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def height(x:str)  -> bool:
    if x.endswith('cm'):
        return 150 <= int(x.rstrip('cm')) <= 193
    elif x.endswith('in'):
        return 59 <= int(x.rstrip('in')) <= 76
    else:
        return False
c = (*list(map(str, range(10))),*list('abcdef'))

def hcl(x:str) -> bool:
    if x.startswith('#') and len(x)==7:
        for i in x.lstrip('#'):
            if i not in c:
                return False
            else:
                return True
    else:
        return False

conditions = {
    "byr": lambda x: len(x)==4 and 1920<=int(x)<=2002 ,
    "iyr": lambda x: len(x)==4 and 2010<=int(x)<=2020 ,
    "eyr": lambda x: len(x)==4 and 2020<=int(x)<=2030 ,
    "hgt": height ,
    "hcl": hcl ,
    "ecl": lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
    "pid": lambda x: len(x)==9 and all(e.isdigit() for e in x),
    "cid": lambda _: True
}

# part 2
result = 0
for i in l:
    if test(i):
        args = sp(i)
        a = [conditions[e[0]](e[1]) for e in args]
        print(a)
        result += all(a)
else:
    print(result)

