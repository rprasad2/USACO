with open('crossroad.in') as f:
    lines = [line.strip() for line in f.readlines()]
    num_entries = int(lines[0])

side_of_road = {}

crossroad = 0
for i in range(num_entries):
    cow_num, side = [int(x) for x in lines[i + 1].split()]
    if cow_num not in side_of_road:
        side_of_road[cow_num] = side
    elif side_of_road[cow_num] != side:
        crossroad += 1
        side_of_road[cow_num] = side

with open('crossroad.out', 'w') as f:
    f.write(str(crossroad) + "\n")
