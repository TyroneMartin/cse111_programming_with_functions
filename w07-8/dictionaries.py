# Dictionaries are key-value pairs, in js they are objects

# Define a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}

# Accessing values
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York
print(person["email"]) # Output: alice@example.com

# Modifying values
person["age"] = 31
print(person["age"])  # Output: 31

# Adding a new key-value pair
person["phone"] = "123-456-7890"
print(person["phone"])  # Output: 123-456-7890

# Deleting a key-value pair
del person["email"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'phone': '123-456-7890'}

# Checking if a key exists
if "name" in person:
    print("Name is present.")  # Output: Name is present.

# Iterating through keys
for key in person:
    print(key, person[key])

# Output:
# name Alice
# age 31
# city New York
# phone 123-456-7890

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 31
# city: New York
# phone: 123-456-7890

# Getting a value with a default if the key doesn't exist
print(person.get("email", "Email not provided"))  # Output: Email not provided

# Getting all keys
print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'phone'])

# Getting all values
print(person.values())  # Output: dict_values(['Alice', 31, 'New York', '123-456-7890'])

# Getting all key-value pairs
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('phone', '123-456-7890')])

# Merging dictionaries
additional_info = {"hobby": "Reading", "pet": "Cat"}
person.update(additional_info)
print(person)

# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'phone': '123-456-7890', 'hobby': 'Reading', 'pet': 'Cat'}

# Creating a dictionary from two lists
keys = ["fruit", "color", "quantity"]
values = ["apple", "red", 5]
dictionary_from_lists = dict(zip(keys, values))
print(dictionary_from_lists)  # Output: {'fruit': 'apple', 'color': 'red', 'quantity': 5}

# Clearing a dictionary
person.clear()
print(person)  # Output: {}
