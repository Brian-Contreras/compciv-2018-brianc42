from data_helper import get_html
from bs4 import BeautifulSoup

def get_and_parse_inmate_rows():
    txt = get_html()
    soup = BeautifulSoup(txt, 'lxml')
    tags = []
    for tag in soup.select('tr'):
        tags.append(tag)
    inmates = []
    for x in range(1,len(tags)):
        inmates.append(tags[x])
    return inmates


def count_inmates():
    n = get_and_parse_inmate_rows()
    return len(n)