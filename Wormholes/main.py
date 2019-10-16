"""
ID: mail4rp1
LANG: PYTHON3
TASK: wormhole
"""

with open("wormhole.in") as f:
    lines = [line.strip() for line in f.readlines()]

wormholes = []
num_wormholes = int(lines[0])


for i in range(num_wormholes):
    coord = tuple(int(x) for x in lines[i + 1].split())
    wormholes.append(coord)

print(wormholes)

pairings = []
j = 0
if len(wormholes) < 5:
    for check in wormholes:
        y_coord = check[1]
        i = 0
        for wormhole in wormholes:
            if wormhole[1] == y_coord and wormhole[0] > check[0] :

                pairings.append((j,i))

            i += 1
        j += 1
# else:
#     combinatinations = []
#     for wormhole in wormholes:



print(pairings)
num_pairings = len(pairings)

with open("wormhole.out", 'w') as f:
    f.write(str(num_pairings) + '\n')
