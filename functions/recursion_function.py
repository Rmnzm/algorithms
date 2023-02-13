def factorial_function(x):
    if x == 1:
        return 1
    else:
        return x * factorial_function(x - 1)


print(factorial_function(5))
