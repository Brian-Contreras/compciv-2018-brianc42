#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]


def foo_hello():
    return type(ez_list)


def foo_a():
    return ez_list[0]


def foo_b():
    return (ez_list[1] + ez_list[3])


def foo_c():
    return ez_list[-1]


def foo_cx():
    return type(ez_list[-2])
    

def foo_d():
    return ez_list[-2][-1]


def foo_e():
    return len(ez_list)


def foo_f():
    contents = ez_list[5]
    string = ""
    iterator = 0
    max = len(contents)
    while iterator < max:
        string += contents[iterator]
        iterator = iterator + 1
        if iterator != max:
            string += ';'
    return string


def foo_g():
    l = []
    for n in range(1,5):
        l.append(ez_list[n])
    return l


def foo_h():
    l = []
    for n in range(1,4):
        l.append(ez_list[-n])
    return l