import functools

numbers = [1, 2, 3, 4]

# Adding all the numbers in the list together.
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)