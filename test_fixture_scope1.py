# Test fixtures scope : 4 scopes which specify how often the fixture will be called (a call that is not shown in really)
# 1. Function : run the fixture once for each test
# 2. Class : run the fixture once for each class of tests
# 3. Module : run once when the module goes in scope
# 4. Session : the fixture is run when pytest starts
# Here is the priority : Session > Module > Class > Function

import pytest


@pytest.fixture(scope= "module",autouse=True)
def setupModule1():
    print("\nSetup Module1")

@pytest.fixture(scope= "class",autouse=True)
def setupClass1():
    print("\nSetup Class1")

@pytest.fixture(scope="function", autouse=True)
def setupFunction1():
    print("\nSetup Function1")

class TestClass:
    def test_it(self):
        print("TestIt")
        assert True

    def test_it1(self):
        print("TestIt1")
        assert True
