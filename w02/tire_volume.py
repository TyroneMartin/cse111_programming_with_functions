"""
Name: Tyrone Martin
Class: CSE 111
Date: 05/03/2024

"""
from datetime import datetime
import math
PI = math.pi
# Call the now() method to get the current time from the computer's operating system
current_date_and_time = datetime.now()

# Open a text file named "volumes.txt" in append mode
with open("volumes.txt", "at") as volumes_file:
    # Write the current date as a title
    volumes_file.write(f"\nGenerated on: {current_date_and_time.strftime('%Y-%m-%d')}\n")
    volumes_file.write("1. Width of the tire\n")
    volumes_file.write("2. Aspect ratio of the tire\n")
    volumes_file.write("3. Diameter of the wheel\n")
    volumes_file.write("4. Volume of the tire\n\n")

    while True:
        w = float(input("Enter the width of the tire in mm (e.g. 205): "))
        a = float(input("Enter the aspect ratio of the tire (e.g. 60): "))
        d = float(input("Enter the diameter of the wheel in inches (e.g. 15): "))

        def tire_volume(w, a, d):
            volume = (PI * (w**2) * (a * (w * a + 2540 * d))) / 10000000000
            return volume

        volume = tire_volume(w, a, d)
        print(f"The approximate volume is {volume:.2f} liters.")

        # Write the customer's responses and the calculated volume to the file
        volumes_file.write(f"{w}, {a}, {d}, {volume:.2f}\n")

        # Ask the user if they want to continue or exit
        choice = input("Do you want to continue (y/n)? ").lower()
        if choice != 'y':
            break