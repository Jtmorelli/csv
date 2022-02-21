# change to all 2018 data
# change title to daily low and high tempatures - 2018
# extract low temps
# shade in are between low and high


import csv
from datetime import datetime

weather = open("sitka_weather_2018_simple.csv", "r")

weather_file = csv.reader(weather, delimiter=",")

header_row = next(weather_file)

# print(type(header_row))

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header)

highs = []
lows = []
dates = []

test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(test_date)


for row in weather_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
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

# plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")

plt.show()
