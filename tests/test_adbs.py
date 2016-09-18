# -*- coding: utf-8 -*-

import sys
import os
import unittest
from nose.tools import assert_equals
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import adbs


class ADBSTestSuite(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_ad_to_bs(self):
        expected_date = {
            'ne': {
                'year': '२०७२',
                'month': '४',
                'day': '१६',
                'str_month': 'श्रावण',
                'str_short_month': 'श्रा',
                'day_of_week': '५',
                'str_day_of_week': 'शनिवार',
                'str_short_day_of_week': 'शनि',
                'str_min_day_of_week': 'श'
            },
            'en': {
                'year': 2072,
                'month': 4,
                'day': 16,
                'str_month': 'Shrawan',
                'str_short_month': 'Shra',
                'day_of_week': 5,
                'str_day_of_week': 'Shanibaar',
                'str_short_day_of_week': 'Shani',
                'str_min_day_of_week': 'Sha'
            }
        }
        assert_equals(adbs.ad_to_bs('2015/8/1'), expected_date)
        expected_date = {
            'ne': {
                'year': '२०७३',
                'month': '६',
                'day': '१५',
                'str_month': 'आश्विन',
                'str_short_month': 'आश',
                'day_of_week': '५',
                'str_day_of_week': 'शनिवार',
                'str_short_day_of_week': 'शनि',
                'str_min_day_of_week': 'श'
            },
            'en': {
                'year': 2073,
                'month': 6,
                'day': 15,
                'str_month': 'Ashwin',
                'str_short_month': 'Ash',
                'day_of_week': 5,
                'str_day_of_week': 'Shanibaar',
                'str_short_day_of_week': 'Shani',
                'str_min_day_of_week': 'Sha'
            }
        }
        assert_equals(adbs.ad_to_bs('2016/10/1'), expected_date)

    def test_bs_to_ad(self):
        expected_date = {
            'year': 2015,
            'month': 7,
            'str_month': 'July',
            'str_short_month': 'Jul',
            'day': 19,
            'day_of_week': 6,
            'str_day_of_week': 'Sunday',
            'str_short_day_of_week': 'Sun'
        }
        assert_equals(adbs.bs_to_ad('2072/4/3'), expected_date)
        expected_date = {
            'year': 2016,
            'month': 10,
            'str_month': 'October',
            'str_short_month': 'Oct',
            'day': 1,
            'day_of_week': 5,
            'str_day_of_week': 'Saturday',
            'str_short_day_of_week': 'Sat'
        }
        assert_equals(adbs.bs_to_ad('2073/6/15'), expected_date)


if __name__ == '__main__':
    unittest.main()
