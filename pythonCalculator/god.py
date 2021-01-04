
#the file called god because the name "operator" can't be used
#god can translate substrings to number by getting only 1 index.
#god can make operations with given the index of the operator

#god holds a dictionary of the all the operators and their strengths
import finder

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5, ')': 99}


#-------------------------------------------------------operations   V


def middle_operator_range(eq, i):
    if not is_known_operator(eq[i]):
        raise Exception("not known operator")

    if i == 0 or i == len(eq) - 1:
        print("middle operator at the edge of the equation")
        return -1, -1

    if not (is_digit(eq[i - 1]) and is_digit(eq[i + 1])):
        print("middle operators in row")
        return -1, -1

    start = finder.find_start_of_number(eq, i-1)
    end = finder.find_end_of_number(eq, i+1)
    return start, end


def right_operator_range(eq, i):
    if not is_known_operator(eq[i]):
        raise Exception("not known operator")
    if i == 0:
        print("right operator at the left of the equation")
        return -1, -1
    if not (True):
        print("none number to the left of the operator (right operator)")
        return -1, -1
    start = finder.find_start_of_number(eq, i-1)
    end = i
    return start, end


def make_middle_operation(eq, i):
    if not is_known_operator(eq[i]):
        raise Exception("not known operator")

    start, end = middle_operator_range(eq, i)
    s1, s2, s3 = split_to_3_string(eq, start, end)
    num1 = num_from_index(eq, i - 1)
    num2 = num_from_index(eq, i + 1)
    res = operate(num1, num2, eq[i])
    return s1 + str(res) + s3


def make_right_operation(eq, i):
    if not is_known_operator(eq[i]):
        raise Exception("not known operator")
    start, end = right_operator_range(eq, i)
    s1, s2, s3 = split_to_3_string(eq, start, end)
    num1 = num_from_index(eq, i - 1)
    res = operate(num1, 0, eq[i])
    return s1 + str(res) + s3


def factorial(num):
    if num < 0:
        print("factorial on negative number")
        return None
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def operate(num1, num2, op):

    #operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5, ')':99}
    if op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2
    elif op == '^':
        return num1 ** num2
    elif op == '@':
        return (num1 + num2)/2
    elif op == '$':
        return max(num1, num2)
    elif op == '&':
        return min(num1, num2)
    elif op == '%':
        return num1 % num2
    elif op == '/':
        return num1 / num2
    elif op == '!':
        return factorial(num1)
    else:
        return None


def split_to_3_string(eq, start, end):
    s1 = substring_by_range(eq, 0, start-1)
    s2 = substring_by_range(eq, start, end)
    s3 = substring_by_range(eq, end + 1, len(eq) - 1)

    return s1, s2, s3

#-------------------------------------------------------operations   ^


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


#
#
def substring_by_range(eq, first, last):
    s = ""
    for i in range(first, last + 1):
        s += eq[i]
    return s


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
    if not(finder.is_digit_or_dot(eq[i])):
        raise Exception("char not a digit or \'.\', char: \'" + str(eq[i]) + "\'  index: " + str(i))
    first, last = find_range_of_a_number(eq, i)
    s = ""
    for j in range(first, last + 1):
        s += eq[j]
    return float(s)


#enter: gets a string eq and index i given that eq[i] is an operator
#exit: returns a string after the operation has been made
def make_operation(eq, i):
    #spot if it's middle operation, left or right
    #act accordingly
    s = kind_of_operator(eq[i])
    if s == "mid":
        return make_middle_operation(eq, i)
    if s == "right":
        return make_right_operation(eq, i)


def kind_of_operator(c):
    #operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5, ')':99}
    if not is_known_operator(c):
        raise Exception("not known operator")
    if c == '+' or c == '*' or c == '^' or c == '@' or c == '$' or c == '&' or c == '%' or c == '/':
        return "mid"
    if c == '!' or c == '~':
        return "right"
    if c == '-':
        return "minus"
    if c == ')':
        return "closer"


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


def strength_of(c):
    if not is_known_operator(c):
        raise Exception("not known operator")
    return operators[c]
