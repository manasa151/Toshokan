import csv

ebird = 'Ixothraupis guttata'


def search_bySpecies():
    path = 'C:\\Users\\jmentore\\Dropbox\\個人図書館-Kojin toshokan\\Thraupis_episcopus.csv'
    species = ebird
    csv_file = csv.reader(open('path', 'r'))

    for row in csv_file:
        print(row)


search_bySpecies()
