numbers  = [1, 2, 3, 4, 5]

# Filtering out the even numbers from the list.
even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(list(even_numbers)) # [2, 4]
