import csv

def print_all(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            url = "https://mangapill.com/chapters/" + str(row[0]) + "-" + str(row[1]) + str(row[2]) + str(row[3]) + "00"
            print(url)