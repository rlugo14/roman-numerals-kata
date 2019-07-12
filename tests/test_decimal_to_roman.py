import unittest
from roman_numerals.decimal_to_roman import decimal_to_roman


class UnitTests(unittest.TestCase):

    def test_direct_values(self):
        self.assertEqual('I', decimal_to_roman(1))
        self.assertEqual('IV', decimal_to_roman(4))
        self.assertEqual('V', decimal_to_roman(5))
        self.assertEqual('IX', decimal_to_roman(9))
        self.assertEqual('X', decimal_to_roman(10))
        self.assertEqual('XL', decimal_to_roman(40))
        self.assertEqual('L', decimal_to_roman(50))
        self.assertEqual('XC', decimal_to_roman(90))
        self.assertEqual('C', decimal_to_roman(100))
        self.assertEqual('CD', decimal_to_roman(400))
        self.assertEqual('D', decimal_to_roman(500))
        self.assertEqual('CM', decimal_to_roman(900))
        self.assertEqual('M', decimal_to_roman(1000))

    def test_repeated_values(self):
        self.assertEqual('II', decimal_to_roman(2))
        self.assertEqual('III', decimal_to_roman(3))
        self.assertEqual('XX', decimal_to_roman(20))
        self.assertEqual('XXX', decimal_to_roman(30))
        self.assertEqual('CC', decimal_to_roman(200))
        self.assertEqual('CCC', decimal_to_roman(300))
        self.assertEqual('MM', decimal_to_roman(2000))
        self.assertEqual('MMM', decimal_to_roman(3000))

    def test_do_not_repeat_more_than_three(self):
        self.assertEqual('XLIX', decimal_to_roman(49))
        self.assertEqual('XLIV', decimal_to_roman(44))
        self.assertEqual('CDXLIV', decimal_to_roman(444))


if __name__ == '__main__':
    unittest.main()
