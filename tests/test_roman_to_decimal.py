import unittest
# from roman_numerals.roman_to_decimal import roman_to_decimal


class UnitTests(unittest.TestCase):
    def test_direct_values(self):
        self.assertEqual(1, roman_to_decimal('I'))
        self.assertEqual(4, roman_to_decimal('IV'))
        self.assertEqual(5, roman_to_decimal('V'))
        self.assertEqual(9, roman_to_decimal('IX'))
        self.assertEqual(10, roman_to_decimal('X'))
        self.assertEqual(40, roman_to_decimal('XL'))
        self.assertEqual(50, roman_to_decimal('L'))
        self.assertEqual(90, roman_to_decimal('XC'))
        self.assertEqual(100, roman_to_decimal('C'))
        self.assertEqual(400, roman_to_decimal('CD'))
        self.assertEqual(500, roman_to_decimal('D'))
        self.assertEqual(900, roman_to_decimal('CM'))
        self.assertEqual(1000, roman_to_decimal('M'))

    def test_repeated_values(self):
        self.assertEqual(2, roman_to_decimal('II'))
        self.assertEqual(3, roman_to_decimal('III'))
        self.assertEqual(20, roman_to_decimal('XX'))
        self.assertEqual(30, roman_to_decimal('XXX'))
        self.assertEqual(100, roman_to_decimal('CC'))
        self.assertEqual(300, roman_to_decimal('CCC'))
        self.assertEqual(2000, roman_to_decimal('MM'))
        self.assertEqual(3000, roman_to_decimal('MMM'))

    def test_do_not_repeat_more_than_three(self):
        self.assertEqual(49, roman_to_decimal('XLIX'))
        self.assertEqual(44, roman_to_decimal('XLIV'))
        self.assertEqual(944, roman_to_decimal('CDXLIV'))


if __name__ == '__main__':
    unittest.main()