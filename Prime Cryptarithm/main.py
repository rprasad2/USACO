"""
ID: mail4rp1
LANG: PYTHON3
TASK: crypt1
"""
# 5
# 2 3 4 6 8

with open("crypt1.in") as f:
    lines = [line.strip() for line in f.readlines()]
    digits = int(lines[0])
    values = [int(x) for x in lines[1].split(' ')]
works = 0
for i in range(0, digits):
    a = int(values[i])
    for j in range(0, digits):
        b = int(values[j])
        for k in range(0, digits):
            c = int(values[k])
            for l in range(0, digits):
                d = int(values[l])
                for m in range(0, digits):
                    e = int(values[m])
                    x = ((a * 100) + (b * 10) + c) * d
                    y = ((a * 100) + (b * 10) + c) * e
                    sum = x + (y * 10)
                    if len(str(x)) == len(str(y)):
                        xa = []
                        ya = []
                        suma = [int(x) for x in str(sum)]
                        xa = [int(x) for x in str(x)]
                        ya = [int(x) for x in str(y)]
                        res1 = all(x in values for x in xa)
                        res2 = all(x in values for x in ya)
                        res3 = all(x in values for x in suma)
                        if res1 and res2 and res3 and len(str(sum)) == 4:
                            works += 1
                            print('xa:', xa, '\nya:', ya, '\nsuma:', suma)
with open("crypt1.out", 'w+') as f:
    f.write(str(works) + '\n')




# ---------------------- SAMPLE SOLUTION -----------------
"""
ID: roobeel1
LANG: PYTHON3
TASK: crypt1
"""

def read_input():
    with open("crypt1.in", "r") as f:
        data = f.readlines()
    nums = data[1].strip().split()
    return nums# generate all possible options for the two numbers that will be multipled together
def generate_options(nums):
    num_one_options = []
    num_two_options = []
    for i in nums:
        for j in nums:
            for k in nums:
                num_one_options.append(i+j+k)
    for i in nums:
        for j in nums:
            num_two_options.append(i+j)
    return num_one_options, num_two_options
def main(num_one_options, num_two_options):# generate the three numbers involved in the multiplication# check combination for its validity
    counter = 0
    for i in num_one_options:
        for j in num_two_options:
            num1 = i
            num2 = j
            row1 = int(num1) * int(num2[1])
            row2 = int(num1) * int(num2[0])
            product = int(num1) * int(num2)
            isValid = True        # make sure that each number is the correct number of digits
            if row1 > 999 or row2 > 999 or product > 9999:
                isValid = False
            row1 = str(row1)
            row2 = str(row2)
            product = str(product)    # check that each number only contains valid digits
            for k in row1:
                if k not in nums:
                    isValid = False
            for k in row2:
                if k not in nums:
                    isValid = False
            for k in product:
                if k not in nums:
                    isValid = False
            if isValid:
                counter += 1
    return counter
def write_output(answer):
    with open("crypt1.out", "w+") as f:
        f.write(str(answer) + "\n")
nums = read_input()
num_one_options, num_two_options = generate_options(nums)
answer = main(num_one_options, num_two_options)
write_output(answer)
