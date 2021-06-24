import pytest


@pytest.mark.smoke
def test_firstTest(setup):
    msg = "Hello"
    assert msg == "Hi", "Failed, because string don't match"

@pytest.mark.xfail
def test_secondTest(setup):
    a = 4
    b = 2
    assert a + 2 == 6, "Addition do not match"

