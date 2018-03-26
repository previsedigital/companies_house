from pydoc import Helper

import requests
import json
import urllib.parse
import logging
import csv
import os

from typing import Optional, Callable, Type


class CompaniesHouseAPIBase:
    _base_url = "https://api.companieshouse.gov.uk/{}"
    _api_key: str

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def get(self, query: str) -> Optional[dict]:
        """
        Run a GET query against the Companies' House API
        :param query: the query, e.g.
        :return:
        """
        url: str = self._base_url.format(query)
        response = requests.request('GET', url, auth=(self._api_key, ''))
        if response.status_code != 200:
            # don't raise if not found, just return None
            if response.status_code == 404:
                logging.warning(f'404 not found: {url}')
                return None

            raise requests.HTTPError(response.status_code, response.text)
        return json.JSONDecoder().decode(response.text)


def _make_function(method_name: str, http_request_str: str, description: str) -> Callable:
    method, generic_url = list(map(lambda s: s.strip('/ '), http_request_str.split('\xa0')))
    base_parts = list(filter(None, generic_url.split('/')))
    name = '_'.join(map(lambda s: str.replace(s, '-', '_'), filter(lambda x: '{' not in x, base_parts)))
    params = list(map(lambda s: str.strip(s, '{}'), filter(lambda x: '{' in x, base_parts)))

    def fn(self, **kwargs) -> Optional[dict]:
        missing = list(filter(lambda x: x not in kwargs, params))
        if missing:
            raise Exception(f'Missing arguments: {missing}')
        required_args = {kw: arg for kw, arg in kwargs.items() if kw in params}
        arg_str = '&'.join([f'{kw}={urllib.parse.quote(arg)}'
                            for kw, arg in kwargs.items() if kw not in params])
        url = generic_url.format(**required_args)
        if arg_str:
            url = f'{url}?{arg_str}'
        return self.get(url)

    fn.__name__ = name
    fn.__doc__ = f'{description} ({method_name})\n' + '\n'.join(
        map(lambda param: f':param {param}:', params)
    )
    return fn


class SimpleRecorder:
    def __init__(self):
        self.clear()

    def clear(self):
        self.text = ''

    def write(self, text):
        self.text += text


def _update_readme(api: type, path: str=os.path.join(os.path.dirname(__file__), 'README.md')):
    r = SimpleRecorder()
    h = Helper(output=r)
    h.help(api)
    readme = f'''
# Companies' House API
When running for the first time, or when the API has changed, 
run `update.py` to re-download the API definition. 
When running the API, this documentation is updated automatically.

Simply create an API client as an instance of CompaniesHouseAPI:
```
from companies_house.api import CompaniesHouseAPI
ch = CompaniesHouseAPI(api_key)
```

This will give you access to all the functions registered in the API. For full reference,
refer to [the API documentation](https://developer.companieshouse.gov.uk/api/docs/)
```
help(CompaniesHouseAPI)
```

```
{r.text}
```
'''
    with open(path, 'w') as f:
        f.write(readme)


def generate_api(
        path: str=os.path.join(os.path.dirname(__file__), 'definition.csv')
) -> Type[CompaniesHouseAPIBase]:

    definition = csv.DictReader(open(path))

    functions = {}
    for line in definition:
        fn = _make_function(line['Method'], line['HTTP Request'], line['Description'])
        functions[fn.__name__] = fn

    api_class: Type[CompaniesHouseAPIBase] = \
        type('CompaniesHouseAPI', (CompaniesHouseAPIBase,), functions)
    
    _update_readme(api_class)
    return api_class


CompaniesHouseAPI: Type[CompaniesHouseAPIBase] = generate_api()
