from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='rfq',
    version=version,
    description='Request For Quotes',
    author='indictrans',
    author_email='anand.pawar@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
