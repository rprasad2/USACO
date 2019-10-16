"""
ID: mail4rp1
LANG: PYTHON3
TASK: milk2
"""

# ***************** NEED TO FIND: *******************
# - The longest time interval at least one cow was milked.
# - The longest time interval (after milking starts) during which no cows were being milked.

with open("milk2.in") as f:
    lines = [line.strip() for line in f.readlines()]

num_cows = int(lines[0])

times = []

for i in range (num_cows):
    nums = tuple([int(n) for n in lines[i + 1].split(" ")])
    times.append(nums)
start = 1000000
end = 0
for time in times:
    if time[0] < start:
        start = time[0]
    if time[1] > end:
        end = time[1]

# print(times)
# print("start :", start)
# print("end :", end)

check = {}


longest_idle = 0
longest_milking = 0

current_milking = 0
current_idle = 0
for second in range(start, end):
    check[second] = False

    for time in times:
        if second >= time[0] and second < time[1]:
            check[second] = True

    # ******************************************************************



    milking = check[second]
    if milking:
        current_milking += 1
        if current_milking > longest_milking:
            longest_milking = current_milking
        current_idle = 0
    else:
        current_idle += 1
        if current_idle > longest_idle:
            longest_idle = current_idle
        current_milking = 0
# 11111111111111111111000000000000111111000000000011111100000000000111111111111111111111111111

with open("milk2.out", "w") as f:
    f.write(str(longest_milking) + ' ' + str(longest_idle))
    f.write("\n")
# times = [
#     (300, 1000), # cow 1
#     (700, 1200), # cow 2
#     (1500, 2100) # cow 3
# ]


# # returns list of lists of start and end milking times
# def readInput():
#     fin = open("milk2.in")
#     data = fin.readlines()
#     fin.close()
#
#     times = []
#     for i in range(1,len(data)):
#         times.append([int(data[i].split()[0]), int(data[i].split()[1])])
#     return times
#
# # returns dictionary of times when milking was active
# def createDict(times):
#     # find earliest and latest time
#     earliestTime = 1000000
#     latestTime = 0
#     for time in times:
#         if time[0] < earliestTime:
#             earliestTime = time[0]
#         if time[1] > latestTime:
#             latestTime = time[1]
#
#     # set up dictionary of milking times
#     milkTimes = {}
#     for i in range(earliestTime, latestTime):
#         milkTimes[i] = False
#
#     # fill dictionary based on when milking was active
#     for time in times:
#         startTime = time[0]
#         endTime = time[1]
#         for i in range(startTime, endTime):
#             milkTimes[i] = True
#
#     return milkTimes, earliestTime, latestTime
#
# # returns longest consecutive milking and non-milking times
# def calcTimes(milkTimes, earliestTime, latestTime):
#     longestMilkTime = 0
#     currentMilkTime = 0
#     longestNoMilkTime = 0
#     currentNoMilkTime = 0
#     for key in range(earliestTime, latestTime):
#         if milkTimes[key]:
#             currentMilkTime += 1
#             if currentMilkTime > longestMilkTime:
#                 longestMilkTime = currentMilkTime
#             currentNoMilkTime = 0
#         else:
#             currentNoMilkTime += 1
#             if currentNoMilkTime > longestNoMilkTime:
#                 longestNoMilkTime = currentNoMilkTime
#             currentMilkTime = 0
#
#     return longestMilkTime, longestNoMilkTime
#
# # writes output
# def writeOutput(longestMilkTime, longestNoMilkTime):
#     fout = open("milk2.out","w")
#     fout.write(str(longestMilkTime) + " " + str(longestNoMilkTime) + "\n")
#     fout.close()
#
# times = readInput()
# milkTimes, earliestTime, latestTime = createDict(times)
#longestMilkTime, longestNoMilkTime = calcTimes(milkTimes, earliestTime, latestTime)
# writeOutput(longestMilkTime, longestNoMilkTime)
