import csv

ebird = 'Ixothraupis guttata'


def search_bySpecies(species):
    path = 'C:\\Users\\jmentore\\Dropbox\\個人図書館-Kojin toshokan\\request_species.csv'
    species = ebird
    csv_file = csv.reader(open('path', 'r'))

    for row in csv_file:
        print(row)
