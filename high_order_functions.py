# Creating a lambda function that takes two arguments, x and function. It then returns the value of x plus
# the value of function(x).
high_ord_func = lambda x, function: x + function(x)


# High order with normal function

# Creating a lambda function that takes a single argument and returns the value of that argument plus 1.
increment = lambda x: x + 1

# Calling the `high_ord_func` function with two arguments, 2 and the `increment` function.
result_function = high_ord_func(2, increment)

print(result_function) # 5



# High order with lambda function

# Calling the `high_ord_func` function with two arguments, 2 and a lambda function that takes a single
# argument and returns the value of that argument plus 2.
result_lamba = high_ord_func(2, lambda x: x + 2)
print(result_lamba) # 6