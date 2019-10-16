"""
ID: mail4rp1
LANG: PYTHON3
TASK: ride
"""
with open("ride.in") as f:
    lines = [line.strip() for line in f.readlines()]
    print("lines:", lines)
    print()
    UFO = lines[0].upper()
    name = lines[1].upper()

# ord('z') will give you the character code (ASCII number) of a character
arr_UFO = [ord(l) - 64 for l in UFO]
arr_name = [ord(l) - 64 for l in name]
print(arr_UFO)

UFO_val = 1
name_val = 1

for i in arr_UFO:
    UFO_val *= i
for i in arr_name:
    name_val *= i
print(UFO_val)
print(name_val)

with open("ride.out", "w") as f:
    f.write("GO" if (UFO_val % 47) == (name_val % 47) else "STAY")
    f.write("\n")
