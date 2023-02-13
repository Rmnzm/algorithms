def binary_search(elems: list, item: int):
    low = 0
    high = int(len(elems) - 1)

    while low <= high:
        mid = int((low + high) / 2)
        guess = elems[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


elems = [1, 3, 5, 7, 9]
print(binary_search(elems, 3))
