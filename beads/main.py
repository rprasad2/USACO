"""
ID: mail4rp1
LANG: PYTHON3
TASK: beads
"""
with open("beads.in") as f:
    lines = [line.strip() for line in f.readlines()]
    beads = lines[1]


bead_count = len(beads)

lengths = {
"r":0,
"b":0
}

def find_max(beads):
    max = 0
    for bead_index in range(bead_count):
        num_beads = 0

        for j in range(2):
            first_bead = beads[bead_index]
            while True:
                if first_bead == "w":
                    num_beads += 1
                    first_bead = beads[bead_index]
                    bead_index += 1
                elif first_bead == beads[bead_index] or beads[bead_index] == "w":
                    num_beads += 1
                    bead_index += 1
                else:
                    break

                if bead_index == bead_count:
                    bead_index = 0


                if num_beads == bead_count:
                    return num_beads

        if num_beads > max:
            max = num_beads

    return max

with open("beads.out", "w") as f:
    f.write(str(find_max(beads)) + "\n")







#Check the previous bead
#Retuens a boolean
# def check_prev(index, bead):
#     curr_bead = bead[index]
#     if curr_bead == "w":
#         curr_bead = white_bead_prev(index, bead)
#     if curr_bead == bead[index - 1] or bead[index - 1] == "w":
#         return True
#     return False
#
# #Check the next bead
# #Retuens a boolean
# def check_next(index, bead):
#     curr_bead = bead[index]
#     if curr_bead == "w":
#         curr_bead = white_bead_next(index, bead)
#     if curr_bead == bead[index + 1] or bead[index + 1] == "w":
#         return true
#     return false
#
# def white_bead_prev(index, bead):
#     if bead[index] == "w":
#         return white_bead_prev(index + 1, bead)
#     else:
#         return bead[index]
#
# def white_bead_next(index, bead):
#     if bead[index] == "w":
#         return white_bead_next(index - 1, bead)
#     else:
#         return bead[index]
#
# for i in range(len(beads)):
#     if beads[i] != beads[i-1]:
#         if beads[i] == "r":
#             lengths["r"] += 1
#             j = i
#             while check_next(j, beads):
#                 lengths["r"] += 1
