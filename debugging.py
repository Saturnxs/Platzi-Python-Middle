def divisors(num):
    """
    It takes a number and returns a list of all the numbers that divide evenly into it
    
    :param num: The number to find the divisors of
    :return: A list of divisors of the number.
    """
    try:
        # Raising an exception if the user enters a negative number.
        if(num < 0):
            raise ValueError('No se puede ingresar un numero negativo')
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
            #if num % i == 1: <---- Bug!
                divisors.append(i)
        return divisors
    # Catching the exception that is raised when the user enters a non-numeric value.
    except ValueError as ve:
        print(ve)


def run():
    """
    It asks the user for a number, and then prints the divisors of that number
    """
    try:
        num = int(input("Ingresa un número: "))    
        print(divisors(num))
        print("Final")
    # Catching the exception that is raised when the user enters a non-numeric value.
    except ValueError:
        print("Se debe ingresar un numero")
        

if __name__ == '__main__':
    run()