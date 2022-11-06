import utils # Importing the `utils` module.

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values) # ['col', 'bol'] [300, 400]



    string = utils.text
    print(string) # Hello world!


    country = input('Type country: ') # Colombia
    result = utils.population_by_country(data, country)
    print(result) # [{'Country': 'Colombia', 'Population': 500}]
    

if __name__ == "__main__":
    run()