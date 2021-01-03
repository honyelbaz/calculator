import god


#
#
# def split_to_3_strings_by_operator(eq, i):
#     if not god.is_known_operator(eq[i]):
#         raise Exception("char not a known operator")
#
#     s1 = ""
#     s2 = ""
#     s3 = ""
#     first = i
#     last = i
#
#     index = i
#
#     i = index - 1
#     while i >= 0 and (eq[i] == ' ' or eq[i] == chr(9)):
#         i -= 1
#
#     if i < 0:
#         i += 1
#
#     if god.is_digit(eq[i]):
#         first, last = god.find_range_of_a_number(eq, i)
#     else:
#         first = i + 1
#
#     i = index + 1
#     while i < len(eq) and (eq[i] == ' ' or eq[i] == chr(9)):
#         i += 1
#
#     if i >= len(eq):
#         i -= 1
#     if god.is_digit(eq[i]):
#         dummy, last = god.find_range_of_a_number(eq, i)
#     else:
#         last = i - 1
#     return first, last
#
#
# split_to_3_strings_by_operator("235++2355+235235", 3)

#skiping all the blank chars and returning the index of the first char found
def find_char_to_the_right(eq, i):
    i += 1
    while i < len(eq) and (eq[i] == ' ' or eq[i] == chr(9)):
        i += 1
    return i


#skiping all the blank chars and returning the index of the first char found
def find_char_to_the_left(eq, i):
    i -= 1
    while i >= 0 and (eq[i] == ' ' or eq[i] == chr(9)):
        i -= 1
    return i


def middle_operator_range(eq, i):
    if i < 0 or i >= len(eq):
        print("middle operator at the edge of the equation")
        return -1, -1
    str.strip()


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


