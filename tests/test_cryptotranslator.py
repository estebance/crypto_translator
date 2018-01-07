# run these tests
# python -m unittest tests/test_cryptotranslator
import unittest
import cryptotranslator

class TestCryptotranslator(unittest.TestCase):

    # configure the tests
    def setUp(self):
        self._exchange = 'GDAX'
        self._pair = 'LTC-BTC'

    def test_get_product_standard(self):
        normalized_name = cryptotranslator.get_product_standard('LTC-BTC', 'GDAX')
        self.assertEqual(normalized_name, 'LTC_BTC')
