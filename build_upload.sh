#!/usr/bin/env bash
rm -rf dist companies_house.egg-info
python increment_version.py
#python ./companies_house/update.py  # update the api from companies' house
python ./companies_house/api.py  # run to make sure the documentation is up-to-date
python setup.py sdist
python setup.py bdist_wheel

twine upload dist/companies_house-`cat version.txt`.tar.gz  # --repository testpypi
twine upload dist/companies_house-`cat version.txt`-py3-none-any.whl
