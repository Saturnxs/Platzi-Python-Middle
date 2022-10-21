def run():
   # Creating a list and a dictionary.
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}
    
    # Creating a list of dictionaries.
    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Arqueada"},
        {"firstname": "Armando", "lastname": "Valles"},
    ]
    
    # Creating a dictionary with three keys, each one with a list of numbers.
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }
    
    # Iterating through the dictionary and printing the key and the value of each item.
    for key, value in super_dict.items():
        print(key, "-", value)
        
    # Iterating through the list and printing each item.
    for i in super_list:
        print(i);


if __name__ == "__main__":
    run()



