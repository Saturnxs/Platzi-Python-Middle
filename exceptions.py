try:
    print(0/0);
except ZeroDivisionError as error:
    print(error)
    
print("El programa llega acá") # Se imprime aunque falle



try:
    assert 1 != 1, "Uno no es igual que uno" # El error se contiene en el try
except AssertionError as error:
    print(error)
    
    
print("El programa llega acá también") # Se imprime aunque falle



try:
    age = 10 # El error se contiene en el try

    if age < 18: 
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)
    
    
print("Y programa llegó también acá") # Se imprime aunque falle}







try:
    print(0/0)
    assert 1 != 1, "Uno no es igual que uno" # El error se contiene en el try
    age = 10 # El error se contiene en el try

    if age < 18: 
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
    
print("El programa llega acá") # Se imprime aunque falle

