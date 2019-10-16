"""
ID: mail4rp1
LANG: PYTHON3
TASK: combo
"""
#
# with open('combo.in') as f:
#     lines = [line.strip() for line in f.readlines()]
#     highest_num = int(lines[0])
#     farmer_combo = [int(x) for x in lines[1].split(' ')]
#     master_combo = [int(x) for x in lines[2].split(' ')]
#
# combinations = { tuple(farmer_combo), tuple(master_combo) }
#
# all_nums = []
#
# def index(x):
#     return all_nums.index(x)
# # 1234
# # 3 + 2
# # (3 + 2) - 4 + 1
# def get_index_wrap_around(digit, offset):
#     print("highest_num\t",highest_num)
#     print("digit\t", digit)
#     print("offset\t", offset)
#     print()
#     if digit + i > highest_num:
#         print("Wrapping around from", digit + offset, "to", highest_num - (digit + offset))
#         return index((digit + offset) - highest_num + 1)
#     else:
#         return index(digit) + offset
#
# for i in range(0,highest_num):
#     all_nums.append(i + 1)
#
# if highest_num == 1 :
#     with open('combo.out', 'w') as f:
#         f.write('1' + '\n')
# elif highest_num == 2:
#     with open('combo.out', 'w') as f:
#         f.write('8' + '\n')
# elif highest_num == 3:
#     with open('combo.out', 'w') as f:
#         f.write('27' + '\n')
# elif highest_num == 4:
#     with open('combo.out', 'w') as f:
#         f.write('64' + '\n')
# else:
#     for i in range(-2,3):
#         digit00 = all_nums[get_index_wrap_around(farmer_combo[0], i)]
#         digit10 = all_nums[get_index_wrap_around(master_combo[0], i)]
#
#             #print(digit0)
#         for j in range(-2,3):
#
#             digit01 = all_nums[get_index_wrap_around(farmer_combo[1], j)]
#             digit11 = all_nums[get_index_wrap_around(master_combo[1], j)]
#             #print(digit1)
#             for k in range(-2,3):
#                     digit02 = all_nums[get_index_wrap_around(farmer_combo[2], k)]
#                     combinations.add((digit00, digit01, digit02))
#                     digit12 = all_nums[get_index_wrap_around(master_combo[2], k)]
#                     combinations.add((digit10, digit11, digit12))
#     with open('combo.out', 'w') as f:
#         f.write(str(len(combinations)) + '\n')



def readInput():
    f = open("combo.in")
    text = f.readlines()
    f.close()

    # read in maxNum and the two codes
    maxNum = int(text[0])
    farmerCombo = text[1].split()
    masterCombo = text[2].split()
    for i in range(3):
        farmerCombo[i] = int(farmerCombo[i])
        masterCombo[i] = int(masterCombo[i])

    return maxNum, farmerCombo, masterCombo

# function that takes in a number and generates a list of the 2 numbers above and below
def generateNumPossibilities(num, maxNum):
    nums = []

    # handle special case where maxNum <= 5
    if maxNum <= 5:
        for i in range(1,maxNum+1): 
            nums.append(i)
        return nums

    for i in range(-2,3):
        codeNum = num + i
        if codeNum < 1:
            codeNum = maxNum + codeNum
        elif codeNum > maxNum:
            codeNum = codeNum - maxNum
        nums.append(codeNum)
    return nums

# function that generates a set of the possible combos, given a code
def generateCombos(code, maxNum):
    combos = set()
    numPossibilities = []

    for i in range(3):
        numPossibilities.append(generateNumPossibilities(code[i], maxNum))

    for i in numPossibilities[0]:
        for j in numPossibilities[1]:
            for k in numPossibilities[2]:
                combo = str(i) + '-' + str(j) + '-' + str(k)
                combos.add(combo)

    return combos

def main(maxNum, farmerCombo, masterCombo):
    # generate the possible combos for both codes
    farmerCombos = generateCombos(farmerCombo, maxNum)
    masterCombos = generateCombos(masterCombo, maxNum)

    # find the size of the union of the possible combos
    numPossibleCombos = len(farmerCombos.union(masterCombos))

    return numPossibleCombos

def writeOutput(numPossibleCombos):
    f = open("combo.out", "w")
    f.write(str(numPossibleCombos) + "\n")
    f.close()

maxNum, farmerCombo, masterCombo = readInput()
numPossibleCombos = main(maxNum, farmerCombo, masterCombo)
writeOutput(numPossibleCombos)
