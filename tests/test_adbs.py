# -*- coding: utf-8 -*-

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import adbs


class ADBSTestSuite(unittest.TestCase):
    def test_ad_to_bs(self):
        assert True

    def test_bs_to_ad(self):
        expectedDate = {
            'year': 2015,
            'month': 7,
            'strMonth': 'July',
            'strShortMonth': 'Jul',
            'day': 19,
            'dayOfWeek': 0,
            'strDayOfWeek': 'Sunday',
            'strShortDayOfWeek': 'Sun'
        }
        assert adbs.bs_to_ad('2072/4/3') == expectedDate


if __name__ == '__main__':
    unittest.main()
