# I would like to learn more about logical operators and shorthand operators, can you please add some examples to the cheat sheet. Make sure to add code comments explaining what everything is and/or what is happening.

# Logical Operators
# and operator
result = True and True   # True
result = True and False  # False
result = False and True  # False
result = False and False # False

# or operator
result = True or True    # True
result = True or False   # True
result = False or True   # True
result = False or False  # False

# not operator
result = not True        # False
result = not False       # True

# Shorthand Operators
# Assignment operators
x = 5       # x = 5
x += 3      # x = x + 3 (x becomes 8)
x -= 2      # x = x - 2 (x becomes 6)
x *= 4      # x = x * 4 (x becomes 24)
x /= 2      # x = x / 2 (x becomes 12.0)
x %= 3      # x = x % 3 (x becomes 0)
x **= 2     # x = x ** 2 (x becomes 0)
x //= 3     # x = x // 3 (x becomes 0)

# Increment and decrement operators
x = 5
x += 1      # x = x + 1 (x becomes 6)
x -= 1      # x = x - 1 (x becomes 5)

# Conditional expressions (ternary operator)
age = 18
is_adult = "Yes" if age >= 18 else "No"  # is_adult becomes "Yes"

# Logical operators with assignment
# and operator
x = 5
y = 10
# x and= y    # x = x and y (x becomes 10)

# or operator
x = 5
y = 0
# x or= y     # x = x or y (x becomes 5)