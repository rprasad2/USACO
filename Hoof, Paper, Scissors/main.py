with open("hps.in") as f:
    lines = [line.strip() for line in f.readlines()]
    num_entries = int(lines[0])

entries = []
for i in range(1, num_entries + 1):
    entries.append((int(lines[i].split()[0]), int(lines[i].split()[1])))

most_wins = 0
forward_wins = 0
backword_wins = 0
for entry in entries:
    cow1 = entry[0]
    cow2 = entry[1]
    if cow1 == 1:
        if cow2 == 2:
            forward_wins += 1
        elif cow2 == 3:
            backword_wins += 1
    elif cow1 == 2:
        if cow2 == 3:
            forward_wins += 1
        elif cow2 == 1:
            backword_wins += 1
    elif cow1 == 3:
        if cow2 == 1:
            forward_wins += 1
        elif cow2 == 2:
            backword_wins += 1

most_wins = max(forward_wins, backword_wins)

with open('hps.out', 'w') as f:
    f.write(str(most_wins) + "\n")
# http://www.usaco.org/index.php?page=viewproblem2&cpid=688

def readInput():
    f = open("hps.in")
    text = f.readlines()
    f.close()

    combos = []
    for i in range(1,len(text)):
        combo = text[i].split()
        combo = [int(x) for x in combo]
        combos.append(combo)

    return combos

def main(combos):
    # define winning combinations for each possible permutation
    # note that this doesn't have to be a dictionary, but we use one for readability
    winningCombos = {
        'hoof1paper2scissors3': [[2,1],[1,3],[3,2]],
        'hoof1scissors2paper3': [[1,2],[3,1],[2,3]],
        'paper1hoof2scissors3': [[1,2],[3,1],[2,3]],
        'paper1scissors2hoof3': [[2,1],[1,3],[3,2]],
        'scissors1paper2hoof3': [[1,2],[3,1],[2,3]],
        'scissors1hoof2paper3': [[2,1],[1,3],[3,2]]
    }

    # find max number of winning combinations
    maxWins = 0
    for key in winningCombos:
        winningPairs = winningCombos[key]
        numWins = 0
        for combo in combos:
            if combo in winningPairs:
                numWins += 1
        if numWins > maxWins:
            maxWins = numWins

    return maxWins

def writeOutput(maxWins):
    f = open("hps.out","w")
    f.write(str(maxWins) + "\n")
    f.close()

combos = readInput()
maxWins = main(combos)
writeOutput(maxWins) 
