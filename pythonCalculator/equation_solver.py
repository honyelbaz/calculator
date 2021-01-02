import god


# checks if the string is even worth trying to solve.
# (the string can be easily classified as invalid with several reasons)


def is_valid(eq):
    # not valid if...
    # if there are no numbers (or even empty)
    # if the amount of left brackets is not equal to the amount of right brackets
    # if two dot are one after another or a dot is not in middle of a number

    msg = ""
    if len(eq) == 0:
        msg += "empty input. "
        return False

    numbers_counter = 0
    left_bracket_counter = 0
    right_bracket_counter = 0

    i = 0
    while i < len(eq):
        if god.is_digit(eq[i]):
            num, i = god.num_from_index_and_new_index(eq, i)
            numbers_counter += 1
            continue

        elif eq[i] == '(':
            left_bracket_counter += 1

        elif eq[i] == ')':
            right_bracket_counter += 1

        elif eq[i] == ' ' or eq[i] == chr(9):
            pass

        elif eq[i] == '.':
            if not god.check_if_dot_in_suitable_place(eq, i):
                msg += "dot not in suitable place. "

        elif not (god.is_known_operator(eq[i])):
            print("invalid character found. ")
            return False

        i += 1

    if numbers_counter == 0:
        msg += "no numbers in the string. "

    if left_bracket_counter != right_bracket_counter:
        msg += "amount of left brackets is not equal to the amount of right brackets. "

    if msg == "":
        return True
    else:
        print(msg)
        return False


while True:
    print(is_valid(input()))
