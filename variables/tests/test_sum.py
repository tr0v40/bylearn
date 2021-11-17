from variables.exercises import sum_values

def test_sum_values():
    sum_v = sum_values.sum_values

    assert sum_v(3,2) == 5
    assert sum_v(7,7) == 14
    assert sum_v(3,1) != 5
