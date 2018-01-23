def print_hedz(url='https://www.stanford.edu/news/'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)
    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)


def extract_headline_text(txt):
    iterator = 0
    headline = ""
    for chr in txt:
        if iterator == 2:
            if chr == '<':
                iterator += 1
            else:
                headline += chr
        if chr == '>':
            iterator += 1
    return headline


def parse_headline_tags(txt):
    lines = txt.splitlines()
    list = []
    for line in lines:
        if "<h3><a" in line:
            list.append(line)
    return list


def fetch_html(url):
    import requests
    html = requests.get(url)
    return html.text