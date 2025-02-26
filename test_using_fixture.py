# Test fixtures scope : 4 scopes which specify how often the fixture will be called
# 1. Function : run the fixture once for each test
# 2. Class : run the fixture once for each class of tests
# 3. Module : run once when the module goes in scope
# 4. Session : the fixture is run when pytest starts

import pytest

# ONE WAY TO USE FIXTURE FOR SETUP FUNCTION (The commented function work, it is simular to the next one)

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


# SECOND WAY TO USE FIXTURE FOR SETUP FUNCTION
# @pytest.fixture(autouse=True)
# def setup():
#     print("\nSetup function")
#
# def test1():
#     print("Execution test1!")
#     assert True
#
# def test2():
#     print("Executing test2!")
#     assert True


# HERE IS THE CODE FOR FIXTURE WITH TEARDOWN
@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1!")
    assert True

def test2(setup2):
    print("Executing test2!")
    assert True
