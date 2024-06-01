"""
This demo uses code that is very similar to what you will need in storage
efficiency assignment. Try adding people to the lists and see how the output
changes. Try changing the ages and see how the output is different.
"""
names = ['Peter', 'John', 'Luke']
ages = [11, 35, 15]
heights = [56, 106, 78]

oldest = -1
oldest_person = None
oldest_age = -1

for i in range(len(names)):
    name = names[i]
    age = ages[i]
    height = heights[i]

    if age > oldest:
        oldest = age
        oldest_person = name
        oldest_age = age

    print(f'Name: {name} Age: {age} Height: {height}')

print(f'The oldest person is {oldest_person} at {oldest_age} years old.')
