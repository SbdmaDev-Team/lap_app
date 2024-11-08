# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in lab_app/__init__.py
from lab_app import __version__ as version

setup(
	name='lab_app',
	version=version,
	description='Lab_App',
	author='eng ezzaldeen alwali',
	author_email='ezwalialwali@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
