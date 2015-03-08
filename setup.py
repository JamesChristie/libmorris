#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
  name='libmorris',
  version='1.0.0',
  author='James Christie',
  author_email='james.aaron.christie@gmail.com',
  url='http://github.com/JamesChristie/libmorris',
  download_url='https://github.com/JamesChristie/libmorris.git',
  description='A library implementation of tic-tac-toe',
  long_description='A library implementation of tic-tac-toe',

  packages = find_packages(),
  include_package_data = True,
  package_data = { 'libmorris': ['libmorris/*'] },
  exclude_package_data = { '': ['README.txt'] },
  
  keywords='python tic-tac-toe minimax',
  license='GPL',
  classifiers=['Development Status :: 5 - Production/Stable',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3',
               'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
               'License :: OSI Approved :: GNU Affero General Public License v3',
               'Topic :: Internet',
               'Topic :: Internet :: WWW/HTTP',
              ],
              
  install_requires = ['setuptools'],
)
