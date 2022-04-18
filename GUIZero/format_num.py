def format_num(num, sep_char=",", chars=3):

    if not str(num).isdigit():
        return num

    if chars == 0:
        return num

    s = str(num)

    new = ""

    # Reverse the string

    for c in range(1, len(s)+1):

        new += s[-c]

    sep = ""

    # Reverse the separator

    for m in range(1, len(sep_char) + 1):

        sep += sep_char[-m]

    final = ""

    # Loop through the reversed string and add separators to every third character

    for i in range(len(new)):

        if i % chars == 0 and i != 0:

            final += sep + new[i]

        else:

            final += new[i]

    return_str = ""

    # Reverse the full string and return

    for x in range(1, len(final) + 1):

        return_str += final[-x]

    return return_str


def format_num_2(num, lst_chars=None, sep=","):

    if lst_chars is None:
        lst_chars = [3, 2, ...]

    if not isinstance(sep, str):
        sep = ","

    if type(lst_chars) not in [type(list()), type(tuple())]:
        return -1

    for i in lst_chars:
        if not isinstance(i, int) and i is not ...:
            return -2
        if i is not ...:
            if i <= 0:
                return -3

    if not str(num).isdigit():
        return -4

    if not len(lst_chars):
        return -5

    s = ''.join(reversed(list(str(num))))

    if lst_chars[-1] is not ...:
        if sum(lst_chars) < len(s):
            return -6

    lst_index = 0
    char_index = 0
    new_num = ''

    for index in range(len(s)):

        while lst_chars[lst_index] is ...:
            lst_index -= 1

        new_num += s[index]

        if char_index == lst_chars[lst_index] - 1:

            new_num += sep
            char_index = 0
            lst_index += 1

        else:
            char_index += 1

    if new_num[-len(sep):] == sep:
        new_num = new_num[:-len(sep)]

    return ''.join(reversed(list(new_num)))


def estimate(num):

    # Raise error if the argument is not in the desired format
    if not str(num).isdigit():
        return num

    s = str(num)
    num = int(num)

    digits = {
        13: [1, " trillion"],
        12: [100, " billion"],
        11: [10, " billion"],
        10: [1, " billion"],
        9: [100, " million"],
        8: [10, " million"],
        7: [1, " million"],
        6: [100, " thousand"],
        5: [10, " thousand"],
        4: [1, " thousand"],
    }

    for i in digits.keys():
        if len(s) >= i:
            ext = digits[i]
            break
    else:
        return ""
    
    return "(~" + str(round(((num/(10**(len(s)-1))) * ext[0]), 1)) + ext[1] + ")"
