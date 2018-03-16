from pathlib import Path 
from bs4 import BeautifulSoup

import csv

OUTPUT_HEADERS = [
    'first_name',
    'last_name',
    'category',
    'report_type',
    'url',
    'date'
]

html_filepath = Path('samples', 'ca-senate-disclosures-index.html')
html = html_filepath.read_text()
soup = BeautifulSoup(html, 'lxml')
tags = soup.select('tbody tr')

output_filepath = Path('samples', 'ca-senate.csv')
ofile = output_filepath.open('w')
cfile = csv.DictWriter(ofile, fieldnames=OUTPUT_HEADERS)

cfile.writeheader()

for row in tags:
    cols = row.select('td')
    d = {}
    d['first_name'] = cols[0].text.strip()
    d['last_name'] = cols[1].text.strip()
    d['category'] = cols[2].text.strip()
    d['report_type'] = cols[3].text.strip()
    link = cols[3].select_one('a')
    d['url'] = link.attrs['href']
    d['date'] = cols[4].text.strip()

    cfile.writerow(d)

ofile.close()