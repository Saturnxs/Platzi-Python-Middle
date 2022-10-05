def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
        #if num % i == 1: <---- Bug!
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Final")


if __name__ == '__main__':
    run()