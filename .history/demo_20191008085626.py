import csv

ebird = 'Ixothraupis guttata'


def search_bySpecies():

    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)


search_bySpecies()
