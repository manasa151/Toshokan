import csv


def search_bySpecies():
    species = 'Ixothraupis guttata'
    with open('request_species.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if species == row[2]:
                print(row[0])
                print(row[1])
                print(row[2])


search_bySpecies()
