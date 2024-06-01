a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c

print(result)

"""
result. Let's break it down step by step:

b * 7 = 3 * 7 = 21: Multiplies b by 7.
21 % 4 = 1: Calculates the remainder of dividing 21 by 4 using the modulus operator %. The modulus operator gives the remainder of the division operation.
a + 1 = 1 + 1 = 2: Adds a (which is 1) to the result of the previous step (which is 1).
2 - c = 2 - (-2) = 4: Subtracts c (which is -2) from the result of the previous step.

So, the final value of result is 4.

"""