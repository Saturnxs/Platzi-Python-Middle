def run():

    # squares = []
    # for i in range(1, 101):
    #     squares.append(i**2)
    # print('Squares ', squares)
    
    
    # Creating a list of squares of numbers from 1 to 100.
    squares = [i**2 for i in range(1, 101)]
    print('Squares ', squares)
    
    # squaresNotByThree = []
    # for i in range(1, 101):
    #     if (i % 3 != 0):
    #         squaresNotByThree.append(i**2)
    # print('Squares not divided by 3 ', squaresNotByThree)
    
    
    # Creating a list of squares of numbers from 1 to 100 that are not divisible by 3.
    squaresNotByThree = [i**2 for i in range (1, 101) if i % 3 != 0]
    print('Squares not divided by 3 ', squaresNotByThree)
    
    
    # Creating a list of numbers from 1 to 100000 that are divisible by 4, 6 and 9.
    challenge = [i for i in range (1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print('Challenge ', challenge)

if __name__ == "__main__":
    run()