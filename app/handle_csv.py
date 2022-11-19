import csv

def read_csv(path):
    """
    It takes a path to a CSV file, reads it, and returns a list of dictionaries, where each dictionary
    represents a row in the CSV file
    
    :param path: the path to the csv file
    :return: A list of dictionaries.
    """
    with open (path, 'r') as csvfile:
        # Reading the csv file and returning a reader object.
        reader = csv.reader(csvfile, delimiter=',')
        # Reading the first line of the csv file and assigning it to the variable `header`.
        header = next(reader)
        data = []
        for row in reader:
            # Creating a dictionary from the header and row and appending it to the list `data`.
            data.append(dict(zip(header, row)))
    return data


if __name__ == "__main__":
    # Calling the function read_csv and passing the path to the csv file as an argument.
    data = read_csv('./app/data.csv')
    print (data)