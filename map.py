numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

# Using the map function to multiply each element in the list by 2.
numbers_double = list(map(lambda i: i * 2, numbers_1))
print(numbers_double) # [2, 4, 6, 8]

# Adding the first element of numbers_1 to the first element of numbers_2, the second element of
# numbers_1 to the second element of numbers_2, and so on.
list_sum = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(list_sum) # [6, 8, 10] (1 + 5, 1 + 6, 3 + 7)



