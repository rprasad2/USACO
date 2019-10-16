"""
ID: mail4rp1
LANG: PYTHON3
TASK: transform
"""

with open('transform.in') as f:
    lines = f.readlines()
    # ['3', '---', '@-@', '-@-', ...]
    # lines[0][0] -> 3

    N = int(lines[0])
    start_square = []
    check_square = []
    transformed_square = []
    for i in range(1,N+1):
        row = []
        for j in range(0, N):
            row.append(lines[i][j])
        start_square.append(row)

    for i in range(N+1,2*N+1):
        row = []
        for j in range(0, N):
            row.append(lines[i][j])
        check_square.append(row)

# Steps
# - read input shapes
# - write algorithms for transformations 1-5
# - compare input shape to transformed shapes
# - done??


# @ - @
# - - -
# @ @ -

# @ - @
# @ - -
# - - @

# [0, 0] -> [0, 2]
# [1, 1] -> [1, 1]

def rot90degree(square, times=1):
    if times > 0:
        return rot90degree(list(zip(*square[::-1])), times-1)
    else:
        return [list(t) for t in square]


    # newPattern = []
    # size = len(pattern)
    #
    # # fill newPattern with appropriate dimensions
    # for i in range(0,size):
    #     row = []
    #     for j in range(0,size):
    #         row.append('')
    #     newPattern.append(row)
    #
    # # create newPattern
    # for i in range(0,size):
    #     for j in range(0,size):
    #         newPattern[j][size-i-1] = pattern[i][j]


# [1, 2, 3][::-1]
def reflect(square):
    transformed_square = square.copy()
    # square.copy()
    # square[:]
    # list(square)
    for i in range(0, N):
        transformed_square[i] = transformed_square[i][::-1]
    return transformed_square

def print_square(square):
    for line in square:
        print(' '.join(line))
    print()

# print_square(start_square)
# print_square(check_square)
#
# print(rot90degree(start_square,1))
# print(check_square)

def check(square):
    if rot90degree(start_square) == check_square:
        return 1
    elif rot90degree(start_square,2) == check_square:
        return 2
    elif rot90degree(start_square,3) == check_square:
        return 3
    elif reflect(start_square) == check_square:
        return 4
    elif rot90degree(reflect(start_square)) == check_square:
        return 5
    elif rot90degree(reflect(start_square),2) == check_square:
        return 5
    elif rot90degree(reflect(start_square),3) == check_square:
        return 5
    elif start_square == check_square:
        return 6
    else:
        return 7

with open('transform.out', 'w') as f:
    f.write(str(check(start_square)) + '\n')
