def sum_function_1(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum_function_1([1, 2, 3, 4]))


def sum_function_2(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_function_2(arr[1:])


print(sum_function_2([1, 2, 3, 4, 5, 6]))
