#!/usr/bin/env python

from distutils.core import setup

setup(name='IP-shitlist',
      version='1.0',
      description='IP address shitlist',
      url='https://github.com/oherrala/shitlist',
      py_modules='shitlist',
      scripts=['shitlist.py'],
      license='MIT',
      install_requires=['click'])

