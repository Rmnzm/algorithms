from functions.search.binary_search_function import binary_search


def test_binary_search_function():
    elems = [1, 3, 5, 7, 9]
    result = binary_search(elems, 3)

    assert result == 1
