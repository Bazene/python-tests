import pytest


# USE CASE 1 : call FizzBuzz
def fizz_buzz(value):
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    return str(value)


def check_expected(value, expected_string):
    response = fizz_buzz(value)
    assert response == expected_string

def test_can_call_fizz_buzz():
    fizz_buzz(1)

# USE CASE 2 : Get "1" when I pass in 1
def test_returns1_with_1passed():
    check_expected(1, "1")

# USE CASE 3 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_3multiples():
    print("Hey")
    check_expected(3, "Fizz")

# USE CASE 4 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_5multiples():
    check_expected(5, "Buzz")

# USE CASE 5 : Get "Fizz" when I pass in 6 (a multiple of 3)
def test_fizz_for_15multiples():
    check_expected(15, "FizzBuzz")

