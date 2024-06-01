"""
Nmae: fuel_usage.py
Author: Tyron Martin
Date: 05/03/2023
Purpose: Create a program that calculates Fuel Usage/Mileage/Odometer Reading
"""

"""
Many vehicle owners record the fuel efficiency of their vehicles as a way to track the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, there is probably something wrong with the engine or drive train of the vehicle. In the United States, fuel efficiency for gasoline powered vehicles is calculated as miles per gallon. In most other countries, fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

mpg = end − start / gallons

he formula for converting miles per gallon to liters per 100 kilometers is the following:

lp100k =  235.215 / mpg(miles per gallon)
"""


# ask user 

starting_miles = float(input("Enter the starting odometer reading (miles): "))
ending_miles = float(input("Enter the ending odometer reading (miles): "))
fuel = float(input("Enter the amount of fuel consumed in gallons: "))

# calculate miles per gallon
mpg = (ending_miles - starting_miles) / fuel
# convert miles per gallon to liters per 100 kilometers
lp100k = 235.215 / mpg
print(f"The fuel efficiency is {mpg:.1f} miles per gallon. and {lp100k:.2f} liters per 100 kilometers.")