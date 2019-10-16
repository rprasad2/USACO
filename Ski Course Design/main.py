"""
ID: mail4rp1
LANG: PYTHON3
TASK: skidesign
"""

# 5 20 4 1 24 21

with open("skidesign.in") as f:
    lines = [line.strip() for line in f.readlines()]
    num_hills = int(lines[0])

hills = []
for i in range(0, num_hills):
    hills.append(int(lines[i + 1]))

cost = 0

hills.sort()
new_hills = hills.copy()

while hills[-1] - 17 > hills[0]:
    for i in range(len(hills)):
        if hills[i] == hills[i - 1]:
            pass
        else:
            if hills[i] == min(hills) or hills[i] == max(hills):
                if hills[-1] - hills[i] > 17:
                    hills[i] += 1
                elif hills[i] - hills[0] > 17:
                    hills[i] -= 1
                    print(hills)
    hills.sort()

'''
def main(heights):
    # calculate the total cost for each possible interval, starting from
    # (minHeight, lowestHeight + 17) up to (minHeight - 17, maxHeight)

    minCost = 1000 * 100**2 # make sure minCost is set reasonably
    minHeight = heights[0]
    maxHeight = minHeight + 17

,

    return minCost
'''

for i in range(len(hills)):
    if hills[i] != new_hills[i]:
        cost += abs(hills[i] - new_hills[i])**2

with open("skidesign.out", 'w') as f:
   f.write(str(cost) + '\n')
