"""
ID: mail4rp1
LANG: PYTHON3
TASK: gift1
"""
with open("gift1.in") as f:
    lines = [line.strip() for line in f.readlines()]

num_people = int(lines[0])

people = {}

for i in range(num_people):
    name = lines[i + 1]
    people[name] = 0

index = num_people + 1

#>>dave
#  200 3
#  laura
#  owen
#  vick

while index < len(lines):
    giver_name = lines[index]
    money = int(lines[index+1].split(" ")[0])

    num_receivers = int(lines[index+1].split(" ")[1])
    # print("%s is giving %d to %d people:" % (giver_name, money, num_receivers))

    if num_receivers == 0:
        pass
    else:
        receiver_money = int(money/num_receivers)
        # print("Recipients are actually getting", receiver_money)

        left_over = money % num_receivers
        people[giver_name] += left_over # left over
        people[giver_name] -= money

        # print(giver_name, "is keeping", left_over)
        for i in range(num_receivers):
            receiver = lines[index + i + 2]
            people[receiver] += receiver_money
    index += num_receivers + 2

# dave 302
# laura 66
# owen -359
# vick 141
# amr -150

#{'dave': 302, 'laura': 0, 'owen': -425, 'vick': 141, 'amr': -150}

with open("gift1.out", "w") as f:
    for name, balance in people.items():
        f.write(name + " " + str(balance) + "\n")
