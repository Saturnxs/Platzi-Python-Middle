def run():

    # squares = []
    # for i in range(1, 101):
    #     squares.append(i**2)
    # print('Squares ', squares)
    
    squares = [i**2 for i in range(1, 101)]
    print('Squares ', squares)
    
    # squaresNotByThree = []
    # for i in range(1, 101):
    #     if (i % 3 != 0):
    #         squaresNotByThree.append(i**2)
    # print('Squares not divided by 3 ', squaresNotByThree)
    
    squaresNotByThree = [i**2 for i in range (1, 101) if i % 3 != 0]
    print('Squares not divided by 3 ', squaresNotByThree)
    
    challenge = [i for i in range (1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print('Challenge ', challenge)

if __name__ == "__main__":
    run()