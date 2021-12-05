try:
    from logic09 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(2, 4, 5)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(6, 3, 8)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(9, 3, 1)
    expected = True
    assert output == expected, "Wrong answer"