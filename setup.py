# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='randrecord',
    version='1.0.1',
    description='Find random recordings',
    long_description=readme,
    author='Patryk Ferenc',
    url='https://github.com/patrykferenc/random-record-retriever',
    license=license,
    packages=find_packages()
)
