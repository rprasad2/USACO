"""
ID: mail4rp1
LANG: PYTHON3
TASK: milk
"""

with open("milk.in") as f:
    lines = [line.strip() for line in f.readlines()]
    milk_wanted = int(lines[0].split(' ')[0])
    num_sellers = int(lines[0].split(' ')[1])
    sellers = {
    }

for i in range(1, num_sellers + 1):
    parts = [int(num) for num in lines[i].split(' ')] # ["5", "20"] -> [5, 20]
    if parts[0] in sellers:
        sellers[parts[0]] += parts[1]
    else:
        sellers[parts[0]] = parts[1]

keys = sorted(sellers.keys())


total_cost = 0
milk_bought = 0

i = 0
while milk_bought != milk_wanted:
    if sellers[keys[i]] == 0:
        i+= 1
    else:
        sellers[keys[i]] -= 1
        milk_bought+= 1
        total_cost += keys[i]

with open('milk.out', 'w') as f:
    f.write(str(total_cost) + '\n')






def readInput():
    f = open("milk.in")
    text = f.readlines()
    f.close()

    numUnits = int(text[0].split()[0])
    numFarmers = int(text[0].split()[1])

    # create dictionary where keys are prices and values are lists of numUnits
    farmers = {}
    for i in range(1,len(text)):
        price = int(text[i].split()[0])
        units = int(text[i].split()[1])

        if price in farmers:
            farmers[price].append(units)
        else:
            farmers[price] = [units]

    return farmers, numUnits

def calcTotalPrice(farmers, numUnits):
    # loop through sorted dictionary until numUnits is reached
    totalUnits = 0
    totalPrice = 0

    for price in sorted(farmers.keys()):
        # calculate number of units offered at this price
        units = 0
        for i in farmers[price]:
            units += i

        # check if units remaining is less than units this farmer offers
        # if so, only buy as many units as needed, otherwise buy all
        remainingUnits = numUnits - totalUnits
        if remainingUnits < units:
            totalPrice += remainingUnits * price
            break
        else:
            totalUnits += units
            totalPrice += units*price

    return totalPrice
