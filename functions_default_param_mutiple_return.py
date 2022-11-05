# Function with default values for the parameters.
def find_volume(width = 1, lenght = 1, height = 1):
    # Returning a tuple with the result of the multiplication, the width and the string 'hola'.
    return width * lenght * height, width, 'hola'


# Printing the tuple returned by the function.
print(find_volume(width=100))


# Printing the first element of the tuple returned by the function.
print(find_volume(width=100)[0])


# Unpacking the tuple returned by the function.
volume, width, text = find_volume(width=100)

print(volume)
print(width)
print(text)

