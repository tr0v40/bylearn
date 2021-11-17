from variables.exercises import multiplication

def test_multiplication_asserts():
    multi = multiplication.multiplication_values
    assert multi(7,8) == 56
    assert multi(10,5) == 50
    assert multi(2,2) == 4
    assert multi(1,5) != 50
