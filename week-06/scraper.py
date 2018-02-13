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
    dic['tdcj_id'] = tags[0]
    dic['url'] = tags[1].get('href')
    dic['last_name'] = tags[2]
    dic['first_name'] = tags[3]
    dic['birthdate'] = txdate_to_iso(tags[4])
    dic['gender'] = tags[5]
    dic['race'] = tags[6]
    dic['date_received'] = txdate_to_iso(tags[7])
    dic['date_offense'] = tags[9]
    dic['age_at_offence'] = calc_years_diff(txdate_to_iso(tags[9]), txdate_to_iso(tags[4]))
    dic['years_before_death_row'] = calc_years_diff(txdate_to_iso(tags[7]), txdate_to_iso(tags[9]))
    



    """
    Args:
        rowtag: a BeautifulSoup <Tag> object, ostensibly representing a table row
            from a parsed Texas death row HTML table, e.g.
            <tr>
            <td>999608</td>
            <td align="center"><a href="dr_info/hudsonwilliam.html" title="Offender Information for William Hudson">Offender Information</a></td>
            <td>Hudson</td>
            <td>William</td>
            <td>07/03/1982</td>
            <td align="center">M</td>
            <td>White</td>
            <td>11/16/2017</td>
            <td>Anderson</td>
            <td>11/14/2015</td>
            </tr>
    Returns:
        <dict>: A dictionary object that contains some of the values in
            the HTML, with formatting where standardization is needed --
            e.g. for dates and for the inmate's URL (absolute vs relative)
            and some derived attributes, e.g. 'age_at_offense'
            The value for 'url' should be an absolute URL, i.e. a valid
               URL on the Web, not a relative one.
            'birthdate', date_received', 'date_offense' should be in 'YYYY-MM-DD'
                format
            All values are strings except for:
               'age_at_offense', which is an integer derived from birthdate and
                                 date of offense
               'years_before_death_row', which is a float
                              (rounded to nearest tenth) derived
                              from date of offense and date received, i.e.
                              number of years between commission of crime and entering
                              death row.
        e.g.
            {
                'tdcj_id': '999608',
                'url': 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html',
                'last_name': 'Hudson',
                'first_name': 'William',
                'birthdate': '1982-07-03',
                'gender': 'M',
                'race': 'White',
                'date_received': '2017-11-16',
                'date_offense': '2015-11-14',
                'age_at_offence': 33,
                'years_before_death_row': 2.0
            }
    """
    ### fill in yourself
    ### (this one will be pretty long, though it's mostly tedious/repetitive steps)