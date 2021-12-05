try:
    from logic23 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(212)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(321)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(364)
    expected = True
    assert output == expected, "Wrong answer"