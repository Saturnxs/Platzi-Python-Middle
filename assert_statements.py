def divisors(num):
        """
        It returns a list of all the divisors of a number
        
        :param num: The number to find the divisors of
        :return: [1, 2, 3, 4, 6, 12]
        """
        # It's checking if the number is greater than 1. If it's not, it will raise an AssertionError.
        assert num > 1, 'No se puede ingresar un numero negativo'
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
            #if num % i == 1: <---- Bug!
                divisors.append(i)
        return divisors


def run():
        """
        It takes a number as input, checks if it's a number, and then prints the divisors of that number
        """
        # It's asking the user to input a number, and then it's checking if the input is a number. If
        # it's not, it will raise an AssertionError.
        num = input("Ingresa un número: ")
        assert num.isnumeric(), "Debe ingresar un numero"
        print(divisors(int(num)))
        print("Final")


if __name__ == '__main__':
    run()