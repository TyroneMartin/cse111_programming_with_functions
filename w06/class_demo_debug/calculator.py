def add(*nums):
    """
    Add all numbers passed in as arguments.

    Arguments:
        *nums ([int|float]): A list of numbers to add.

    Returns:
        (int|float): The result of adding all numbers passed in as arguments, or raises a TypeError
                     exception.
    """
    if not nums:
        raise TypeError("Not enough numbers to add")
    
    result = 0
    for num in nums:
        result += num
    return result


def subtract(*nums):
    """
    Subtract all numbers passed in as arguments.

    Arguments:
        *nums ([int|float]): A list of numbers to subtract.

    Returns:
        (int|float): The result of subtracting all numbers passed in as arguments, or raises a
                     TypeError exception.
    """
    if not nums:
        raise TypeError("Not enough numbers to subtract")

    result = nums[0]
    for num in nums[1:]:
        result -= num
    return result


def multiply(*nums):
    """
    Multiplies all numbers passed in as arguments.

    Arguments:
        *nums ([int|float]): A list of numbers to multiply.

    Returns:
        (int|float): The result of multiplying all numbers passed in as arguments, or raises a
                     TypeError exception.
    """
    if not nums:
        raise TypeError("Not enough numbers to multiply")
    
    result = 1
    for num in nums:
        result *= num
    return result


def divide(*nums):
    """
    Divides all numbers passed in as arguments.

    Arguments:
        *nums ([int|float]): A list of numbers to divide.

    Returns:
        (int|float): The result of dividing all numbers passed in as arguments, or raises a TypeError
                     or ZeroDivisionError exception.
    """
    if not nums:
        raise TypeError("Not enough numbers to divide")

    try:
        result = nums[0]
        for num in nums[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")


# Our main function that should not be run in this demo!
def main():
    while True:
        print('TRAP! You ran this code wrong press [ctrl] + [c]')


# Do not call main() if this file was imported by another.
if __name__ == '__main__':
    main()