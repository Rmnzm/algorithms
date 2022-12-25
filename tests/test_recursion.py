from functions.recursion_function import factorial_function


def test_recursion():
    result = factorial_function(5)

    assert result == 120
