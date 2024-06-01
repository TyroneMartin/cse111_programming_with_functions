
import math
# The math.ceil() function rounds a number up to the nearest integer that is greater than or equal to a number.

"""
# prompt the user to enter the number of boxes

number_of_items_manufactured = int(input("Enter the number of items manufactured: "))
items_per_box = int(input("Enter the number of items per box: "))
number_of_items_in_boxes = math.ceil(number_of_items_manufactured / items_per_box)

print(f"For {number_of_items_manufactured} items. The number of boxes required is: {number_of_items_in_boxes}")
"""

# Improved version with IA

# Prompt the user to enter the number of items manufactured
while True:
    try:
        number_of_items_manufactured = int(input("Enter the number of items manufactured: "))
        if number_of_items_manufactured <= 0:
            raise ValueError("Number of items must be a positive integer.")
        break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.")

# Prompt the user to enter the number of items per box
while True:
    try:
        items_per_box = int(input("Enter the number of items per box: "))
        if items_per_box <= 0:
            raise ValueError("Items per box must be a positive integer.")
        break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.")

# Calculate the number of boxes required
number_of_boxes_required = math.ceil(number_of_items_manufactured / items_per_box)

# Print the result
print(f"For {number_of_items_manufactured} items, the number of boxes required is: {number_of_boxes_required}")