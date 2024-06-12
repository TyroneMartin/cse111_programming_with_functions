# Import the array module
from array import array

# Create an array of type 'd' (double - represents a floating point number)
# or # Create an array of type 'f' (float)

scores = array('d')

# Append elements to the array
scores.append(100.0)
scores.append(56.0)

# Print the entire array
print(scores)  # Output: array('d', [100.0, 56.0])

# Access an element by index
print(scores[1])  # Output: 56.0

# Additional use cases:

# Extending an array with another array or iterable
more_scores = array('d', [75.5, 89.0, 92.5])
scores.extend(more_scores)
print(scores)  # Output: array('d', [100.0, 56.0, 75.5, 89.0, 92.5])

# Inserting an element at a specific position
scores.insert(2, 65.0)
print(scores)  # Output: array('d', [100.0, 56.0, 65.0, 75.5, 89.0, 92.5])

# Removing an element by value
scores.remove(56.0)
print(scores)  # Output: array('d', [100.0, 65.0, 75.5, 89.0, 92.5])

# Removing an element by index
del scores[0]
print(scores)  # Output: array('d', [65.0, 75.5, 89.0, 92.5])

# Reversing the array
scores.reverse()
print(scores)  # Output: array('d', [92.5, 89.0, 75.5, 65.0])

# Summing the elements of the array
total = sum(scores)
print(total)  # Output: 322.0

# Finding the maximum and minimum values
max_score = max(scores)
min_score = min(scores)
print(max_score)  # Output: 92.5
print(min_score)  # Output: 65.0

# Converting the array to a list
scores_list = scores.tolist()
print(scores_list)  # Output: [92.5, 89.0, 75.5, 65.0]

# Iterating over the elements of the array
for score in scores:
    print(score)

# Output:
# 92.5
# 89.0
# 75.5
# 65.0

# Creating an array from an existing iterable
scores_from_iterable = array('d', [45.0, 50.5, 60.0])
print(scores_from_iterable)  # Output: array('d', [45.0, 50.5, 60.0])
