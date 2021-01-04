import god

#--------------------finder---------------


#skiping all the blank chars and returning the index of the first char found
def find_char_to_the_right(eq, i):
    i += 1
    while i < len(eq) and (eq[i] == ' ' or eq[i] == chr(9)):
        i += 1
    return i



#
#
def left_operator_range(eq, i):
    pass


#
#
def right_operator_range(eq, i):
    pass


def minus_operator_range(eq, i):
    pass


def split_to_3_strings_by_operator(eq, i):
    #identafiy is it middle opr, left or right

    #minus has a special treatment
    pass


def is_digit_or_dot(c):
    return god.is_digit(c) or c == '.'


def find_start_of_number(eq, i):
    if not is_digit_or_dot(eq[i]):
        raise Exception("not digit or number")
    while i >= 0 and is_digit_or_dot(eq[i]):
        i -= 1
    i += 1
    return i


def find_end_of_number(eq, i):
    if not is_digit_or_dot(eq[i]):
        raise Exception("not digit or number")
    while i < len(eq) and is_digit_or_dot(eq[i]):
        i += 1
    i -= 1
    return i


def find_strongest_operator(eq):
    maxi = -1
    maxs = -1
    for i in range(len(eq)):
        if god.is_known_operator(eq[i]) and god.strength_of(eq[i]) > maxs:
            maxi = i
            maxs = god.strength_of(eq[i])
    return maxi
