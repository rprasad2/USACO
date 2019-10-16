with open("square.in") as f:
    lines = [line.strip() for line in f.readlines()]
    print("lines:", lines)
    print()
    rect1 = [int(c) for c in lines[0].split()]
    rect2 = [int(c) for c in lines[1].split()]


print("This is rect 1:", rect1, "\nThis is rect 2:", rect2)

maxx = max(rect1[0],rect1[2],rect2[0],rect2[2])
minx = min(rect1[0],rect1[2],rect2[0],rect2[2])
maxy = max(rect1[1],rect1[3],rect2[1],rect2[3])
miny = min(rect1[1],rect1[3],rect2[1],rect2[3])
disty = maxy-miny
distx = maxx-minx

if distx > disty:
    area = distx ** 2
else:
    area = disty ** 2

with open("square.out", "w") as f:
    f.write(str(area))
