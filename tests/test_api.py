import unittest
import os

from api import CompaniesHouseAPIBase, CompaniesHouseAPI, flatten_dict

API_KEY = os.environ.get('CH_API_KEY')
API_KEY = 'Jh3fh4L8bfMqBSGAwAEJIUHUxp95UtDiATCUO8o_'
if not API_KEY:
    API_KEY = input('Please enter API key!\n')

COMPANY_NUMBER = '09117429'


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
        result = self.api.get_company(COMPANY_NUMBER)
        self.assertIsInstance(result, dict)

    def test_flatten(self):
        inp = dict(a='5', b=dict(deep=dict(val=42)))
        exp = dict(a='5', b__deep__val=42)
        act = flatten_dict(inp)
        self.assertEqual(exp, act)

    def test_flatten_with_list(self):
        inp = dict(l=[1, 2, dict(a=1, b=2)])
        exp = dict(l__0=1, l__1=2, l__2__a=1, l__2__b=2)
        act = flatten_dict(inp)
        self.assertEqual(exp, act)

    def test_flat_result(self):
        result = self.api.get_company(COMPANY_NUMBER, flatten=True)
        self.assertIsInstance(result, dict)