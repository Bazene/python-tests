import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    returned_value = request.param
    print("\nSetup! returned_value = {}".format(returned_value))

def test1(setup):
    print("\nSetup = {}".format(setup))
    assert True
