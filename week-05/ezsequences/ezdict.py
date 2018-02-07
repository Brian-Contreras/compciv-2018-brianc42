
ez_dict = {'birthdate': '1946-06-14', 'party': 'Republican',
           'gender': 'M',
           'identifiers': {
             'twitter': 'realDonaldTrump',
             'fec': 'P80001571',
           },
           'name': {'first': 'Donald', 'last': 'Trump'},
           'birthplace': {'state': 'NY', 'city': 'New York City'},
           'children': ['Donald', 'Ivanka',
                        'Eric', 'Tiffany', 'Barron'],
            'spouse': 'Melania Trump',
            'terms': [{'start_date': '2017-01-20',
                     'end_date': '2021-01-20'}]
           }


def foo_hello():
    return type(ez_dict)


def foo_a():
    return ez_dict['spouse']



def foo_b():
    return ez_dict['name']['first']


def foo_bx():
    return type(ez_dict['terms'])


def foo_c():
    string1 = ""
    string1 += ez_dict['name']['last']
    string1 += ", "
    string1 += ez_dict['name']['first']
    return string1


def foo_d():
    iterator = 0
    for elem in ez_dict:
        iterator += 1
    return iterator


def foo_e():
    count = 0
    for elem in ez_dict['children']:
        count += 1
    return count


def foo_f():
    return ez_dict['children'][-1]


def foo_g():
    string1 = ""
    list1 = []
    list1.append(ez_dict['spouse'])
    for elem in ez_dict['children']:
        list1.append(elem)
    iterator = 0
    max = len(list1)
    while iterator < max:
        string1 += list1[iterator]
        iterator += 1
        if iterator != max:
            string1 += ','
    return string1


def foo_h():
    return(ez_dict['terms'][0]['start_date'])


def foo_i():
    import dateutil.parser
    from dateutil.relativedelta import relativedelta
    term = ez_dict['terms'][0]
    ty = dateutil.parser.parse(term['end_date'])
    tx = dateutil.parser.parse(ez_dict['birthdate'])
    diff = relativedelta(ty, tx)
    return diff.years


def foo_j():
    fec = ez_dict['identifiers']['fec']
    url = "http://docquery.fec.gov/cgi-bin/fecimg/?" + fec
    return url