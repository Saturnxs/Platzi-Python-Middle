# Asserts

suma = lambda x,y: x+y
assert suma(2,2) == 4

print("Test passsed")

mult = lambda x,y: x*y
assert mult(1,2) == 4
# Traceback (most recent call last):
#   File "c:\Users\emabm\Documents\Development\PLATZI\PYTHON\Platzi-Middle-Python\errors.py", line 9, in <module>
#     assert mult(1,2) == 4
# AssertionError
# print("Test passsed") will never print


age = 10

if age < 18:
    raise Exception('No se permiten menores de edad')
# Traceback (most recent call last):
#     raise Exception('No se permiten menores de edad')
# Exception: No se permiten menores de edad


