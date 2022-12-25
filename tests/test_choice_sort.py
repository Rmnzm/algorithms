from functions.sort.choice_sorting import choice_sorting


def test_choice_sort():
    result = choice_sorting([5, 3, 6, 2, 10])

    assert result == [2, 3, 5, 6, 10]
