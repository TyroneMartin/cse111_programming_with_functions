"""
Map
"""
numbers = [2, 17, 5, 19, 87, 4, 56]

""" Add 3 to each item in the list using Map and a Lambda function. """
mod_numbers = list(map(lambda num: num + 3, numbers))


""" Without Map we would have to do the following instead: """
# def add(num):
#     return num + 3

# mod_numbers = []
# for num in numbers:
#     mod_numbers.append(add(num))

print(f'Original numbers: {numbers}')
print(f'Modified numbers: {mod_numbers}')
print()

"""
Filter
"""

""" Use Filter to make an odd and even list out of our numbers. """
odd_nums = list(filter(lambda num: num % 2 == 1, numbers))
even_nums = list(filter(lambda num: num % 2 == 0, numbers))

""" Without Filter we would have to do the following instead: """
# odd_nums = []
# even_nums = []

# for num in numbers:
#     if num % 2 == 0:
#         even_nums.append(num)
#     else:
#         odd_nums.append(num)

print(f'Original numbers:  {numbers}')
print(f'Odd numbers only:  {odd_nums}')
print(f'Even numbers only: {even_nums}')
print()