#!/usr/bin/env python
from setuptools import setup, Extension

setup(
    name='eventfd',
    version=0.1,
    packages=['eventfd'],
    license='Simplified BSD License',
    description='threading.Event like class that has a file descriptor and can be used in select/poll',
    long_description=open('README.txt').read(),
    author='Aviv Palivoda',
    author_email='palaviv@gmail.com',
    url='http://eventfd.readthedocs.org',
    ext_modules=[Extension("eventfd._eventfd_c", sources=["eventfd/_eventfd.c"])]
)
