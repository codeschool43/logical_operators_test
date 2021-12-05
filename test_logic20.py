try:
    from logic20 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(22)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(99)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(9)
    expected = False
    assert output == expected, "Wrong answer"