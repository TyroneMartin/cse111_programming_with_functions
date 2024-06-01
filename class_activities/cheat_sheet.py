# I would like you to create a cheat sheet document in Python that in a concise way covers the fundamentals of programming with Python. You should cover topics like data types, variables, expressions, conditionals, loops, lists, dictionaries, input/output, and reading/writing to a file. Please keep everything in one large document and add appropriate comments directly into the code explaining what everything is.

# Data Types
# Numbers (integers and floating-point numbers)
x = 5       # Integer
y = 3.14    # Float

# Strings (sequences of characters enclosed in single or double quotes)
name = "Alice"
message = 'Hello, World!'

# Booleans (True or False values)
is_student = True
is_teacher = False

# Lists (ordered collections of items)
fruits = ["apple", "banana", "cherry"]

# Tuples (immutable ordered collections of items)
point = (2, 3)

# Dictionaries (unordered collections of key-value pairs)
person = {"name": "Bob", "age": 30}

# Sets (unordered collections of unique items)
numbers = {1, 2, 3, 4, 4}  # Duplicate 4 is ignored


# Variables
# Assigning values to variables
x = 10
y = 20
name = "Alice"

# Dynamically typed (no need to declare data type)
x = 5       # x is now an integer
x = "Hello" # x is now a string


# Expressions
# Arithmetic operations
result = 2 + 3    # 5
result = 10 - 4   # 6
result = 5 * 6    # 30
result = 8 / 2    # 4.0
result = 5 % 2    # 1 (remainder)
result = 2 ** 3   # 8 (exponentiation)

# Comparison operations
is_equal = 5 == 6      # False
is_not_equal = 5 != 6  # True
is_greater = 7 > 3     # True
is_less = 7 < 3        # False
is_greater_or_equal = 7 >= 7  # True
is_less_or_equal = 7 <= 3     # False

# Logical operations
a = True
b = False
result = a and b  # False
result = a or b   # True
result = not a    # False


# Conditionals
# If statement
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")

# If-elif-else statement
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# Loops
# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Range function
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

for i in range(2, 8, 2):  # 2, 4, 6
    print(i)


# Lists
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list items
print(fruits[0])  # "apple"

# Modifying list items
fruits[0] = "orange"

# List methods
fruits.append("grape")      # ["orange", "banana", "cherry", "grape"]
fruits.remove("banana")     # ["orange", "cherry", "grape"]
fruits.pop(1)               # ["orange", "grape"]
fruits.insert(1, "kiwi")    # ["orange", "kiwi", "grape"]
fruits.sort()               # ["grape", "kiwi", "orange"]
fruits.reverse()            # ["orange", "kiwi", "grape"]
len(fruits)                 # 3


# Dictionaries
# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing dictionary values
print(person["name"])  # "Alice"

# Modifying dictionary values
person["age"] = 31

# Adding new key-value pairs
person["email"] = "alice@example.com"

# Dictionary methods
person.keys()       # dict_keys(["name", "age", "city", "email"])
person.values()     # dict_values(["Alice", 31, "New York", "alice@example.com"])
person.items()      # dict_items([("name", "Alice"), ("age", 31), ("city", "New York"), ("email", "alice@example.com")])
"name" in person    # True
len(person)         # 4


# Input/Output
# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Printing output
print("Hello,", name)
print("You are", age, "years old")


# Reading from a file
file = open("data.txt", "r")
contents = file.read()
print(contents)
file.close()

# Writing to a file
file = open("output.txt", "w")
file.write("This is a sample text.")
file.close()