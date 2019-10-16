with open('cowsignal.in') as f:
    lines = [line.strip() for line in f.readlines()]

    # Read in M, N, and K
    values =  lines[0].split()
    M =  int(values[0])
    N = int(values[1])
    K = int(values[2])

    # Read in the figure

#0   3 3 2
#1   #.#
#2   .#.
#3   #.#

# ##..##
# ##..##
# ..##..
# ..##..
# ##..##
# ##..##
signal = []
for i in range(1, M+1):
    signal.append(lines[i])

new_signal = []

# for line in signal:
#     new_line = ""
#     for c in line:
#         for i in range(K):
#             # ... build up line
#             new_line += c


for sign in signal:
    new_line = ""
    for symbol in sign:
        for j in range(K):
            new_line += symbol

    for i in range(K):
        new_signal.append(new_line)


with open('cowsignal.out', 'w') as f:
    for line in new_signal:
        f.write(line + '\n')
