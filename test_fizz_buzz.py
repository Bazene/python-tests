import pytest


# USE CASE 1 : call FizzBuzz
def fizz_buzz(value):
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    if value % 15 == 0:
        return "FizzBuzz"
    return str(value)

def test_can_call_fizz_buzz():
    fizz_buzz(1)

# USE CASE 2 : Get "1" when I pass in 1
def test_returns1_with_1passed():
    returned_val = fizz_buzz(1)
    assert returned_val == "1"

# USE CASE 3 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_3multiples():
    response = fizz_buzz(3)
    assert response == "Fizz"

# USE CASE 4 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_5multiples():
    response = fizz_buzz(5)
    assert response == "Buzz"

# USE CASE 5 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_15multiples():
    response = fizz_buzz(5)
    assert response == "FizzBuzz"

test_fizz_for_15multiples()