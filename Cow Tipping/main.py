with open('cowtip.in') as f:
    lines = [line.strip() for line in f.readlines()]
    rows = int(lines[0])

array = []
for i in range(rows):
    array.append([int(x) for x in lines[i + 1]])

def display_array(array):
    return
    for line in array:
        print(line)
    print()

display_array(array)

def change_value(x,y):
    global array
    if array[x][y] == 0:
        array[x][y] = 1
    else:
        array[x][y] = 0

def flip(x,y):
    for i in range(x + 1):
        for j in range(y + 1):
            change_value(i,j)

num_flip = 0
for i in range(rows - 1, -1, -1):
    for j in range(rows - 1, -1, -1):
        if array[i][j] == 1:
            flip(i,j)
            num_flip += 1

display_array(array)

with open("cowtip.out", 'w') as f:
    f.write(str(num_flip))
