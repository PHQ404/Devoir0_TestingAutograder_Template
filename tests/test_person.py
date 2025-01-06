import pytest
from src.person import Person  # Import Person class from src/person.py

def test_greet():
    person = Person("John", 25)
    assert person.greet() == "Hello, my name is John and I am 25 years old."

def test_is_adult():
    person_adult = Person("Alice", 20)
    person_child = Person("Bob", 15)
    assert person_adult.is_adult() is True
    assert person_child.is_adult() is False
