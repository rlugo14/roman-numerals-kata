from collections import OrderedDict


class NonValidRepeatedRomanCharacterException(Exception):
    pass


class MoreThanFourRepetitionsException(Exception):
    pass


class RedundantRomanNumberCombination(Exception):
    pass


roman_dictionary = OrderedDict([
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
])


def roman_to_decimal(input_roman):
    output_decimal = 0
    analysed_string = ''
    warning_flag = ''
    repeated_roman_key = 0
    input_roman = input_roman.upper()
    input_length = len(input_roman)
    roman_keys = list(roman_dictionary.keys())

    while input_length > 0:
        target_roman_key = input_roman[0]
        input_roman = input_roman[1:]
        target_roman_index = roman_keys.index(target_roman_key)
        case = 'ones case'

        if target_roman_index % 2 != 0:
            case = 'fives case'

        try:

            if target_roman_key == warning_flag:
                output_decimal = None
                raise RedundantRomanNumberCombination

            next_roman_key = input_roman[0]

            target_decimal_value = roman_dictionary[target_roman_key]
            next_decimal_value = roman_dictionary[next_roman_key]

            if case == 'ones case':
                if target_decimal_value > next_decimal_value:
                    output_decimal += target_decimal_value
                    analysed_string_length = len(analysed_string)
                    if analysed_string_length > 0:
                        output_decimal += analysed_string_length * roman_dictionary[analysed_string[0]]
                    repeated_roman_key = 0

                elif target_decimal_value < next_decimal_value:
                    output_decimal += next_decimal_value - target_decimal_value
                    input_roman = input_roman[1:]
                    repeated_roman_key = 0
                    warning_flag = target_roman_key

                else:
                    analysed_string += target_roman_key
                    repeated_roman_key += 1
                    if repeated_roman_key > 2:
                        output_decimal = None
                        raise MoreThanFourRepetitionsException

            elif case == 'fives case':
                if target_decimal_value > next_decimal_value:
                    output_decimal += target_decimal_value

                else:
                    output_decimal = None
                    raise NonValidRepeatedRomanCharacterException

        except (ValueError, IndexError):
            if len(analysed_string) == 0:
                output_decimal += roman_dictionary[target_roman_key]
            elif target_roman_key == analysed_string[0]:
                analysed_string += target_roman_key
                output_decimal += len(analysed_string) * roman_dictionary[analysed_string[0]]
            else:
                output_decimal += roman_dictionary[target_roman_key]
                output_decimal += len(analysed_string) * roman_dictionary[analysed_string[0]]

        except NonValidRepeatedRomanCharacterException:
            print('A valid roman number does not contain "V", "L" or "D" together')
            break

        except MoreThanFourRepetitionsException:
            print('A valid roman number does not contain a same character more than three times in a row')
            break

        except RedundantRomanNumberCombination:
            print('Roman number combinations like "IXI", "XCX" and "CMC" are redundant and therefore invalid')
            break

        input_length = len(input_roman)

    return output_decimal


if __name__ == '__main__':
    print(roman_to_decimal('vv'))
