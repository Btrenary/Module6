import unittest
from more_functions import string_functions

class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual('BradyBradyBradyBradyBrady', string_functions.multiply_string('Brady', 5))


if __name__ == '__main__':
    unittest.main()
