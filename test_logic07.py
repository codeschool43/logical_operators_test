try:
    from logic07 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(5)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(8)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(-2)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_4():
    output = bool_1(0)
    expected = False
    assert output == expected, "Wrong answer"