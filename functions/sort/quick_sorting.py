def quick_sorting(arr):
    if len(arr) < 2:
        return arr
    else:
        prev = arr[0]
        less = [i for i in arr[1:] if i < prev]

        great = [i for i in arr[1:] if i > prev]

        return quick_sorting(less) + [prev] + quick_sorting(great)


print(quick_sorting([10, 5, 2, 3]))
