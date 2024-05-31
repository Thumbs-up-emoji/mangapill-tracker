import csv
from urllib.parse import urlparse

def parse_url(url, filename):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')     #splits by /, for basic parts of url
    number_parts = path_parts[2].split('-')     #splits by -, for chapter number and manga no.
    parsed_parts = number_parts[0], number_parts[1][:1], number_parts[1][1:-3], number_parts[1][-3]   #manga number, manga "group" no., manga chapter no., decimal point chapters

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list(parsed_parts))

# usage
# url = "https://mangapill.com/chapters/1063-20202500/dragon-ball-chapter-202.5"
# parse_url(url, 'db.csv')

def update(url,filename):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')     #splits by /, for basic parts of url
    number_parts = path_parts[2].split('-')     #splits by -, for chapter number and manga no.

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    found=False

    for row in data:
        if row[0] == number_parts[0]:
            row[1]=number_parts[1][:1]
            row[2]=number_parts[1][1:-3]
            row[3]=number_parts[1][-3]
            found=True
            break

    if not found:
        parse_url(url, filename)
    else:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
