# fixtures are used for setup & teardown methods test cases
# conftest file is used to generalize fixture
# fixture become available to all test cases when defined in conftest file
# datadriven & parameterization can be done with return statement in tuple format
# once you define fixture scope to class only, it will run once before class is initiated & at the end

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ["deepak","thakur","thakurdpk786@gmail.com"]

@pytest.fixture(params=[("Chrome","deepak","thakur"),("Firefox","deepak"),"Edge"])
def crossBrowser(request):
    return request.param