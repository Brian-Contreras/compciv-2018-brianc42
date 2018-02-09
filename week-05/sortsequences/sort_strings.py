from datastubs import STRING_LIST


def reverse_alpha():
    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    return sorted(STRING_LIST, key=lambda x: (x.lower()))


def by_longest_length():
    return sorted(STRING_LIST, key=lambda x: len(x))


def filter_and_sort_number_strings():
    newList = []
    for n in STRING_LIST:
        if n.isnumeric():
            newList.append(n)
    return sorted(newList, key=lambda x: str(x))


def filter_and_sort_number_strings_as_numbers():
    newList = []
    for n in STRING_LIST:
        if n.isnumeric():
            newList.append(n)
    return sorted(newList, key=lambda x: int(x))