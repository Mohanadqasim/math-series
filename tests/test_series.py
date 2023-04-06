import pytest
from series.series import *




# Fibonacci test cases:

def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_five():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected




# Lucas test cases:

def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_four():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_five():
    actual = lucas(4)
    expected = 7
    assert actual == expected




# sum_series test cases:

def test_sum_series_2_one():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_2_two():
    actual = sum_series(2,2,1)
    expected = 3
    assert actual == expected

def test_sum_series_2_three():
    actual = sum_series(2,5,1)
    expected = 6
    assert actual == expected