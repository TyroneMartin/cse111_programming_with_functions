from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    """Test the `add()` function."""

    # Test that the function returns the correct result when given two numbers.
    assert add(1, 2) == 3
    assert add(-10, 3) == -7
    assert add(11, 35.55) == 46.55

    # Test that the function raises a TypeError if it is called with no parameters.
    with pytest.raises(TypeError):
        add()


def test_subtract():
    """Test the `subtract()` function."""

    # Test that the function returns the correct result when given two numbers.
    assert subtract(5, 2) == 3
    assert subtract(5.5, 0.5) == 5
    assert subtract(-5, 5) == -10

    # Test that the function raises a TypeError if it is called with no parameters.
    with pytest.raises(TypeError):
        subtract()


def test_multiply():
    """Test the `multiply()` function."""

    # Test that the function returns the correct result when given two numbers.
    assert multiply(3, 4) == 12
    assert multiply(3.5, 2) == 7
    assert multiply(5, 5) == 25

    # Test that the function raises a TypeError if it is called with no parameters.
    with pytest.raises(TypeError):
        multiply()


def test_divide():
    """Test the `divide()` function."""

    # Test that the function returns the correct result when given two numbers.
    assert divide(10, 5) == 2
    assert divide(100, 10) == 10
    assert divide(10, 4) == 2.5

    # Test that the function raises a TypeError if it is called with no parameters.
    with pytest.raises(TypeError):
        divide()

    # Test that the function raises a ZeroDivisionError if it is called with a zero as the divisor.
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


pytest.main(["-v", "--tb=line", "-rN", __file__])