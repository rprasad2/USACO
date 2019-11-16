
import random
import math
import copy
checkerboard = [[],[],[],[],[],[],[],[]]
for i in range(len(checkerboard)):
    for j in range(8):
        checkerboard[i].append(random.randint(0,1))
def create_visual(grid):
    print('\n',"----- "*8)
    for row in grid:
        print('|', end= '')
        for value in row:
            if value == 0:
                print('  H  |', end = '')
            else:
                print('     |', end = '')

        print('\n',"----- "*8)
create_visual(checkerboard)

goal = (random.randint(0,7),random.randint(0,7))

def point_to_index(x, y):
    return x * 8 + y

def point_to_binary(x, y):
    return bin(point_to_index(x, y))[2:].rjust(6,'0')

binary_goal = point_to_binary(goal[0], goal[1])

print("The coin you want is number: ", point_to_index(goal[0], goal[1]))
coordinate = [int(x) - 1 for x in input("What is the coordinate of the coin you want to flip, enter it as a coordinate pair X,Y: ").split(',')]
coordinate = [coordinate[-1],coordinate[0]]


def check_value(checkerboard):
    checkerboard_value = ""
    num = [0,0,0,0,0,0]
    for i in range(len(checkerboard)):
        for j in range(len(checkerboard)):
            if j %2 == 0:
                if checkerboard[i][j] == 0:
                    num[0] += 1
            if j < 2 or (j > 3 and j < 6):
                if checkerboard[i][j] == 0:
                    num[1] += 1
            if j < 4:
                if checkerboard[i][j] == 0:
                    num[2] += 1
            if i %2 == 0:
                if checkerboard[i][j] == 0:
                    num[3] += 1
            if i < 2 or (i > 3 and i < 6):
                if checkerboard[i][j] == 0:
                    num[4] += 1
            if i < 4:
                if checkerboard[i][j] == 0:
                    num[5] += 1
    for value in num:
        checkerboard_value += "1" if value % 2 == 0 else "0"

    return checkerboard_value


print("Original checkerboard value", check_value(checkerboard))
og_checkerboard_value =check_value(checkerboard)

new_checkerboard = copy.deepcopy(checkerboard)
if new_checkerboard[coordinate[0]][coordinate[1]] == 0:
    new_checkerboard[coordinate[0]][coordinate[1]] = 1
else:
    new_checkerboard[coordinate[0]][coordinate[1]] = 0

create_visual(new_checkerboard)
print("New checkerboard value", check_value(new_checkerboard))

print("binary goal", binary_goal)

def same(x,y):
    if x == y:
        return True
    else:
        return False

def flip(x,y):
    global checkerboard
    if checkerboard[x][y] == 0:
        checkerboard[x][y] = 1
    else:
        checkerboard[x][y] = 0



if same(check_value(new_checkerboard),binary_goal):
    print("Good Job!")
else:
    i = 0
    j = 0
    while not same(check_value(checkerboard),binary_goal):
        flip(i,j)
        if same(check_value(checkerboard),binary_goal):
            break
        else:
            flip(i,j)
        if j == 7:
            i += 1
            j = 0
        elif i == 7 and j == 7:
            print("You messed up")
        else:
            j += 1


    print("The checkerboard value you wanted to change was", (i * 8 + j + 1))
    print("That numbers binary value is", bin(i * 8 + j + 1)[2:].rjust(6,'0'))
    print("Original Value", og_checkerboard_value)
