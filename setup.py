#!/usr/bin/env python

from setuptools.depends import get_module_constant
from setuptools import setup

setup(
    name = 'convertapi',
    packages = ['convertapi'],
    version = get_module_constant('convertapi', '__version__'),
    description = 'Convert API Python Client',
    long_description = 'Convert various files like MS Word, Excel, PowerPoint, Images to PDF and Images. Create PDF and Images from url and raw HTML. Extract and create PowerPoint presentation from PDF. Merge, Encrypt, Split, Repair and Decrypt PDF files. All supported files conversions and manipulations can be found at https://www.convertapi.com/doc/supported-formats',
    author = 'Tomas Rutkauskas',
    author_email = 'support@convertapi.com',
    url = 'https://github.com/ConvertAPI/convertapi-python',
    download_url = 'https://github.com/ConvertAPI/convertapi-python',
    keywords = ['convert', 'api', 'client', 'conversion'],
    install_requires= ['requests>=2.4.2'],
    classifiers = [],
    license = 'MIT',
)
