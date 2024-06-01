"""
01 Prove Milestone: Review Python

Problem Statement
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = π w^2 (aw a + 2,540 d) / 10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
If you’re curious about how the above formula was derived, you can read the tire volume formula derivation.

"""

import math
PI = math.pi

# Prompt the user for the tire width, aspect ratio, and wheel diameter
w = float(input("Enter the width of the tire in mm (e.g. 205): "))
a = float(input("Enter the aspect ratio of the tire (e.g. 60): "))
d = float(input("Enter the diameter of the wheel in inches (e.g. 15): "))

volume = (PI * (w**2) * (a * (w * a + 2540 * d))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")


# make into a function
# def tire_volume(w, a, d):
#     volume = (PI * (w**2) * (a * (w * a + 2540 * d))) / 10000000000
#     return volume

# w = float(input("Enter the width of the tire in mm (e.g. 205): "))
# a = float(input("Enter the aspect ratio of the tire (e.g. 60): "))
# d = float(input("Enter the diameter of the wheel in inches (e.g. 15): "))

# volume = tire_volume(w, a, d)

# print(f"The approximate volume is {volume:.2f} liters.")
