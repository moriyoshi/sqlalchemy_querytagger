from setuptools import setup, find_packages
import os

version = '0.0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='sqlalchemy_querytagger',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/moriyoshi/sqlalchemy_querytagger',
      license='proprietary',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'sqlalchemy == 0.7.4',
      ],
      test_suite='sqlalchemy_querytagger.tests',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
