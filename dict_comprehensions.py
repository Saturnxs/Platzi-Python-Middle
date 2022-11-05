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
    
    
    # Creating a dictionary with the keys being the names and the values being the ages.
    names = ['nico', 'zule', 'santi']
    ages = [12, 56, 98]
    
    # zip(names, ages) - Creating a list of tuples.
    users = {name: age for (name, age) in zip(names, ages)}
    print(users)
    
    
    # Creating a dictionary with the keys being the vowels and the values being the vowels in uppercase.
    text = 'Hola, soy Thomas'
    
    unique = {char: char.upper() for char in text if char in 'aeiou'}
    print(unique)

if __name__ == "__main__":
    run()