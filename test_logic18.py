try:
    from logic18 import bool_1
except ImportError:
    assert False, "Not found"

def test_main_1():
    output = bool_1(44)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_2():
    output = bool_1(6)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_3():
    output = bool_1(100)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_4():
    output = bool_1(100)
    expected = False
    assert output == expected, "Wrong answer"

def test_main_5():
    output = bool_1(10)
    expected = True
    assert output == expected, "Wrong answer"

def test_main_6():
    output = bool_1(99)
    expected = True
    assert output == expected, "Wrong answer"