#!/bin/env python

import os
from setuptools import setup, find_packages
from glob import glob

def packagez(base):
    return  ["{0!s}{1!s}{2!s}".format(base, os.path.sep, p) for p in find_packages(base)]

setup(
    name = 'pyccp',
    version = '0.9.0',
    provides = ['pyccp'],
    description = "CAN Calibration Protocol for Python",
    author = 'Christoph Schueler',
    author_email = 'cpu12.gems@googlemail.com',
    url = 'http://github.com/christoph2/pyccp',
    packages = packagez('pyccp'),
    install_requires = ['enum34', 'future', 'mako'],    # 'mock'
    #entry_points = {
    #    'console_scripts': [
    #            'readelf.py = objutils.tools.readelf:main',
    #    ],
    #},
    #data_files = [
    #    ('objutils/tests/ELFFiles', glob('objutils/tests/ELFFiles*.*')),
    #],
    package_dir = {'tests': 'pyccp/tests'},
    #package_data = {'tests': ['ELFFiles/*.*']},
    #include_package_data = True,
    test_suite = "pyccp.tests"
)

