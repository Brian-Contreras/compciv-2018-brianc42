import requests
from bs4 import BeautifulSoup


OFFICIAL_URL='https://www.stanford.edu/news/'
SAMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'


def fetch_hedz(url=OFFICIAL_URL):
    txt = fetch_html(url)
    tags = parse_headline_tags(txt)
    headlines = []
    for tag in tags:
        dic = extract_headline_data(tag)
        headlines.append(dic)
    return headlines


def extract_headline_data(tag):
    url = tag.get('href')
    title = tag.get_text()
    dic = {}
    dic['url'] = url
    dic['title'] = title
    return dic


def fetch_html(url):
    txt = requests.get(url)
    return txt.text


def parse_headline_tags(txt):
    soup = BeautifulSoup(txt, 'lxml')
    tags = []
    for tag in soup.select('h3 > a'):
        tags.append(tag)
    return tags


def print_hedz(url=OFFICIAL_URL):
    headlines = fetch_hedz(url)
    for hed in headlines:
        print(hed['title'])