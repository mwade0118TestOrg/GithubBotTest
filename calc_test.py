import calc

def test_add():
    val = calc.add(23, 1)
    assert val == 24

def test_times():
    val = calc.multiply(8, 2)
    assert val == 16

def test_divide():
    val = calc.divide(0, 999)
    assert val == 0.0

def test_subtract():
    val = calc.subtract(10,8)
    assert val == 2