import unittest
from roman_numerals.roman_to_decimal import *


class UnitTests(unittest.TestCase):
    def test_direct_values(self):
        self.assertEqual(1, roman_to_decimal('I'))
        self.assertEqual(5, roman_to_decimal('V'))
        self.assertEqual(10, roman_to_decimal('X'))
        self.assertEqual(50, roman_to_decimal('L'))
        self.assertEqual(100, roman_to_decimal('C'))
        self.assertEqual(500, roman_to_decimal('D'))
        self.assertEqual(1000, roman_to_decimal('M'))

    def test_repeated_values(self):
        self.assertEqual(2, roman_to_decimal('II'))
        self.assertEqual(3, roman_to_decimal('III'))
        self.assertEqual(20, roman_to_decimal('XX'))
        self.assertEqual(30, roman_to_decimal('XXX'))
        self.assertEqual(200, roman_to_decimal('CC'))
        self.assertEqual(300, roman_to_decimal('CCC'))
        self.assertEqual(2000, roman_to_decimal('MM'))
        self.assertEqual(3000, roman_to_decimal('MMM'))

    def test_different_subtraction_cases(self):
        self.assertEqual(49, roman_to_decimal('XLIX'))
        self.assertEqual(44, roman_to_decimal('XLIV'))
        self.assertEqual(444, roman_to_decimal('CDXLIV'))
        self.assertEqual(999, roman_to_decimal('CMXCIX'))
        self.assertEqual(257, roman_to_decimal('CCLVII'))

    def test_non_valid_repeated_values(self):
        self.assertRaises(NonValidRepeatedRomanCharacterException, roman_to_decimal('VV'))
        self.assertRaises(NonValidRepeatedRomanCharacterException, roman_to_decimal('LL'))
        self.assertRaises(NonValidRepeatedRomanCharacterException, roman_to_decimal('DD'))

    def test_non_valid_redundant_values(self):
        self.assertRaises(RedundantRomanNumberCombination, roman_to_decimal('IXI'))
        self.assertRaises(RedundantRomanNumberCombination, roman_to_decimal('XCX'))
        self.assertRaises(RedundantRomanNumberCombination, roman_to_decimal('CMC'))

    def test_roman_number_repeated_more_than_three_times_in_a_row(self):
        self.assertRaises(MoreThanFourRepetitionsException, roman_to_decimal('IIII'))
        self.assertRaises(MoreThanFourRepetitionsException, roman_to_decimal('XXXX'))
        self.assertRaises(MoreThanFourRepetitionsException, roman_to_decimal('CCCC'))
        self.assertRaises(MoreThanFourRepetitionsException, roman_to_decimal('MMMM'))


if __name__ == '__main__':
    unittest.main()
