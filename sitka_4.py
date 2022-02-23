# change to all 2018 data
# change title to daily low and high tempatures - 2018
# extract low temps
# shade in are between low and high


import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# print(header_row)

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header)

highs = []
lows = []
dates = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)


for row in csv_file:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])

    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

print(highs)
print(lows)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily low and high tempatures, 2018", fontsize=16)
plt.xlabel("Month in 2018")
plt.ylabel("Tempatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
