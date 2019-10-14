import csv
from os import makedirs


def search_bySpecies():
    species = 'Ixothraupis guttata'
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            #makedirs(f'{row[0]}/{row[1]}/{row[2]}', exist_ok=True)
            print(row)


search_bySpecies()
