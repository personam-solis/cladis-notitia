#!/usr/bin/env python3

import unittest
from datetime import datetime, timedelta
import ingest_data as test_module

gdacs_url = 'https://gdacs.org/xml/rss.xml'

fema_url = 'https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries'
check_date = datetime.now() - timedelta(days=365)
formatted_date = check_date.strftime("%Y-%m-%d")

emdat_file = "dummy_data/EM-DAT_DUMMY.csv"


"""
All GDACS Tests
"""
class TestGDACS(unittest.TestCase):

    # Pull XML from GDACS
    def test_pull(self):
        self.gdacs_data = test_module.gdacs_pull(url=gdacs_url)
        self.assertTrue(self.gdacs_data is not None)
        self.assertTrue(type(self.gdacs_data) is str)
        self.assertRegex(self.gdacs_data, r'.*dateadded.*')


"""
All FEMA Tests
"""
class TestFEMA(unittest.TestCase):

    # Pull JSON from FEMA
    def test_pull(self):
        self.fema_data = test_module.openfema_pull(url=fema_url,
                                                   from_date=formatted_date)
        self.assertTrue(self.fema_data is not None)
        self.assertTrue(type(self.fema_data) is list)
        self.assertGreater(len(self.fema_data), 2,
                           "There should be > 2 elements but found {}".format(
                               len(self.fema_data)))


"""
All EM-DAT Tests
"""
class TestEMDAT(unittest.TestCase):

    # Open the EM-DAT Dummy Data
    def test_open(self):
        self.emdat_csv = test_module.emdat_open(emdat_file)


# Only run if executing, not import
if __name__ == '__main__':

    unittest.main()
