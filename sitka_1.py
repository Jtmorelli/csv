import csv

weather = open("sitka_weather_07-2018_simple.csv", "r")

weather_file = csv.reader(weather, delimiter=",")

header_row = next(weather_file)

print(type(header_row))

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header)

highs = []

for row in weather_file:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")

plt.title("Daily high tempatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Tempatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
