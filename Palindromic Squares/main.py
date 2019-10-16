"""
ID: mail4rp1
LANG: PYTHON3
TASK: palsquare
"""

# ALGORITHM:
# https://mathbits.com/MathBits/CompSci/Introduction/frombase10.htm

with open('palsquare.in') as f:
    lines = f.readlines()
    base = int(lines[0])

# Normal division: 345 / 13 = 26.5384615385
# quotient = 345 // 13 = 26
# remainder = 345 % 13 = 7

"""
1.  Divide the "desired" base INTO the number you are trying to convert.
2.  Save the integer quotient and integer remainder separately.
3.  Repeat this division process using the previous quotient.
4.  Continue repeating this division until the quotient is zero.
5.  The final answer is the remainders read from the bottom up.
"""

num_to_letter= {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J'
}

palsquare = []

def convert_to_base(N, base, remainders=[]):
    if N == 0:
        return ''.join(remainders[::-1])
    else:
        div = N // base
        remainder = N % base
        if remainder > 9:
            remainder = num_to_letter[remainder]
        #print(remainders)
        return convert_to_base(div, base, remainders + [str(remainder)])

for N in range(1, 301):
    # N ** 2
    # N * N
    square = N ** 2
    converted = convert_to_base(N, base)
    converted_square = convert_to_base(square, base)
    if converted_square == converted_square[::-1]:
        palsquare.append((converted, converted_square))
    # '101001010'
    # '1E420'
    # 'A232A'

with open('palsquare.out', 'w') as f:
    for pair in palsquare:
        f.write(pair[0] + ' ' + pair[1] + '\n')
