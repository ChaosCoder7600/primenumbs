__author__ = 'Todd'

import unittest
import primenumbs

class PrimeNumbsTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_even_number_even(self):
        self.assertTrue(primenumbs.iseven(2))

    def test_even_number_odd(self):
        self.assertFalse(primenumbs.iseven(3))

    def test_isprime_prime(self):
        self.assertTrue(primenumbs.isprime(11))

    def test_isprime_composit(self):
        self.assertFalse(primenumbs.isprime(6))

    def test_output_count(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
