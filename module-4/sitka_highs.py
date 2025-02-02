"""
Name: Andrew Stiles
Date: 1-26-2025
Assignment: Module 4-2 Assignment (original working)
Purpose: Sitka Matplot for High and Low Temperates
Citation: N/A
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Update the file path to the full path
filename = r"C:\Users\adsti\OneDrive\Desktop\adstiles85-Github\CSD\CSD-325\module-4\sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# The rest of your plotting code remains unchanged
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()