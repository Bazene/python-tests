import pytest

# ONE WAY (The commented function work, it is simular to the next one)

# @pytest.fixture()
# def setup():
#     print("\nSetup function")
#
# # First way to reuse setup function
# def test1(setup):
#     print("Execution test1!")
#     assert True
#
# # Second way to reuse setup function
# @pytest.mark.usefixtures("setup")
# def test2():
#     print("Executing test2!")
#     assert True


# SECOND WAY
@pytest.fixture(autouse=True)
def setup():
    print("\nSetup function")

def test1():
    print("Execution test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True