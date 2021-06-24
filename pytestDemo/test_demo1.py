# any pytest file should start with prefix text_ or end with _test
# pytest method name should start with prefix text_
# any code should be wrapped in method only
# method name should have sense
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# -m stands for mark
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.regression
def test_secondProgram(setup):
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
