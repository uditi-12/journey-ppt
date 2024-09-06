import pytest
from calc import Calculator
 
def test_addition():
    calc = Calculator()
    assert calc.execute('add', 15, 15) == 30
 
def test_subtraction():
    calc = Calculator()
    assert calc.execute('subtract', 10, 4) == 6
 
def test_multiplication():
    calc = Calculator()
    assert calc.execute('multiply', 10, 5) == 50
 
def test_division():
    calc = Calculator()
    assert calc.execute('divide', 10, 2) == 5.0
 
def test_division_by_zero():
    calc = Calculator()
    assert calc.execute('divide', 10, 0) == "Error! Division by zero."
