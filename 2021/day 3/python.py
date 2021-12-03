from typing import Counter
import numpy
from numpy.core.fromnumeric import sort
try:
    with open('input.txt') as file:
        l: numpy.ndarray = numpy.array(
            [list(i.rstrip('\n')) for i in file.readlines()])
except FileNotFoundError:
    with open('day 3/input.txt') as file:
        l: numpy.ndarray = numpy.array(
            [list(i.rstrip('\n')) for i in file.readlines()])

gamma: str = ''
for i in range(len(l[0])):
    gamma += Counter(l[:, i]).most_common(1)[0][0]
epsilon = ''.join([str(int(not int(i))) for i in gamma])
epsilon, gamma = int(epsilon, 2), int(gamma, 2)
print(f"Part 1: {epsilon*gamma}")

# part 2

ogr: int
csr: int

for thing in [0, 1]:

    l2 = l.copy()
    for i in range(len(l2[0])):
        to_be_deleted = []
        c = Counter(l2[:, i]).most_common()
        # print(c)
        if len(c) == 1:
            break

        if c[0][1] == c[1][1]:
            target = '1'
        else:
            target = c[0][0]
            # print(f"{target=} { str(int(not int(target))) } ")

        if thing:
            target = str(int(not int(target)))
        for j in range(numpy.shape(l2)[0]):
            if not l2[j][i] == target:
                to_be_deleted.append(j)

        to_be_deleted = sorted(set(to_be_deleted), reverse=1)
        for j in to_be_deleted:
            l2 = numpy.delete(l2, j, 0)

    if thing:
        csr = int(''.join(l2[0]), 2)
    else:
        ogr = int(''.join(l2[0]), 2)

print(f"{csr=} {ogr=} ")
print(f'Part 2: {csr*ogr}')
