try:
    from logic19 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(345)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(99)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(100)
    expected = True
    assert output == expected, "Wrong answer"