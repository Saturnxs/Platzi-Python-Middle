def divisors(num):
    try:
        if(num < 0):
            raise ValueError('No se puede ingresar un numero negativo')
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
            #if num % i == 1: <---- Bug!
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    try:
        num = int(input("Ingresa un número: "))    
        print(divisors(num))
        print("Final")
    except ValueError:
        print("Se debe ingresar un numero")
        
        


if __name__ == '__main__':
    run()