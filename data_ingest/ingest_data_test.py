#!/usr/bin/env python3

import unittest
import ingest_data as id_module


class TestGDACS(unittest.TestCase):

    def test_pull(self):
        self.gdacs_request = id_module.gdacs_pull('https://gdacs.org/xml/rss.xml')
        self.assertTrue(self.gdacs_request is not None)
        self.assertTrue(type(self.gdacs_request) is str)
        self.assertRegex(self.gdacs_request, r'.*dateadded.*')


# Only run if executing, not import
if __name__ == '__main__':

    unittest.main()
