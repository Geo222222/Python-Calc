import pytest
from logic import evaluate_expression

def test_addition():
    assert evaluate_expression("2 + 3") == 5

def test_subtraction():
    assert evaluate_expression("10 - 4") == 6

def test_multiplication():
    assert evaluate_expression("3 * 7") == 21

def test_division():
    assert evaluate_expression("8 / 2") == 4

def test_decimal_operations():
    assert evaluate_expression("2.5 + 1.5") == 4.0

def test_order_of_operations():
    assert evaluate_expression("2 + 3 * 4") == 14

def test_parentheses():
    assert evaluate_expression("(2 + 3) * 4") == 20

def test_invalid_characters():
    with pytest.raises(ValueError):
        evaluate_expression("2 + 3a")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_expression("5 / 0")

def test_empty_expression():
    with pytest.raises(ValueError):
        evaluate_expression("")
