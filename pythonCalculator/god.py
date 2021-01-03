
#the file called god because the name "operator" can't be used
#god can translate substrings to number by getting only 1 index.
#god can make operations with given the index of the operator

#god holds a dictionary of the all the operators and their strengths
operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5}


# #returns a string after made the sum operation on it (given index of operator)
# def make_sum(eq, i):
#     #if it's the first char raise exception
#     if i == 0:
#         raise Exception("\'+\' cannot be first character")
#     # if it's the last char raise exception
#     if i == len(eq):
#         raise Exception("\'+\' cannot be last character")
#     # if it's not '+' raise exception
#     if eq[i] != '+':
#         raise Exception("the operator is not \'+\'")
#
#     #save the original index
#     index = i
#
#     i = index - 1
#     #find the first none blank char to the left of '+'
#     while i >= 0 and (eq[i] == ' ' or eq[i] == chr(9)):
#         i -= 1
#     # if found that '+' is actually the first char then raise exception
#     if i == 0:
#         raise Exception("\'+\' cannot be first character")
#     #if the first char is not a digit of a number return false
#     if not is_digit(eq[i]):
#         return eq, False
#     #num1 = to the number found
#     num1 = num_from_index(eq, i)
#
#     # i = to the original index
#     i = index + 1
#     #find the first none blank char to the right of '+'
#     while i < len(eq) and (eq[i] == ' ' or eq[i] == chr(9)):
#         i += 1
#     # if found that '+' is actually the last char then raise exception
#     if i == len(eq):
#         raise Exception("\'+\' cannot be last character")
#
#     #num2 = to the number found
#     num2 = num_from_index(eq, i)
#
#     return num1 + num2
#
#
# def make_sub(eq, i):
#     pass
#
#
# def make_mul(eq, i):
#     pass
#
#
# def make_div(eq, i):
#     pass
#
#
# def make_pow(eq, i):
#     pass
#
#
# def make_neg(eq, i):
#     pass
#
#
# def make_modulus(eq, i):
#     pass
#
#
# def make_factorial(eq, i):
#     pass
#
#
# def make_avg(eq, i):
#     pass
#
#
# def make_max(eq, i):
#     pass
#
#
# def make_min(eq, i):
#     pass
#

def make_middle_operation(eq, i):
    pass


def make_sum(num1, num2):
    pass


#enter: get a char
#exit: returns true if the char is a digit else returns false
def is_digit(c):
    return '0' <= c <= '9'


#
#
def find_range_of_a_number(eq, i):
    #if it's not a character of a number than it's not logical
    if not(is_digit(eq[i]) or eq[i] == '.'):
        raise Exception("the index is not in a number")

    #save the original index
    index = i

    #go to the left edge of the number
    while i >= 0 and (is_digit(eq[i]) or eq[i] == '.'):
        i -= 1
    beginning = i + 1
    i = index

    #go tp the right edge of the number
    while i < len(eq) and (is_digit(eq[i]) or eq[i] == '.'):
        i += 1
    finish = i - 1

    return beginning, finish


#enter:gets a char
#exitreturns if it's in the dictionary of the operators
def is_known_operator(c):
    return operators.keys().__contains__(c)


#enter: gets a string representing an equation and index of first char of number
#exit: assembles a number , returns the number and the index of after the number
def num_from_index_and_new_index(eq, i):

    if not(is_digit(eq[i]) or eq[i] == '.'):
        raise Exception("char not a digit or a dot, char: \'" + str(eq[i]) + "\'  index: " + str(i))

    num = 0
    while i < len(eq) and is_digit(eq[i]):
        num *= 10
        num += int(eq[i])
        i += 1

    x = -1
    after_dot = 0
    if i < len(eq):
        if eq[i] == '.':
            i += 1
            while i < len(eq) and is_digit(eq[i]):
                after_dot += int(eq[i]) * (10 ** x)
                i += 1
                x -= 1
    num += after_dot
    return num, i


#enter:gets a string and index of any digit in the number
#exit: returns only the num
def num_from_index(eq, i):
    if not(is_digit(eq[i]) or eq[i] == '.'):
        raise Exception("char not a digit or \'.\', char: \'" + str(eq[i]) + "\'  index: " + str(i))
    first, last = find_range_of_a_number(eq, i)
    s = ""
    for j in range(first, last + 1):
        s += eq[j]
    return float(s)


#enter: gets a string eq and index i given that eq[i] is an operator
#exit: returns a string after the operation has been made
def make_operation(eq, i):
    pass


#enter:gets string and index of a dot
#exit:returns true if the dot is in suitable place, else false
def check_if_dot_in_suitable_place(eq, i):
    if eq[i] != '.':
        raise Exception("char is not a dot")

    if i == 0:
        return False
    if i == len(eq):
        return False

    index = i

    i = index - 1
    while i >= 0 and (eq[i] == ' ' or eq[i] == chr(9)):
        i -= 1
    if i < 0:
        return False
    if not is_digit(eq[i]):
        return False

    i = index + 1
    while i < len(eq) and (eq[i] == ' ' or eq[i] == chr(9)):
        i += 1
    if i >= len(eq):
        return False
    if not is_digit(eq[i]):
        return False

    beginning, finish = find_range_of_a_number(eq, index)
    dot_count = 0
    for j in range(beginning, finish):
        if eq[j] == '.':
            dot_count += 1
    if dot_count > 1:
        return False

    return True
