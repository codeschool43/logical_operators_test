try:
    from logic24 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(21265)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(9999)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(100000)
    expected = False
    assert output == expected, "Wrong answer"