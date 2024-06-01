"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""


import math # import math module

# t = 2π √h/9.81  formula for time
PI= math.pi
SQUARE= math.sqrt
hight= float(input("Enter the length of the pendulum in meters: ")) # length of a pendulum in meters

time = 2 * PI * SQUARE(hight/9.81)
# formula

print(f"The time taken for the pendulum to swing back and forth is {time:.2f} seconds.")

# make into a function

# import math

def pendulum_period(length):
    """
    Calculates the time period for a pendulum to swing back and forth based on its length.
    
    Args:
        length (float): The length of the pendulum in meters.
        
    Returns:
        float: The time period for the pendulum to swing back and forth in seconds.
    """
    PI = math.pi
    g = 9.81  # Acceleration due to gravity (m/s^2)
    
    time_period = 2 * PI * math.sqrt(length / g)
    
    return time_period

# Prompt the user for the pendulum length
pendulum_length = float(input("Enter the length of the pendulum in meters: "))

# Calculate the time period
period = pendulum_period(pendulum_length)

# Print the result
print(f"The time taken for the pendulum to swing back and forth is {period:.2f} seconds.")