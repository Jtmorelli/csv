import csv
from datetime import datetime
from matplotlib import pyplot as plt

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# print(header_row_sitka)

for index, coloumn_header in enumerate(header_row):
    print(index, coloumn_header)

date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")
name_index = header_row.index("NAME")

highs = []
lows = []
dates = []
location1 = []


for row in csv_file:
    if not location1:
        location1 = str(row[name_index])
        print(location1)
    try:
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        high = int(row[high_index])
        low = int(row[low_index])

    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.title(location1, fontsize=16)


open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)

for index, coloumn_header2 in enumerate(header_row2):
    print(index, coloumn_header2)

date_index = header_row2.index("DATE")
high_index = header_row2.index("TMAX")
low_index = header_row2.index("TMIN")
name_index = header_row2.index("NAME")

highs2 = []
lows2 = []
dates2 = []
location2 = []

for row in csv_file2:
    if not location2:
        location2 = str(row[name_index])
        print(location2)
    try:
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        high = int(row[high_index])
        low = int(row[low_index])

    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)

# print(highs)
# print(lows)
# print(dates)


plt.plot(dates2, highs2, c="red")
plt.plot(dates2, lows2, c="blue")

plt.title(location2, fontsize=16)


plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title(location1)

plt.subplot(2, 1, 2)
plt.plot(dates2, highs2, c="red")
plt.plot(dates2, lows2, c="blue")
plt.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
plt.title(location2)

plt.suptitle(
    "Tempature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

fig.autofmt_xdate()


plt.show()
