try:
    from logic01 import bool_1
except ImportError:
    assert False, "Not found"

# assign a bool type value to the result variable.
def test_main_1():
    output = bool_1()
    expected = bool
    assert output == expected, "Wrong answer"