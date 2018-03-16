from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso


def get_inmate_data():
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data



def get_and_parse_inmate_rows():
    from data_helper import get_html
    txt = get_html()
    soup = BeautifulSoup(txt, 'lxml')
    tags = []
    for tag in soup.select('tr'):
        tags.append(tag)
    inmates = []
    for x in range(1,len(tags)):
        inmates.append(tags[x])
    return inmates


def wrangle_inmate_data_from_tag(rowtag):
    tags = []
    dic = {}
    for tag in rowtag.select('td'):
        tags.append(tag)
    dic['tdcj_id'] = tags[0].text.strip()
    dic['url'] = make_absolute_url(tags[1].select('a')[0].get('href'))
    dic['last_name'] = tags[2].text.strip()
    dic['first_name'] = tags[3].text.strip()
    dic['birthdate'] = txdate_to_iso(tags[4].text.strip())
    dic['gender'] = tags[5].text.strip()
    dic['race'] = tags[6].text.strip()
    dic['date_received'] = txdate_to_iso(tags[7].text.strip())
    dic['date_offense'] = txdate_to_iso(tags[9].text.strip())
    dic['years_before_death_row'] = calc_years_diff(dic['date_offense'], dic['date_received'])
    dic['county'] = tags[8].text.strip()

    aao = calc_years_diff(dic['birthdate'], dic['date_offense'])
    if (aao % 1 != 0):
        aao += 1
    dic['age_at_offense'] = int(aao)

    return dic