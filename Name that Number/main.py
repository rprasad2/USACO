"""
ID: mail4rp1
LANG: PYTHON3
TASK: namenum
"""

with open("namenum.in") as f:
    lines = [line.strip() for line in f.readlines()]
with open("dict.txt") as f:
    names = [name.strip() for name in f.readlines()]

name_len = len(lines[0])
nameid = str(lines[0])
matching_names = [] # the output
all_names_len = []

letter_to_number = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9'
}

for name in names:
    if not len(name) == name_len or 'Q' in name or 'Z' in name:
        continue
    all_names_len.append(name)

for name in all_names_len:
    curr_nameid = ''
    for letter in name:
        curr_nameid += letter_to_number[letter]

    print(curr_nameid)
    if curr_nameid == nameid:
        matching_names.append(name)

with open("namenum.out", 'w') as f:
    if len(matching_names) > 0:
        for name in matching_names:
            f.write(name + '\n')
    else:
        f.write("NONE" + "\n")

# """
# ID: roobeel1
# LANG: PYTHON3
# TASK: namenum
# """
#
# def readInput():
#     fin = open('dict.txt')
#     names = fin.readlines()
#     fin.close()
#
#     fin = open('namenum.in')
#     data = fin.readlines()
#     fin.close()
#     brandNum = data[0].strip()
#
#     return names, brandNum
#
# # returns dictionary where keys are serial nums and values are lists of names
# def translateNames(names):
#     nameNumDict = {}
#
#     for name in names:
#         name = name.strip()
#         nameNum = ''
#         for letter in name:
#             num = 0
#             # special case for after Q
#             if ord(letter) > ord('Q'):
#                 num = int((ord(letter)-66)/3) + 2
#             else:
#                 num = int((ord(letter)-65)/3) + 2
#             nameNum += str(num)
#
#         if nameNum in nameNumDict:
#             nameNumDict[nameNum].append(name)
#         else:
#             nameNumDict[nameNum] = [name]
#
#     return nameNumDict
#
# # writes output
# def writeOutput(nameNumDict, brandNum):
#     fout = open('namenum.out', 'w')
#
#     if brandNum in nameNumDict:
#         names = nameNumDict[brandNum]
#         for name in names:
#             fout.write(name + '\n')
#     else:
#         fout.write('NONE\n')
#
#     fout.close()
#
# names, brandNum = readInput()
# nameNumDict = translateNames(names)
# writeOutput(nameNumDict, brandNum)
