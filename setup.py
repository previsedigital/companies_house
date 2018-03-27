# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version_file = path.join(here, 'version.txt')
with open(version_file, 'r') as f:
    version = f.read()

setup(
    name='companies_house',
    version=version,
    description='Dynamic API wrapper for Companies\' House',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='http://previ.se',
    author='Elias Mistler, Previse Limited',
    author_email='elias@previ.se',

    license='MIT',


    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Internet',
        'Topic :: Office/Business',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='companieshouse api',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    python_requires='>=3',
    install_requires=['pandas'],

    project_urls={
        'Source': 'https://github.com/previsedigital/companies_house',
    },
)
