"""
ID: mail4rp1
LANG: PYTHON3
TASK: friday
"""
with open("friday.in") as f:
    lines = [line.strip() for line in f.readlines()]
    print("lines:", lines)
    print()
    years = int(lines[0])
months = {
    0:31,
    1:28,
    2:31,
    3:30,
    4:31,
    5:30,
    6:31,
    7:31,
    8:30,
    9:31,
    10:30,
    11:31
}
days = {
    0: 0, #Saturday
    1: 0, #Sunday
    2: 0, #Monday
    3: 0, #Tuesday
    4: 0, #Wednesday
    5: 0, #Thursday
    6: 0  #Friday
}
leap_year_count = 0
start_day_of_week = 2 # Starting on Monday since Jan 1, 1900 is Monday
for year in range(0, years):
    year += 1900
    for month, num_of_days in months.items():
        # Check if year is leap year
        print("Year:", year)
        if month == 1 and year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    num_of_days = 29
                    print("Century leap year!")
                    leap_year_count += 1
            else:
                print("Normal leap year!")
                num_of_days = 29
                leap_year_count += 1

        for day in range(0, num_of_days):
            day_of_week = (start_day_of_week + day) % 7
            if day == 12: # If day is the 13th
                days[day_of_week] += 1
        start_day_of_week = (start_day_of_week + num_of_days) % 7

print("# of leap years", leap_year_count)

#print(days)
with open("friday.out", "w") as f:
    f.write(str(days[0]) + " " + str(days[1]) + " " + str(days[2]) + " " + str(days[3]) + " " + str(days[4]) + " " + str(days[5]) + " " + str(days[6]))

    # " ".join(days.values())
    f.write("\n")
