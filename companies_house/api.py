import functools
import inspect
from pydoc import Helper

import requests
import json
import urllib.parse
import logging
import csv
import os

from typing import Optional, Callable, Type, Union

from companies_house.constants import DEFAULT_DEFINITIONS_FILE


class CompaniesHouseAPIBase:
    _base_url = "https://api.companieshouse.gov.uk/{}"
    _api_key: str

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def _follow_links(self, obj: Union[dict, list]) -> Union[dict, list]:
        if isinstance(obj, dict) and 'links' in obj:
            for link_name, link_query in obj['links'].items():
                if link_name == 'self':
                    pass
                else:
                    if link_name in obj:
                        raise Exception(f'Link name shadows builtin: {link_name}')
                    obj[link_name] = self.get(link_query, follow_links=True)
            return obj
        elif isinstance(obj, list):
            return [self._follow_links(o) for o in obj]
        else:
            return obj

    def get(self, query: str, flatten: bool=False, follow_links: bool=False) -> Optional[dict]:
        """
        Run a GET query against the Companies' House API
        :param query: the query, e.g. "company/09117429"
        :param flatten: flatten the result dictionary
        :return: the result as dict
        """
        url: str = self._base_url.format(query)
        response = requests.request('GET', url, auth=(self._api_key, ''))
        if response.status_code != 200:
            # don't raise if not found, just return None
            if response.status_code == 404:
                logging.warning(f'404 not found: {url}')
                return None

            raise requests.HTTPError(response.status_code, response.text)
        result = json.JSONDecoder().decode(response.text)
        if follow_links:
            result = self._follow_links(result)
        if flatten:
            result = flatten_dict(result)
        return result


def flatten_dict(d: dict, full_name: str=None, sep: str='__') -> Union[dict, list]:

    if isinstance(d, dict):
        flat = {}
        for key, val in d.items():
            name = sep.join([full_name, key]) if full_name else key
            flat.update(flatten_dict(val, name, sep))
        return flat

    elif isinstance(d, list):
        flat_dict = {}
        for idx, val in enumerate(d):
            name = sep.join([full_name, str(idx)])
            flat_dict.update(flatten_dict(val, name, sep))
        return flat_dict

    else:
        return {full_name: d}


def _make_function(method_name: str, http_request_str: str, description: str) -> Callable:
    method, generic_url = map(lambda s: s.strip('/ '), http_request_str.replace('\xa0', ' ').split())
    base_parts = list(filter(None, generic_url.split('/')))
    fn_name = '_'.join(map(lambda s: str.replace(s, '-', '_'), filter(lambda x: '{' not in x, base_parts)))
    params = list(map(lambda s: str.strip(s, '{}'), filter(lambda x: '{' in x, base_parts)))

    def fn(self, flatten: bool=False, follow_links: bool=False, **kwargs) -> Optional[dict]:
        arg_str = '&'.join([f'{kw}={urllib.parse.quote(arg)}'
                            for kw, arg in kwargs.items() if kw not in params])

        required_args = {kw: arg for kw, arg in kwargs.items() if kw in params}
        url = generic_url.format(**required_args)

        if arg_str:
            url = f'{url}?{arg_str}'

        return self.get(url, flatten=flatten, follow_links=follow_links)

    def update_signature(fn: Callable) -> Callable:
        old_sig: inspect.Signature = inspect.signature(fn)
        sig_args = list(old_sig.parameters.values())

        sig_args = [
            sig_args[0],
            *[inspect.Parameter(
                param,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                annotation=str
            ) for param in params],
            *sig_args[1:]
        ]

        prefix = method_name.split()[0].lower()
        if prefix and not fn_name.startswith(prefix):
            name = '_'.join([prefix, fn_name])
        else:
            name = fn_name

        def wrapper(*args, **kwargs):
            # Remap non-kwargs onto function.
            for i, value in enumerate(args):
                arg_def = sig_args[i]
                kwargs[arg_def.name] = value

            return fn(**kwargs)

        fn.__name__ = name
        fn.__doc__ = description + '\n' + '\n'.join(
            map(lambda p: f':param {p}:', params)
        )
        fn.__signature__ = old_sig.replace(parameters=sig_args)
        new_func = functools.update_wrapper(wrapper, fn)
        return new_func

    return update_signature(fn)


def generate_api(path: str, force_update: bool=False) -> Type[CompaniesHouseAPIBase]:

    if not os.path.isfile(path) or force_update:
        from companies_house.update import update
        update(path=path)

    functions = {}
    with open(path, encoding='utf-8') as f:
        definition = csv.DictReader(f)
        for line in definition:
            fn = _make_function(line['Operation'], line['HTTP Request'], line['Description'])
            functions[fn.__name__] = fn

    api_class: Type[CompaniesHouseAPIBase] = type(
        'CompaniesHouseAPI', 
        (CompaniesHouseAPIBase,), 
        functions
    )

    return api_class


CompaniesHouseAPI = generate_api(path=DEFAULT_DEFINITIONS_FILE)
