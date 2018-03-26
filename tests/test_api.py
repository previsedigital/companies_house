import unittest
import os

from api import CompaniesHouseAPIBase, CompaniesHouseAPI

API_KEY = os.environ.get('CH_API_KEY')
API_KEY = 'Jh3fh4L8bfMqBSGAwAEJIUHUxp95UtDiATCUO8o_'
if not API_KEY:
    API_KEY = input('Please enter API key!\n')


class CompaniesHouseTestCase(unittest.TestCase):
    def setUp(self):
        self.base_api: CompaniesHouseAPIBase = CompaniesHouseAPIBase(API_KEY)
        self.api: CompaniesHouseAPI = CompaniesHouseAPI(API_KEY)

    def test_api_base(self):
        search_result = self.base_api.get('search')
        self.assertIsInstance(search_result, dict)

    def test_search(self):
        search_result = self.api.search_companies(q='PREVISE')
        self.assertGreater(len(search_result['items']), 0)

    def test_company(self):
        result = self.api.get_company('09117429')
        self.assertIsInstance(result, dict)
