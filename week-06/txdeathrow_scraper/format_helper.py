from datetime import datetime
from urllib.parse import urljoin
import data_helper

def txdate_to_iso(datestr):
    origlist = datestr.split('/')
    newstr = ""
    if len(origlist[2]) == 2:
        origlist[2] = '19' + origlist[2]
    newlist = [origlist[2], origlist[0], origlist[1]]
    newstr = '-'.join(newlist)
    return newstr


def calc_years_diff(start_date, end_date):
    start2 = datetime.strptime(start_date, '%Y-%m-%d')
    end2 = datetime.strptime(end_date, '%Y-%m-%d')
    dif = end2 - start2
    change = dif.days/365
    return round(change, 1)


def make_absolute_url(href):
    origin = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
    return urljoin(origin, href)