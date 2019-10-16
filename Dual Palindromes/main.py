"""
ID: mail4rp1
LANG: PYTHON3
TASK: dualpal
"""
import math

with open('dualpal.in') as f:
    lines = f.readlines()
    line = lines[0].split(' ')
    needed = int(line[0])
    start = int(line[1])

found = 0
dualpals = []


def convert_to_base(N, base, remainders=[]):
    if N == 0:
        return ''.join(remainders[::-1])
    else:
        div = N // base
        remainder = N % base
        return convert_to_base(div, base, remainders + [str(remainder)])

for i in range(start + 1, 10000000000000000000000000000000000000):
    num_of_pal = 0
    for j in range(2, 11):
        converted_num = convert_to_base(i,j)
        if converted_num == converted_num[::-1]:
            num_of_pal += 1
    if num_of_pal >= 2:
        dualpals.append(i)
        found += 1
    if found == needed:
        break

with open('dualpal.out', 'w') as f:
    for dualpal in dualpals:
        f.write(str(dualpal) + '\n')
