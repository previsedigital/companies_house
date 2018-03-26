import unittest
import os

from api import CompaniesHouseAPIBase, CompaniesHouseAPI

API_KEY = os.environ.get('CH_API_KEY')
if not API_KEY:
    API_KEY = input('Please enter API key!')


class CompaniesHouseTestCase(unittest.TestCase):
    def setUp(self):
        self.base_api: CompaniesHouseAPIBase = CompaniesHouseAPIBase(API_KEY)
        self.api: CompaniesHouseAPI = CompaniesHouseAPI(API_KEY)

    @unittest.skip
    def test_api_base(self):
        self.assertIsInstance(self.base_api.get('search'), dict)

    def test_api(self):
        help(CompaniesHouseAPI)
        search_result = self.api.search_companies(q='PREVISE')
        print(search_result)
        self.assertGreater(len(search_result['items']), 0)
