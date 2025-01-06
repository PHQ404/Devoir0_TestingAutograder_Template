import pytest
from src.calculator import Calculator  # Import Calculator class from src/calculator.py

def test_add():
    assert Calculator.add(3, 4) == 7
    assert Calculator.add(-1, 1) == 0

def test_subtract():
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(3, 4) == -1

def test_multiply():
    assert Calculator.multiply(2, 5) == 10
    assert Calculator.multiply(-2, 4) == -8

def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(9, 3) == 3

    with pytest.raises(ValueError):
        Calculator.divide(5, 0)
