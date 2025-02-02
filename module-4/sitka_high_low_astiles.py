"""
Name: Andrew Stiles
Date: 1-26-2025
Assignment: Module 4-2 Assignment
Purpose: Sitka Matplot for High and Low Temperatures
Citation: N/A
"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

# Direct path to local file
filename = r"C:\Users\adsti\OneDrive\Desktop\adstiles85-Github\CSD\CSD-325\module-4\sitka_weather_2018_simple.csv"

# Read the CSV file and extract dates, highs, and lows
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Initialize lists for dates, highs, and lows
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

# Function to plot temperatures
def plot_temperatures(dates, temps, label, color):
    plt.style.use('ggplot')  # Use ggplot style
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Main Program Loop
while True:
    # Display menu
    print("\nWelcome to the Sitka Weather Temperature Viewer!")
    print("Select an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        # Plot High Temps
        plot_temperatures(dates, highs, "High", "red")
    elif choice == '2':
        # Plot Low Temps
        plot_temperatures(dates, lows, "Low", "blue")
    elif choice == '3':
        # Exit the program
        print("Thank you for using the Sitka Weather Temperature Viewer! Goodbye!")
        sys.exit()
    else:
        # Invalid input
        print("Invalid choice. Please enter 1, 2, or 3.")
