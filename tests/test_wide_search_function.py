from functions.search.wide_search_function import wide_search_function


def test_wide_search_function():
    result = wide_search_function("you")

    assert 'thom is a mango seller' in result
    assert True in result
    assert len(result) == 2
