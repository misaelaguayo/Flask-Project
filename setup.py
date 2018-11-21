# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="flask_project",
    version="1.0.0",
    description="My first Flask web application.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)