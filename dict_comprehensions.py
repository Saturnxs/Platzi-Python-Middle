import random


def run():
    # Creating a dictionary with the keys being the numbers from 1 to 100 that are not divisible by 3
    # and the values being the cubes of those numbers.
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print('my_dict ', my_dict)
    
    
    # Creating a dictionary with the keys being the numbers from 1 to 100 that are not divisible by 3
    # and the values being the cubes of those numbers.
    my_dict_not_divided_by_three = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print('my_dict_not_divided_by_three ', my_dict_not_divided_by_three)
    
    
    # Creating a dictionary with the keys being the numbers from 1 to 1000 and the values being the
    # square roots of those numbers.
    challenge = {i: i**0.5 for i in range(1,1001)}
    print('challenge ', challenge)
    
    
    # Creating a dictionary with the keys being the countries and the values being the population of those
    # countries.
    countries = ['col', 'mex', 'bol']
    population = {country: random.randint(1,100) for country in countries}
    print(population)
    
    
    names = ['nico', 'zule', 'santi']
    ages = [12, 56, 98]
    
    users = {name: age for (name, age) in zip(names, ages)}
    print(users)

if __name__ == "__main__":
    run()