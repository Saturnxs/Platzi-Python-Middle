def run():
    # Creating a set of countries.
    set_countries = {'col', 'mex', 'bol'}
    print(set_countries)
    print(type(set_countries))
    
    # Creating a set of numbers.
    set_numbers = {1,2 ,2, 443, 23}
    print(set_numbers)
    print(type(set_numbers))
    
    # Creating a set with different types of data.
    set_types = {False, 1, "Hola", 12.22}
    print(set_types)
    
    # Creating a set from a string.
    set_from_string = set('Hola')
    print(set_from_string)
    
    # Creating a set from a tuple.
    set_from_tupla = set(('abc', 'cbv', 'as', 'abc'))
    print(set_from_tupla)

    # Creating a list of numbers and then converting it to a set.
    numbers = [1,2,3,1,2,3,4]
    set_numbers_list = set(numbers)
    print(set_numbers_list)
    
    # Converting the set to a list.
    unique_numbers = list(set_numbers_list)
    print(unique_numbers)


if __name__ == "__main__":
    run()