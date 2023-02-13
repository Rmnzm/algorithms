from functions.sum_function import sum_function_1, sum_function_2


def test_sum_func_1():
    result = sum_function_1([1, 2, 3, 4, 5])

    assert result == 15


def test_sum_func_2():
    result = sum_function_2([1, 2, 3, 4, 5])

    assert result == 15
