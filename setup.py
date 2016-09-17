# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='adbs',
    version='0.0.1',
    description='AD BS Converter',
    long_description=readme,
    author='Samar Acharya',
    author_email='samar+python@techgaun.com',
    url='https://github.com/techgaun/ad-bs-converter.py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
