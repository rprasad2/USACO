import math

with open("notlast.in") as f:
    lines = [line.strip() for line in f.readlines()]
    num_entries = int(lines[0])


cows_milk = {}
for i in range(1, num_entries + 1):
    line = lines[i].split()
    if line[0] not in cows_milk:
        cows_milk[line[0]] = int(line[1])
    else:
        cows_milk[line[0]] += int(line[1])
# # print("How much milk each cow produces", cows_milk)
#
# lowest = 101
# for name in cows_milk:
#     if len(cows_milk.keys()) != 7:
#         lowest = 0
#     else:
#         lowest = cows_milk[name] if (cows_milk[name] < lowest) else lowest
#
# # print("The lowest amount of milk produced", lowest)
#
# second_lowest = float('inf')
# for name in cows_milk:
#     second_lowest = cows_milk[name] if (cows_milk[name] > lowest and cows_milk[name] < second_lowest) else second_lowest
#
# # print("The second lowest amount of milk produced", second_lowest)
#
# with open('notlast.out', 'w') as f:
#     total_sec_lowest = 0
#     for name in cows_milk:
#         if cows_milk[name] == second_lowest:
#             total_sec_lowest += 1
#     if total_sec_lowest > 1 or total_sec_lowest == 0:
#         f.write("Tie")
#     else:
#         for name in cows_milk:
#             if cows_milk[name] == second_lowest:
#                 f.write(name)


sorted_cows_milk = sorted(cows_milk.items(), key = lambda x:x[1])
lowest = sorted_cows_milk[0][1]

winner = "Tie"
if len(sorted_cows_milk) == 7:
    # find second lowest
    second_lowest_index = 0
    for i in range(len(sorted_cows_milk)):
        if sorted_cows_milk[i][1] > sorted_cows_milk[second_lowest_index][1]:
            second_lowest_index = i
            break

    if second_lowest_index < len(sorted_cows_milk) - 2:
        if sorted_cows_milk[second_lowest_index][1] != sorted_cows_milk[second_lowest_index + 1][1]:
            winner = sorted_cows_milk[second_lowest_index][0]

elif len(sorted_cows_milk) == 1:
    winner = sorted_cows_milk[0][0]
elif sorted_cows_milk[0][1] != sorted_cows_milk[1][1]:
    winner = sorted_cows_milk[0][0]


with open('notlast.out', 'w') as f:
    f.write(winner + '\n')
