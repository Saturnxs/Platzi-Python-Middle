def run():
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print('my_dict ', my_dict)
    
    my_dict_not_divided_by_three = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print('my_dict_not_divided_by_three ', my_dict_not_divided_by_three)
    
    challenge = {i: i**0.5 for i in range(1,1001)}
    print('challenge ', challenge)


if __name__ == "__main__":
    run()