try:
    from logic04 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(3)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(5)
    expected = True
    assert output == expected, "Wrong answer"