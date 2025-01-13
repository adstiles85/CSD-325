"""
Name: Andrew Stiles
Date: 1-12-2025
Assignment: Module 1.3 Assignment
Purpose: This program mimics the "99 Bottles of Beer" countdown song.
Citation: N/A
"""

# Create function that counts down bottles
def countdown_bottles(n):
    while n > 0:
        if n > 1:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            print(f"Take one down and pass it around, {n - 1} bottle{'s' if n - 1 > 1 else ''} of beer on the wall.\n")
        else:
            print(f"{n} bottle of beer on the wall, {n} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        n -= 1

# Create main with number input feature
def main():
    print("Welcome to the 'Bottles of Beer' countdown program!")
    while True:
        try:
            bottles = int(input("Enter number of bottles: "))
            if bottles <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Start the countdown
    print("\nStarting the countdown...")
    countdown_bottles(bottles)
    print("Time to buy more bottles of beer!")

# Run the main program
if __name__ == "__main__":
    main()
