import utils # Importing the `utils` module.
import handle_csv
import charts

def run():
    data = handle_csv.read_csv('./app/data.csv')
    country = input('Type country: ')
    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)



if __name__ == "__main__":
    run()