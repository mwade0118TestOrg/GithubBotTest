import hello

def test_add_one():
    val = hello.addOne(23)
    assert val == 24

def test_times_two():
    val = hello.timesTwo(8)
    assert val == 16

def test_zero():
    val = hello.zero(999)
    assert val == 5