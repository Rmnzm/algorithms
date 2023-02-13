from functions.sort.quick_sorting import quick_sorting


def test_quick_sort():
    result = quick_sorting([10, 5, 2, 3])

    assert result == [2, 3, 5, 10]
