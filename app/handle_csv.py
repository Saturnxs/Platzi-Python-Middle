import csv

def read_csv(path):
    with open (path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            data.append(dict(zip(header, row)))
    return data


if __name__ == "__main__":
    data = read_csv('./app/data.csv')
    print (data)