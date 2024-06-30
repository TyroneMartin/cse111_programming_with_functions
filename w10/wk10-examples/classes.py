"""
This line defines a new class called `Person`:
- A class is a blueprint or template for creating objects.
- Objects are instances of the class (blueprint).
- Classes encapsulate data (attributes) and behaviors (methods).
- Attributes are variables attached to the class and behaviors are functions attached to the class.
"""
class Person:

    """
    This is a special method called the constructor or initializer (`__init__`):
    - It is automatically called when a new instance of the `Person` class is created.
    - The `self` parameter refers to the current instance of the class. It is a convention in Python
      to use `self` as the first argument in instance methods (function).
    - The `name` and `age` parameters are used to initialize the corresponding attributes
      (`self.name` and `self.age`) for each instance of the `Person` class. These attributes will
      store the name and age values specific to each person object.

    Args:
        name (str): The name of the person
        age (int): The age of the person
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    This is a special method called the to-string (`__str__`) method:
    - It is a built-in method in Python that provides a string representation of an object.
    - The `__str__` method is automatically called when we use the `print` function or the `str`
      function on an object.
    - By defining the `__str__` method within a class, we can customize the string representation of
      instances of that class. In simple terms, if the user prints this class we can control what is
      output by `print`.

    Args:
        self (Person): The instance of the `Person` class on which the method is called

    Returns:
        str: A string representation of the person's name and age
    """
    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    """
    This is a method (function) defined within the `Person` class:
    - It takes `self` as the first argument, which allows it to access and manipulate the attributes
      of the instance it is called on.
    - When this method is called on a `Person` instance, it will print a message indicating that the
      person (represented by `self.name`) is walking.

    Args:
        self (Person): The instance of the `Person` class on which the method is called

    Returns:
        None
    """
    def go_for_a_walk(self):
        print(f'{self.name} is walking')

    """
    This is another method within the `Person` class:
    - It checks the `age` attribute of the instance it is called on.
    - If the age is greater than 55, it prints a message indicating that the person is eating a
      cheap meal, otherwise, it prints a message saying the person is eating an expensive meal.

    Args:
        self (Person): The instance of the `Person` class on which the method is called

    Returns:
        None
    """
    def eat(self):
        if self.age > 55:
            print(f'{self.name} is eating a cheap meal')
        else:
            print(f'{self.name} is eating an expensive meal')

    """
    This method is similar to the `eat` method:
    - It checks the age attribute and prints a message about the person's energy level; the message
      that prints we be determined by the person's (this instances) `age` value.

    Args:
        self (Person): The instance of the `Person` class on which the method is called

    Returns:
        None
    """
    def dance(self):
        if self.age > 30:
            print(f'{self.name} is dancing with less energy')
        else:
            print(f'{self.name} is dancing with ENDLESS energy')


"""
Here, we create two instances (objects) of the `Person` class:
- The `Person` constructor (`__init__`) is called for each instance with the provided `name` and `age` values.
- The new instances are assigned to the variables `brian` and `jeff`, respectively.
"""
brian = Person('Brian', 12)
jeff = Person('Jeff', 60)

"""
These lines call the `eat`, `dance`, and `go_for_a_walk` methods on the `brian` and `jeff` instances.
The methods will execute their respective logic and print messages based on the `name` and `age`
attributes of each instance.
"""
print()
brian.eat()
jeff.eat()
print()
brian.dance()
jeff.dance()
print()
brian.go_for_a_walk()
jeff.go_for_a_walk()

"""
These lines demonstrate the overridden `__str__` (toString) method in action. Normally when printing
a class (object) you will get a hexadecimal string representing it's location in memory. With our
`__str__` method working it will print a sentence describing the instance instead.
"""
print()
print(brian)
print(jeff)
print()