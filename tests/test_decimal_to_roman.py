import unittest
import mock
from roman_numerals.decimal_to_roman import *


class UnitTests(unittest.TestCase):

    def test_is_direct_value(self):
        self.assertTrue(is_direct_value(1))
        self.assertFalse(is_direct_value(2))

    def test_input_decimal(self):
        with mock.patch('builtins.input', return_value="1"):
            self.assertEquals(receive_decimal(), 1)


if __name__ == '__main__':
    unittest.main()
