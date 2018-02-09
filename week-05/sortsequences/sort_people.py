from datastubs import PEOPLE_LIST

def longest_name():
    def foolen(p):
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)


def youngest():
    return sorted(PEOPLE_LIST, key=lambda x: x['age'])


def oldest():
    return sorted(PEOPLE_LIST, reverse=True, key=lambda x: x['age'])


def name_reverse_alpha():
    return sorted(PEOPLE_LIST, reverse=True, key=lambda x: x['name'])


def country_then_age():
    return sorted(PEOPLE_LIST, key=lambda x: [x['country'], x['age']])