def divisors(num):
        assert num > 1, 'No se puede ingresar un numero negativo'
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
            #if num % i == 1: <---- Bug!
                divisors.append(i)
        return divisors


def run():
        num = input("Ingresa un número: ")
        assert num.isnumeric(), "Debe ingresar un numero"
        print(divisors(int(num)))
        print("Final")


if __name__ == '__main__':
    run()