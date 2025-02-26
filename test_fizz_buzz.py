import pytest


# USE CASE 1 : call FizzBuzz
def fizz_buzz(value):
    return value

def test_can_call_fizz_buzz():
    fizz_buzz(1)

# USE CASE 2 : Get "1" when I pass in 1
def test_returns1_with_1passed():
    returned_val = fizz_buzz(1)
    assert returned_val == 1

test_returns1_with_1passed()

