try:
    from logic03 import bool_1
except ImportError:
    assert False, "Not found"

# Check that they are equal
def test_main_1():
    output = bool_1(6,6)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(4,2)
    expected = False
    assert output == expected, "Wrong answer"