from collections import OrderedDict

roman_dictionary = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
])


def decimal_to_roman(input_decimal):
    roman_string = ''

    while input_decimal != 0:
        for decimal, roman in roman_dictionary.items():
            if input_decimal in roman_dictionary:
                roman_string += roman_dictionary.get(input_decimal)
                input_decimal = 0
            if input_decimal > decimal:
                times_to_repeat = int(input_decimal / decimal)
                roman_string += (times_to_repeat * roman)
                input_decimal -= times_to_repeat * decimal
                continue
    return roman_string


if __name__ == '__main__':
    print(decimal_to_roman(44))
