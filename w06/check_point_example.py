# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def main():
    print("This program computes the fuel efficiency")
    print("of your vehicle in miles per gallon.")

    prev_odom = float(input("Enter the previous odometer reading in miles: "))
    curr_odom = float(input("Enter the current odometer reading in miles: "))
    fuel_amount = float(input("Enter the amount of fuel in U.S. gallons: "))

    """
    texting formula 
    1st odometer reading : 1030 miles
    2nd odometer reading : 2010 miles
    fuel amount : 30 gallons

    miles per gallon = (2010 - 1030) / 30 = 32.67

    """


    # bug was here with the placement of the parmeters
    # efficiency = miles_per_gallon(fuel_amount, prev_odom, curr_odom)
    efficiency = miles_per_gallon(prev_odom, curr_odom, fuel_amount)
    

    print(f"{efficiency:.2f} miles per gallon")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """

    # not the correct formula
    distance = end_miles - start_miles
    mpg = distance / amount_gallons

    # debugger corrections based on tutor



    return mpg


# If this file was executed like this:
# > python example.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
