text = 'Hello world!'

def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    
    return keys, values


def population_by_country(data, country):
    return list(filter(lambda item: item['Country'] == country, data))