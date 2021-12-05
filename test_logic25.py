try:
    from logic25 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(65432)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(45643)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(12347)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(96420)
    expected = True
    assert output == expected, "Wrong answer"