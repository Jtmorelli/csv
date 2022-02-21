# using the datetime module


import csv
from datetime import datetime

weather = open("sitka_weather_07-2018_simple.csv", "r")

weather_file = csv.reader(weather, delimiter=",")

header_row = next(weather_file)

# print(type(header_row))

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header)

highs = []
dates = []

test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(test_date)


for row in weather_file:
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)

print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")

plt.title("Daily high tempatures, July 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Tempatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
