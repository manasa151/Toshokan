import csv
from os import makedirs


def search_bySpecies():
    species = 'Megarynchus pitangua'
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if species == row[2]:
                makedirs(f'{row[0]}/{row[1]}/{row[2]}', exist_ok=True)
                print(row)
