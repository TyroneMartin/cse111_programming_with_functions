# In Python, a list is an ordered collection of items.
# In JavaScript, a similar structure is called an array.

# Sample lists
names = ["John", "Paul", "George", "Ringo"]
scores = [100, 99, 98, 97]

# Accessing list elements
print(names[0])  # Output: John
print(scores[0])  # Output: 100
print(names[0] + " " + names[1])  # Output: John Paul

# Modifying lists
scores.append(96)  # Adds 96 to the end of the scores list

# Performing operations on lists
print(scores[0] + scores[1] + scores[2] + scores[3] + scores[4])  # Sum of scores elements
print(sum(scores))  # Using sum function to get the total of scores
print(len(names))  # Length of names list

# Slicing lists
print(names[0:3])  # Output: ['John', 'Paul', 'George']   Slicing from index 0 to index 3
print(names[0:4:2])  # Output: ['John', 'George']   Slicing from index 0 to index 4 with step 2

# Sorting and reversing lists
names.sort()  # Sorts the names list alphabetically
print(names)  # Output: ['George', 'John', 'Paul', 'Ringo']
names.reverse()  # Reverses the order of the names list
print(names)  # Output: ['Ringo', 'Paul', 'John', 'George']

# Additional list operations
print(len(scores))  # Length of scores list
print(max(scores))  # Maximum value in scores list
print(min(scores))  # Minimum value in scores list
print(sum(scores))  # Sum of scores list


# Lists properties and capabilities
# - Lists are mutable
# - Lists are ordered
# - Lists are iterable
# - Lists are indexed
# - Lists can contain different data types
# - Lists can be nested
# - Lists can be sliced
# - Lists can be concatenated
# - Lists can be repeated
# - Lists can be sorted
# - Lists can be reversed
# - Lists can be searched for an item
# - Lists can be joined with other lists
# - Lists can be sliced with a start and end index
# - Lists can be sliced with a step
# - Lists can be sliced with a start, end, and step
