try:
    from logic22 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(22)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(31)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(34)
    expected = True
    assert output == expected, "Wrong answer"