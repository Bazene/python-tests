# Test fixtures scope : 4 scopes which specify how often the fixture will be called (a call that is not shown in really)
# 1. Function : run the fixture once for each test
# 2. Class : run the fixture once for each class of tests
# 3. Module : run once when the module goes in scope
# 4. Session : the fixture is run when pytest starts
# Here is the priority : Session > Module > Class > Function

import pytest


@pytest.fixture(scope= "session",autouse=True)
def setupSession():
    print("\nSetup Session")

@pytest.fixture(scope= "module",autouse=True)
def setupModule():
    print("\nSetup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True
