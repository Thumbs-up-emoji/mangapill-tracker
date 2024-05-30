#implement checking if same manga already added before
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