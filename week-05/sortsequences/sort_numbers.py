from datastubs import NUMBER_LIST

def reverse_numerical_order():
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
    return sorted(NUMBER_LIST)


def as_absolute_value():
    return sorted(NUMBER_LIST, key=lambda x: abs(x))


def as_inverse_number():
    return sorted(NUMBER_LIST, key=lambda x: (1/x))