"""
ID: mail4rp1
LANG: PYTHON3
TASK: barn1
"""

with open('barn1.in') as f:
    lines = [line.strip() for line in f.readlines()]
    max_boards = int(lines[0].split(' ')[0])
    stalls = int(lines[0].split(' ')[1])
    num_cows = int(lines[0].split(' ')[2])

stalls_with_cows = []

for i in range(1, num_cows + 1):
    stalls_with_cows.append(int(lines[i]))

stalls_with_cows = sorted(stalls_with_cows)
stalls_boarded = num_cows

gaps = []

# the farmer can leave the N largest gaps uncovered, where N = numBoards - 1
# thus, calculate the total length of the N largest gaps

for i in range(0, num_cows - 1):
    if stalls_with_cows[i+1] - stalls_with_cows[i] > 1:
        gaps.append(stalls_with_cows[i+1] - stalls_with_cows[i] - 1)

while len(gaps) > max_boards - 1:
    stalls_boarded += min(gaps)
    gaps.remove(min(gaps))

with open('barn1.out', 'w') as f:
    f.write(str(stalls_boarded) + '\n')









# -----------------------------------


def readInput():
    f = open("barn1.in")
    text = f.readlines()
    f.close()

    numBoards = int(text[0].split()[0])

    # create list of sorted stall numbers that are occupied
    occupiedStalls = []
    for i in range(1,len(text)):
        occupiedStalls.append(int(text[i]))

    return sorted(occupiedStalls), numBoards

# creates list of lengths of gaps between the occupied stalls
def calcGapLengths(occupiedStalls):
    gapLengths = []
    gapLength = 0
    prevStallNum = occupiedStalls[0]

    for i in range(1,len(occupiedStalls)):
        gapLengths.append(occupiedStalls[i]-prevStallNum-1)
        prevStallNum = occupiedStalls[i]

    return gapLengths

def calcNumStallsBlocked(occupiedStalls, gapLengths, numBoards):
    # the farmer can leave the N largest gaps uncovered, where N = numBoards - 1
    # thus, calculate the total length of the N largest gaps
    totalGapLength = 0
    gapLengths = sorted(gapLengths, reverse=True)

    for i in range(0,numBoards-1):
        # if there are more boards than gaps, break
        if i >= len(gapLengths):
            break
        totalGapLength += gapLengths[i]

    # the number of stalls blocked is then:
    maxStallNum = occupiedStalls[-1]
    minStallNum = occupiedStalls[0]
    numBlocked = maxStallNum-minStallNum+1-totalGapLength

    return numBlocked

def writeOutput(numBlocked):
    f = open("barn1.out", "w")
    f.write(str(numBlocked) + "\n")
    f.close()

occupiedStalls,numBoards = readInput()
gapLengths = calcGapLengths(occupiedStalls)
numBlocked = calcNumStallsBlocked(occupiedStalls, gapLengths, numBoards)
writeOutput(numBlocked)
